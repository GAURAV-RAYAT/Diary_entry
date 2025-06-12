# Flask Diary Web App
## DEMO : [dairy.gauravrayat.me](https://dairy.gauravrayat.me)

This is a personal diary web application built with **Flask**, supporting:

- ✍️ User registration & login
- 🔐 Session-based authentication
- 📖 Add, view, read, and delete personal diary entries
- 🧠 Data stored securely in SQLite
- 🌐 Deployed with Gunicorn on Render

---

## 🚀 Features

- User authentication (register, login, logout)
- Each user has their own entries
- Bootstrap 5 UI with accordion views
- Flask SQLAlchemy + Bcrypt security
- WSGI-ready (via Gunicorn)

---

## 📸 Screenshots

### Home Page
![Home](/static/home.png)

### Register
![View Entries](/static/register.png)

### Login Page
![Login](/static/login.png)

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Flask SQLAlchemy
- Flask Login
- Flask Bcrypt
- Gunicorn (for deployment)

---

## 🧑‍💻 Local Setup

1. **Clone the repo**

```bash
git clone https://github.com/YOUR_USERNAME/flask-diary-app.git
cd flask-diary-app
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run locally**

```bash
python app.py
```

Open in browser: `http://localhost:5000`

---

## 🌍 Deploying to Render

1. Push your project to GitHub
2. Go to [https://render.com](https://render.com)
3. Create a new **Web Service**
4. Set these fields:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. App will be deployed with a live URL!

---

## 📁 Project Structure

```
flask-diary-app/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── view.html
│   ├── read.html
│   ├── login.html
│   └── register.html
├── static/
│   ├── my-avatar.png
├── requirements.txt
├── Procfile
└── README.md
```

---

## 🙌 Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Render](https://render.com)

---

> Built with ❤️ by Gaurav Rayat
> [Portfolio](https://gauravrayat.me)