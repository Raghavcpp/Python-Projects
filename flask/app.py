from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world1():
    return "<h1>Yo It's Raghav</h1>"

@app.route("/a")
def hello_world2():
    return render_template('index.html')


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/welcome/<name>")
def hello_world3(name):
    return f"<h1> You are {name}</h1>"
if __name__ == "__main__":
    app.run(debug=True)