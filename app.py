from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/NBA_Tableau/")
def dashboard():
  return render_template("NBA_Tableau.html")

@app.route("/powerpoint/")
def powerpoint():
  return render_template("powerpoint.html")

if __name__ == "__main__":
  app.run(debug=True)