from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1 style="color:pink; text-align:center; margin-top:200px;">
        ❤️ Happy Valentine ❤️
    </h1>
    <p style="text-align:center; font-size:20px;">
        You are my favorite person 💕
    </p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)