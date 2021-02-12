from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contact/')
def contact():
    return render_template("ContactMe.html")

@app.route('/np/')
def np():
    return render_template("NationalParksMap.html")

"""
@app.route('/resume/')
def resume():
    path = "Joshua_Gomes_Resume.pdf"
    return send_file(path, as_attachment=True)
"""

if __name__ == "__main__":
    app.run(debug=True)
