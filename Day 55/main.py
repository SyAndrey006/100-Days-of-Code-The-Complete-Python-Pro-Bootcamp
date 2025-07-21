from flask import Flask
import random

app = Flask(__name__)

chosen_number = random.randint(0, 9)
print(chosen_number)

@app.route("/")
def main():
    return ('<h1>Guess the number from 1 to 10?</h1>'
            '<img src = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaml2ZGpoOHJpNGV2eHUxY2M5anZyOTlmOXNkcnhlazhjbzh5cnE1biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ggM9uqf27nBkH9uwk1/giphy.gif", width = 200>')


@app.route("/<int:number>")
def check(number):
    if number == chosen_number:
        return ('<p style="color: green" >You guessed it!</p>'
                '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2dvcm1oM2s5NWJzazhtZmthdzBocjlid2QxeXYybnN0NHF6dTZnZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7SfAXqgRgh0li/giphy.gif", width=200>')
    elif number < chosen_number:
        return ('<p style="color: red">Too low. Try again!</p>'
                '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3Q4bmN2OXg4Z290dWo4MTRibWwwZXdpMzVuMWFhcHpudDd5b2sxeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CM1rHbKDMH2BW/giphy.gif", width = 200>')
    else:
        return ('<p style="color: purple">Too high. Try again!</p>'
                '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTN5d2Q1MmR0MjM1a2l1OWw5azVlZDBiZzdhNjF4Zmt6MWRob3NpNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3OhXBaoR1tVPW/giphy.gif", width = 200>')

if __name__ == "__main__":
    app.run(debug=True)

#set FLASK_APP=server.py
#python -m flask run