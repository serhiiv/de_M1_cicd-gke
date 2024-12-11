import os
import socket
from flask import Flask, render_template

app = Flask(__name__)

app.config['WORKFLOW'] = os.getenv('WORKFLOW', 'None')
workflow = os.getenv('WORKFLOW')

ip = socket.gethostbyname(socket.gethostname())
name = socket.gethostname()


@app.route("/")
def hello_world():
    return render_template('main.html', name=name, ip=ip, workflow=app.config['WORKFLOW'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
