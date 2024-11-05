#!/usr/bin/env python3
""" 0. Basic Flask app. """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False  # routes with or without trailing slashes


@app.route("/")
def welcome():
    """Render the home page with a welcome message."""
    return render_template('0-index.html')


if __name__ == '__main__':
    # Run the app on host 0.0.0.0 to make it accessible externally
    app.run(host='0.0.0.0', port=5000)
