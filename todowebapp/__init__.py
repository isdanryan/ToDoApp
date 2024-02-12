from dotenv import load_dotenv
import os
from flask import Flask

# load enviroment variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY

    # import routes
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app