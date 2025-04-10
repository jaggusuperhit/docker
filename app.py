from flask import Flask
from flask_talisman import Talisman

# Initialize Flask app and enforce HTTPS using Flask-Talisman
app = Flask(__name__)
Talisman(app)

@app.route('/')
def index():
    return '''
        <html>
        <head>
            <title>Secure Flask App</title>
        </head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
            <h1>Welcome to the Secure Flask App!</h1>
            <p>This Flask app enforces HTTPS using Flask-Talisman.</p>
        </body>
        </html>
    '''

if __name__ == '__main__':
    # Runs the Flask application on 0.0.0.0 with port 5000
    app.run(host='0.0.0.0', port=5000)
