from flask import Flask
from extensions import db, login_manager

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)
    login_manager.init_app(app)

    # Import routes (IMPORTANT: inside function)
    from routes.auth import auth
    from routes.tasks import tasks

    app.register_blueprint(auth)
    app.register_blueprint(tasks)

    return app


app = create_app()

# Create DB
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)