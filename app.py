#templates are used to separate bussiness logic from presentation logic
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_view():
	return render_template('index.html')
	return render_template('Contact.html')
	return render_template('Home.css')
	return render_template('Home.html')
	return render_template('jquery.js')
	return render_template('nicepage.css')
	return render_template('nicepage.js')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
