from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    title = "This is the homepage"
    text = "type /fizzbuzz/(insert number) in the url"

    return render_template('homepage.html', title=title, text=text)

@app.route("/fizzbuzz/<int:n>")
def fizzbuzz(n):
    result = []
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            result.append("FizzBuzz")
        elif i%3 == 0:
            result.append("Fizz")
        elif i%5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return render_template('fizzbuzz.html', result=result)