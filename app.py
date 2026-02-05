from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #1a0033 0%, #330066 50%, #1a0033 100%);
                min-height: 100vh;
                overflow: hidden;
                font-family: Arial, sans-serif;
            }
            
            .lights {
                position: fixed;
                width: 100%;
                height: 100%;
                top: 0;
                left: 0;
                pointer-events: none;
            }
            
            .light {
                position: absolute;
                width: 20px;
                height: 20px;
                border-radius: 50%;
                animation: twinkle 2s infinite;
            }
            
            @keyframes twinkle {
                0%, 100% { opacity: 0.3; }
                50% { opacity: 1; }
            }
            
            .container {
                position: relative;
                z-index: 10;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                text-align: center;
            }
            
            h1 {
                color: #ff1493;
                font-size: 3.5em;
                margin: 20px 0;
                text-shadow: 0 0 20px rgba(255, 20, 147, 0.8);
                animation: heartbeat 1.5s infinite;
            }
            
            @keyframes heartbeat {
                0%, 100% { transform: scale(1); }
                25% { transform: scale(1.05); }
                50% { transform: scale(1.1); }
            }
            
            p {
                color: #ffffff;
                font-size: 1.5em;
                margin: 20px 0;
                text-shadow: 0 0 15px rgba(255, 105, 180, 0.6);
            }
            
            .decorations {
                position: absolute;
                width: 100%;
                height: 100%;
                top: 0;
                left: 0;
                pointer-events: none;
            }
            
            .heart {
                position: absolute;
                opacity: 0.6;
                animation: float 6s infinite ease-in-out;
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0px) rotate(0deg); }
                50% { transform: translateY(-30px) rotate(10deg); }
            }
        </style>
    </head>
    <body>
        <div class="decorations">
            <div class="heart" style="left: 10%; top: 20%; animation-delay: 0s;">💝</div>
            <div class="heart" style="left: 20%; top: 50%; animation-delay: 1s; font-size: 2em;">✨</div>
            <div class="heart" style="left: 30%; top: 30%; animation-delay: 2s;">💖</div>
            <div class="heart" style="left: 75%; top: 25%; animation-delay: 0.5s; font-size: 2.5em;">🌟</div>
            <div class="heart" style="left: 85%; top: 60%; animation-delay: 1.5s;">💝</div>
            <div class="heart" style="left: 15%; top: 75%; animation-delay: 2.5s; font-size: 1.8em;">✨</div>
            <div class="heart" style="left: 70%; top: 80%; animation-delay: 3s;">💕</div>
        </div>
        
        <div class="lights">
            <div class="light" style="background: #ff1493; left: 5%; top: 10%; animation-delay: 0s;"></div>
            <div class="light" style="background: #ff69b4; left: 15%; top: 20%; animation-delay: 0.3s;"></div>
            <div class="light" style="background: #ffb6c1; left: 25%; top: 15%; animation-delay: 0.6s;"></div>
            <div class="light" style="background: #ff1493; left: 75%; top: 10%; animation-delay: 0.2s;"></div>
            <div class="light" style="background: #ff69b4; left: 85%; top: 25%; animation-delay: 0.5s;"></div>
            <div class="light" style="background: #ffb6c1; left: 90%; top: 40%; animation-delay: 0.8s;"></div>
            <div class="light" style="background: #ff1493; left: 10%; top: 85%; animation-delay: 0.4s;"></div>
            <div class="light" style="background: #ff69b4; left: 50%; top: 90%; animation-delay: 0.7s;"></div>
            <div class="light" style="background: #ffb6c1; left: 80%; top: 88%; animation-delay: 1s;"></div>
        </div>
        
        <div class="container">
            <h1>❤️ Happy Valentine ❤️</h1>
            <p>You are my favorite person 💕</p>
            <p style="font-size: 1.2em; margin-top: 40px;">✨ 💖 🌹 💖 ✨</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)