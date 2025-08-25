from flask import Flask
import os
app = Flask(__name__)
@app.get("/")
def hello():
    version = os.getenv("APP_VERSION", "dev")
    return f"hello from trainsquare demo v{version}\n"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
