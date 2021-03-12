from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    return render_template('homepage.html')
     

@app.route('/form')
def show_form():
    """Shows the form."""
    
    return render_template("form.html")

@app.route('/results')
def show_results():
    """Shows the results."""

    cheery = request.args.get('cheery')
    honest = request.args.get('honest')
#     dreary = request.args.get('dreary')

    if cheery:
        message = "You are a wonderful person who will continue to jump around in fuzzy clouds forever"

    else:
        message = "We're all admiring you for your loyalty and deviance."

    return render_template("results.html", 
                            message=message)

@app.route('/save-name', methods=["POST"])
def save_name():
    name = request.form.get('name')
    session['name'] = name

    return render_template('form.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
