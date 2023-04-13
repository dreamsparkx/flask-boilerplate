import os
from flask import Flask


def create_app(test_config=None):   # create_app is the application factory function
    # create and configure the app
    # __name__ is the name of the current Python module. The app needs to know where it’s located to set up some paths, and __name__
    # is a convenient way to tell it that.
    # instance_relative_config=True tells the app that configuration files are relative to the instance folder. The instance folder is
    # located outside the flaskr package and can hold local data that shouldn’t be committed to version control, such as configuration secrets and the database file.
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(    # sets some default configuration that the app will use:
        # used by Flask and extensions to keep data safe. It’s set to 'dev' to provide a convenient value during development, but it
        # should be overridden with a random value when deploying.
        SECRET_KEY='dev',
        # path where the SQLite database file will be saved. It’s under app.instance_path, which is the path that Flask has chosen for
        # the instance folder. You’ll learn more about the database in the next section.
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        #  ensures that app.instance_path exists. Flask doesn’t create the instance folder automatically,
        # but it needs to be created because your project will create the SQLite database file there.
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "hello"

    from . import db
    from . import auth
    from . import blog
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
