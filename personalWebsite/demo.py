from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello you gorgeous Flask developer"

@app.route('/about/')
def about():
    return "This is the start of something new"

if __name__ == "__main__":
    app.run(debug=True)
