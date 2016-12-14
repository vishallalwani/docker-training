from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask inside Docker!!"


if __name__ == "__main__":
    app.run(debug=True,port=5000,host='0.0.0.0')