from flask import Flask, render_template
from flask_cors import CORS
from routes.portfolio import portfolio_bp
from routes.translate import translate_bp
from routes.pricing import pricing_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(portfolio_bp, url_prefix="/api")
    app.register_blueprint(translate_bp, url_prefix="/api")
    app.register_blueprint(pricing_bp, url_prefix="/api")

    @app.route("/")
    def home():
        return render_template("index.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
