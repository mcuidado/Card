from flask import Flask,render_template, url_for
# https://html5up.net/ethereal
app = Flask(__name__)

# url_for("static", "index.html")
# url_for("static", filename= "style.css")


@app.route("/")
def welcome():
    return render_template("index.html")


# @app.route("/<name>")
# def welcome(name):
#     return render_template("index.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)