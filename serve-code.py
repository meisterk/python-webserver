from flask import Flask

app = Flask("my hello app")


@app.route("/hello")
def hello():
    return "Hello World!"


app.run()
