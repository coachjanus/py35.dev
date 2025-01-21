# flask_payroll/payroll/pages.py

from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
	return render_template("pages/home.html")
	# return "Hello, Home!"


@bp.route("/about")
def about():
	return render_template("pages/about.html")
	# return "Hello, About!"

