from flask import Flask

app = Flask(__name__)

# what request are we going to understand


@app.route('/')  # http://www.google.com/
def home():
    return "Hello world!"


app.run(port=5000)
