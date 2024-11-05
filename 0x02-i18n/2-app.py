#!/usr/bin/env python3
""" Basic Flask app with Babel and locale selector. """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration for Babel and supported languages."""
    LANGUAGES = ["en", "fr"]  # Supported languages
    BABEL_DEFAULT_LOCALE = "en"  # Default language
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def welcome() -> str:
    """Render the home page with a welcome message."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
