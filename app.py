#templates are used to separate bussiness logic from presentation logic
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_view():
	return render_template('index.html','Contact.html','Home.css','jquery.js','nicepage.css','index.html','nicepage.js')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
