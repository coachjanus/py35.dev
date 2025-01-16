from flask import Blueprint, render_template
from payroll.database import get_db
bp = Blueprint("staff", __name__)

@bp.route('/staff')
def index():
    db = get_db()
    employees = db.execute(
        "SELECT emp.id emp_id, employee_name, department_id, department_name, join_date, role_id, role_name FROM employee emp JOIN roles r ON emp.role_id = r.id JOIN department d ON emp.department_id = d.id ORDER BY department_id ASC"
    ).fetchall()

    return render_template('staff/index.html', employees=employees)


@bp.route("/staff/create")
def create():
   db = get_db()
   departments = db.execute('SELECT id, department_name FROM department').fetchall()
   roles = db.execute('SELECT id, role_name FROM roles').fetchall()
   return render_template("staff/create.html", roles = roles, departments=departments)