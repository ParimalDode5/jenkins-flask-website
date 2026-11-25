from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "application": "DevOps Demo Website"}), 200


@app.route("/about")
def about():
    return jsonify({
        "project": "DevOps Demo Website",
        "technologies": ["Python", "Flask", "HTML", "CSS", "GitHub", "Jenkins"],
    }), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
