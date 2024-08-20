#!/usr/bin/python3
"""Start Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/')
def hello_hbnb():
    """
    Routing to root, airbnb-onepage ensure
    the URL works when it ends both with or without the /
    ""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
