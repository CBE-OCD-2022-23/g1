from flask import Flask
from datetime import datetime

app = Flask(__name__)
number = 0


@app.route('/')
def hello_world():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return ' Hello, World OCB! %s' %current_time

if __name__ == "__main__":
   app.run()