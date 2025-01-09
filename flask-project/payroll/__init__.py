from flask import Flask
from payroll import pages

# app = Flask(__name_ 
# @app.route('/')
# def hello():
#     return "Hello Flask"

# def create_app():
#     app = Flask(__name__, instance_relative_config=True)

#     @app.route('/')
#     def hello():
#         return "Hello Flask"
#     return app

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(pages.bp)    
    return app