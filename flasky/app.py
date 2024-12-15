from datetime import datetime
import socket
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    message = ["Hello, DevDataOps!"]
    message.append('---')
    message.append('version: 0.02')
    message.append('hostname: ' + str(socket.gethostname()))
    message.append('datetime: ' + str(datetime.now()))
    message.append('')
    return '\n'.join(message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
