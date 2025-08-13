from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_menu():
    return render_template('main.html')

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 locally if PORT not set
    app.run(host="0.0.0.0", port=port)


