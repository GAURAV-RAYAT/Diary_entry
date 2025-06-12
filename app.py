try:
    from flask import Flask, render_template, request, redirect
    from flask_sqlalchemy import SQLAlchemy
    from datetime import datetime
    from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
    from flask_bcrypt import Bcrypt
except:
    print("can't able to acces flask")


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b009982614f34614370746a489d3ceca'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dairy.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
bcrypt = Bcrypt(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    entries = db.relationship('Entry', backref='author', lazy=True)

    def __repr__(self) -> str:
        return f"{self.id} - {self.username}"

class Entry(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    entry_content = db.Column(db.String(10000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self) -> str:
        return f"{self.sno} - {self.title} | {self.date_created}"

#Creating DATABASE
with app.app_context():
    db.create_all()
    print("Database created successfully!")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# LOGIC STARTS HERE
from flask import flash, session

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect('/')
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method=='POST':
        title = request.form['title']
        entry_content = request.form['entry_content']

        entry = Entry(title=title, entry_content=entry_content, author=current_user)
        db.session.add(entry)
        db.session.commit()

    allpro = Entry.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', allpro=allpro)

@app.route('/delete/<int:sno>')
def delete(sno):
    pro = Entry.query.filter_by(sno=sno).first()
    db.session.delete(pro)
    db.session.commit()
    return redirect("/")

@app.route('/read/<int:sno>')
def read(sno):
    pro = Entry.query.filter_by(sno=sno).first()
    print(pro)
    return render_template("read.html",pro=pro)

@app.route('/view')
@login_required
def view():
    allpro = Entry.query.filter_by(user_id=current_user.id).all()
    return render_template('view.html', allpro=allpro)