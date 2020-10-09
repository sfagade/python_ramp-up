from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/height_collector'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email_ = email
        self.height_ = height


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/fileUpload")
def file_upload():
    return render_template("file_uploader.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        if db.session.query(Data).filter(Data.email_ == email).count() < 1:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height, 2)
            count = db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)
            print(average_height)
            return render_template("success.html")

        return render_template("index.html", text="Email address already exist")


@app.route("/upload", methods=['POST'])
def upload_file():
    global file
    if request.method == 'POST':
        file = request.files["file_"]
        file.save(secure_filename("uploaded"+file.filename))
        with open("uploaded"+file.filename, "a") as f:
            f.write("This was added now!")

        print(type(file))
        return render_template("file_uploader.html", btn="download.html")


@app.route("/download")
def download():
    return send_file("uploaded" + file.filename, attachment_filename="yourfile.csv", as_attachment=True)



if __name__ == '__main__':
    app.debug = True
    app.run()
