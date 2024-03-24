from flask import Flask, redirect, render_template, url_for
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="challa",
    password="MyDBPassword",
    hostname="challa.mysql.pythonanywhere-services.com",
    databasename="challa$quotes",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Quote(db.Model):

    __tablename__ = "quotes"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))
    author = db.Column(db.String(512))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", quotes=Quote.query.all())

    #comments.append(request.form["contents"])
    quote = Quote(content=request.form["contents"])
    db.session.add(quote)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/hello")
def hello():
    return "<h2>Hello world!, from Shiva!</h2>"
