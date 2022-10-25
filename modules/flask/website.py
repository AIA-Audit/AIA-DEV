from flask import Flask, render_template
import logging
import threading
app = Flask(__name__,
            static_url_path='',
            static_folder='./frontend/dist',
            template_folder="./frontend/dist")


@app.route('/')
def hello_world():
    return render_template('index.html')


def website_start():
    log = logging.getLogger('werkzeug')
    log.disabled = True
    _thread = threading.Thread(target=lambda: app.run(host="0.0.0.0", port="5000", debug=False, use_reloader=False))
    _thread.setDaemon(True)
    _thread.start()
    return _thread
