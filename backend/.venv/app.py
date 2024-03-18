from flask import Flask, send_from_directory

homepage = "../../react-app/public"

app = Flask(__name__)


# Homepage
@app.route("/")
def hellow_world():
    return send_from_directory(homepage, "index.html")

@app.route("/hello")
def hello_page():
    return "<h1>Welcome welcome</h1>"
	
	