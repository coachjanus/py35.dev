from flask import Flask
from payroll import pages, database
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'payroll.db')
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    database.init_app(app)

    app.register_blueprint(pages.bp)    
    return app

