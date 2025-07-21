from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/b9d21b4c923db38e247c").json()

app = Flask(__name__)

my_email = "andrew.100daysofcode@gmail.com"
my_password = "udlc znvi edws qoox"

@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(my_email, my_email, email_message)

if __name__ == "__main__":
    app.run(debug=True, port=5001)


#set FLASK_APP=main.py
#python -m flask run