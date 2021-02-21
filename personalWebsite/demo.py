from flask import Flask, render_template, send_file, make_response

app = Flask(__name__)


@app.route('/')
def home():
    resp = make_response('Hello, World!')
    # Set a same-site cookie for first-party contexts
    resp.set_cookie('cookie1', 'value1', samesite='Lax')
    # Set a cross-site cookie for third-party contexts
    resp.set_cookie('cookie2', 'value2', samesite='None', secure=True)
    return render_template("index.html")

"""
@app.route('/')
def home():
    return render_template("index.html")
"""

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
