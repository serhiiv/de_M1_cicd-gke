from datetime import datetime
import socket
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    message = ["Hello, DevDataOps!"]
    message.append('version: 0.01')
    message.append(socket.gethostname())
    message.append(str(datetime.now()))
    return '\n'.join(message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
