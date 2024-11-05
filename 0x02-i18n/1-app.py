#!/usr/bin/env python3
""" Basic Flask app with Babel setup. """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration for Babel and supported languages."""
    LANGUAGES = ["en", "fr"]  # Supported languages
    BABEL_DEFAULT_LOCALE = "en"  # Default language
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False  # Allows flexible URL routing

babel = Babel(app)  # Initialize Babel for app


@app.route("/")
def welcome() -> str:
    """Render the home page with a welcome message."""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
