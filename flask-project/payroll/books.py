# flask_payroll/payroll/books.py

# http://books.toscrape.com
# This is a demo website for web scraping purposes. 
# Prices and ratings here were randomly assigned and have no real meaning.

from flask import Blueprint, render_template
from .scraper.catalog import Catalog

bp = Blueprint("books", __name__, url_prefix='/books')
book_app = Catalog()

@bp.route("/list")
def list():
	items = book_app.books()
	return render_template("books/index.html", items=items)

@bp.route("/best")
def best():
	items = book_app.best_books()
	return render_template("books/index.html", items=items)

@bp.route("/cheapest")
def cheapest():
	items = book_app.cheapest_books()
	return render_template("books/index.html", items=items)
