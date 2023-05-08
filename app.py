from flask import Flask, render_template

app = Flask(__name__)

criteria = [
    {
        "title": "scalability",
        "weight": 0,
        "total_score": 0
    },
    {
        "title": "adaptability",
        "weight": 0,
        "total_score": 0
    },
    {
        "title": "easy-of-use",
        "weight": 0,
        "total_score": 0
    },
    {
        "title": "price",
        "weight": 0,
        "total_score": 0
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',
                           criteria=criteria)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)