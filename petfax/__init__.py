from flask import Flask

# factory
def create_app():
    app = Flask(__name__)

    # index route
    @app.route('/')
    def index():
        return 'Hello, Petfax!'

    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    # register fact blueprint
    from . import fact
    app.register_blueprint(fact.bp)

    return app