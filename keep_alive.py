import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    print("Ping received!")
    return "I am alive!"

def run():
    port = int(os.environ.get("PORT", 8082))
    # Disable debug mode to pass production checks
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

def keep_alive():
    t = Thread(target=run, daemon=True)
    t.start()
