"""flask_payroll/payroll/__init__.py: Initialize Flask application."""
# 
from flask import Flask
import os 

from payroll import pages, database, staff, departments, auth, books

def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
        SECRET_KEY="Bala bala bal",
        DATABASE=os.path.join(app.instance_path, 'payroll.sqlite')    
    )
	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
	app.config.from_pyfile("application.cfg", silent=True)

	database.init_app(app)

	# if test_config is None:
	# 	# load the instance config, if it exists, when not testing
	# 	app.config.from_pyfile('application.cfg', silent=True)
	# else:
	# 	# load the test config if passed in
	# 	app.config.from_mapping(test_config)


	print(app.config['SECRET_KEY'])
	print(app.config['DATABASE'])
	
	app.register_blueprint(pages.bp)
	app.register_blueprint(staff.bp)
	app.register_blueprint(departments.bp)
	app.register_blueprint(auth.bp)
	app.register_blueprint(books.bp)
	
	return app
