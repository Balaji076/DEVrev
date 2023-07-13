from flask import Flask, render_template
 
app = Flask(__name__)
 
 
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/flightsearch")
def flightsearch():
    return render_template("flightsearch.html")

@app.route("/flightbooking")
def flightbooking():
    return render_template("flightbooking.html")

@app.route("/userbooking")
def userbooking():
    return render_template("userbooking.html")
 
if (__name__ == "__main__"):
    app.run(debug=True)








































    