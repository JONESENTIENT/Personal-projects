from flask import Flask

# Step 1 This doesnt matter to understand. Just initialises flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'This is the secret key  that stores user data'
    
    # to tell flask there are blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app