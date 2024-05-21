try:
    from flask import Flask, render_template, request, redirect
    from flask_sqlalchemy import SQLAlchemy
    from datetime import datetime
except:
    print("can't able to acces flask")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dairy.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Entry(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    entry_content = db.Column(db.String(10000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title} | {self.date_created}"

# LOGIC STARTS HERE
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        title = request.form['title']
        entry_content = request.form['entry_content']

        entry = Entry(title=title,entry_content=entry_content)
        db.session.add(entry)
        db.session.commit()
        
    allpro = Entry.query.all() 
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
def view():
    allpro = Entry.query.all() 
    return render_template('view.html', allpro=allpro)

if __name__ == "__main__":
    app.run(debug=True, port=5000)