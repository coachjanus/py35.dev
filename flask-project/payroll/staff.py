# flask_payroll/payroll/staff.py

# from flask import Blueprint, render_template
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from werkzeug.exceptions import abort

from payroll.database import get_db

from payroll.auth import login_required

bp = Blueprint("staff", __name__)

@bp.route("/staff/index")
def index():
	db = get_db()
	employees = db.execute(
        'SELECT emp.id emp_id, employee_name, department_id, department_name, join_date, role_id, role_name'
        ' FROM employee emp JOIN roles r ON emp.role_id = r.id'
		' JOIN departments d ON emp.department_id = d.id'
        ' ORDER BY department_id ASC'
    ).fetchall()
	return render_template("staff/index.html", employees = employees)


@bp.route("/staff/create", methods=("GET", "POST"))
@login_required
def create():

    db = get_db()
    departments = db.execute('SELECT id, department_name FROM departments').fetchall()
    roles = db.execute('SELECT id, role_name FROM roles').fetchall()

    if request.method == "POST":
        employee_name = request.form["employee_name"]
        department_id = int(request.form["department_id"])
        role_id = int(request.form["role_id"])
        weekly_salary = float(request.form["weekly_salary"]) or 0
        commission_per_sale = float(request.form["commission_per_sale"]) or 0
        hour_rate = float(request.form["hour_rate"]) or 0


        if role_id in (1, 2, 3, 4):
            db.execute(
                "INSERT INTO employee(employee_name, weekly_salary, commission_per_sale, hour_rate, role_id, department_id)  VALUES (?, ?, ?, ?, ?, ?)", (employee_name, weekly_salary, commission_per_sale, hour_rate, role_id, department_id),
            )
            db.commit()
    
        
        else:
            flash("Something goes wrong : ", category="error")
            # return redirect(url_for("staff.create"))

        current_app.logger.info(f"New employee {employee_name} was hired")
        flash(f"New employee {employee_name} was hired", category="success")
        return redirect(url_for("staff.index"))
        
    return render_template("staff/create.html", roles = roles, departments=departments)

def get_employee(id):
    employee = get_db().execute(
        'SELECT * FROM employee WHERE id = ?', (id,)).fetchone()

    if employee is None:
        flash(f"Employee id: {id} doesn't exist.", category="error")
        current_app.logger.info(f"Employee id: {id} doesn't exist.")
        abort(404, f"Employee id: {id} doesn't exist.")

    return employee


@bp.route('/staff/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    employee = get_employee(id)
    departments = get_db().execute('SELECT id, department_name FROM departments').fetchall()
    roles = get_db().execute('SELECT id, role_name FROM roles').fetchall()

    if request.method == 'POST':
        employee_name = request.form["employee_name"]
        department_id = int(request.form["department_id"])
        role_id = int(request.form["role_id"])
        weekly_salary = float(request.form["weekly_salary"]) or 0
        commission_per_sale = float(request.form["commission_per_sale"]) or 0
        hour_rate = float(request.form["hour_rate"]) or 0
        error = None

        if not employee_name:
            error = 'employee name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE employee SET employee_name = ?, department_id = ?, role_id = ?, weekly_salary=?, commission_per_sale=?, hour_rate=? WHERE id = ?',
                (employee_name, department_id, role_id, weekly_salary, commission_per_sale, hour_rate, id)
            )
            db.commit()
            return redirect(url_for('staff.index'))

    return render_template("staff/update.html", roles = roles, departments=departments, employee=employee)


@bp.route('/staff/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_employee(id)
    db = get_db()
    db.execute('DELETE FROM employee WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('staff.index'))
