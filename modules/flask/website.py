from flask import Flask
import logging
import threading
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def website_start():
    log = logging.getLogger('werkzeug')
    log.disabled = True
    _thread = threading.Thread(target=lambda: app.run(host="0.0.0.0", port="5000", debug=False, use_reloader=False))
    _thread.setDaemon(True)
    _thread.start()
    return _thread
