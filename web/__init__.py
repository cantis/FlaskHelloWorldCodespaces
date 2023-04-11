from flask import Flask


def create_app():
    '''Create the flask app'''
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return '<h1>Hello, World!</h1>'
    # app.config.from_object('config')
    # app.config.from_envvar('APP_CONFIG_FILE')

    # Register blueprints
    # from web import views
    # app.register_blueprint(views.bp)

    return app