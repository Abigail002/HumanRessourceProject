from app import app
from config import db
from models import Employee, Department, Project
from flask import jsonify, render_template, request

with app.app_context():
    db.drop_all()
    db.create_all()
    department1 = Department(name="Informatique", location="Agoè")
    department1 = Department(name="Electronique", location="Agoè")

    employee1 = Employee(firstname="John", lastname="KOJU",
                         department=department1)
    employee2 = Employee(firstname="Ali", lastname="LOZO", manager=department1)
    # department1.employees.append(employee1)
    db.session.add(employee1)
    db.session.add(department1)
    db.session.commit()

"""CRUD operations for the Employee table"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employeeAdd', methods=['POST'])
def employeeRegister():
    try:
        json = request.json
        print (json)
        firstname = json['firstname']
        lastname = json['lastname']
        departmentId = json['departmentId_']
        #isHeadOF = json['isHeadOF']

        if firstname and lastname and request.method == 'POST':
            # Creation an employee
            employee = Employee(firstname=firstname, lastname=lastname)
            print("****************************************")
            print(employee)

            if departmentId:
                department = Department.query.filter_by(id=departmentId).first()
                print(department)
                employee.department = department

            db.session.add(employee)
            db.session.commit()
            response = jsonify('Nouveau employé ajouté avec succès')
            return response
        else:
            message = {'status': 404, 'message': 'Entrées invalides'}
            response = jsonify(message)
            response.status_code = 404
            return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        db.session.rollback()
        return message
    finally:
        db.session.close()


@app.route('/employees', methods=['GET'])
def getEmployees():
    try:
        employees = Employee.query.all()
        data = [{"id": employee.id, "Nom": employee.lastname,
                 "Prénom": employee.firstname} for employee in employees]
        print(data)
        response = jsonify({"statut_code": 200, "employees": data})
        return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message


@app.route('/employee/update', methods=['POST'])
def employeeUpdate():
    try:
        data = request.json
        id = data["id"]
        firstname = data["firstname"]
        lastname = data["lastname"]
        employee = Employee.query.filter_by(id=id).first()
        if id and firstname and lastname and request.method == 'POST':
            employee.firstname = firstname
            employee.lastname = lastname
            db.session.commit()
            response = jsonify(
                'Les informations de l"employé ont été modifiées')
            return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/employee/delete/', methods=['POST'])
def deleteEmployee():
    try:
        json = request.json
        id = json['id']

        employee = Employee.query.filter_by(id=id).first()
        db.session.delete(employee)
        db.session.commit()
        resultat = jsonify('Employé supprimé ♠♦')
        return resultat
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message
    finally:
        db.session.rollback()
        db.session.close()


"""CRUD operations for the Department table"""


@app.route('/departmentAdd', methods=['POST'])
def departmentRegister():
    try:
        json = request.json
        print(json)
        name = json['name']
        location = json['location']

        if name and location and request.method == 'POST':
            # Creation a department
            department = Department(name=name, location=location)
            print("*******************")

            db.session.add(department)
            db.session.commit()
            response = jsonify('Nouveau département ajouté avec succès')
            return response
        else:
            message = {'status': 404, 'message': 'Entrées invalides'}
            response = jsonify(message)
            response.status_code = 404
            return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        db.session.rollback()
        return message
    finally:
        db.session.close()


@app.route('/departments', methods=['GET'])
def getDepartments():
    try:
        departments = Department.query.all()
        data = [{"id": department.id, "Name": department.name,
                 "Location": department.location} for department in departments]
        print(data)
        response = jsonify({"statut_code": 200, "departments": data})
        return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message


@app.route('/department/update', methods=['POST'])
def departmentUpdate():
    try:
        data = request.json
        id = data["id"]
        name = data["name"]
        location = data["location"]
        department = Department.query.filter_by(id=id).first()
        if id and name and location and request.method == 'POST':
            department.name = name
            department.location = location
            db.session.commit()
            response = jsonify(
                'Les informations du département ont été modifiées')
            return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/department/delete/', methods=['POST'])
def deleteDep():
    try:
        json = request.json
        id = json['id']

        dep = Department.query.filter_by(id=id).first()
        db.session.delete(dep)
        db.session.commit()
        resultat = jsonify('Département supprimé ♠♦')
        return resultat
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message
    finally:
        db.session.rollback()
        db.session.close()


"""CRUD operations for the Project table"""


@app.route('/projectAdd', methods=['POST'])
def projectRegister():
    try:
        json = request.json
        name = json['name']

        if name and request.method == 'POST':
            # Creation an project
            project = Project(name=name)

            db.session.add(project)
            db.session.commit()
            response = jsonify('Nouveau projet ajouté avec succès')
            return response
        else:
            message = {'status': 404, 'message': 'Entrées invalides'}
            response = jsonify(message)
            response.status_code = 404
            return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        db.session.rollback()
        return message
    finally:
        db.session.close()


@app.route('/projects', methods=['GET'])
def getprojects():
    try:
        projects = Project.query.all()
        data = [{"id": project.id, "Name": project.name}
                for project in projects]
        print(data)
        response = jsonify({"statut_code": 200, "projects": data})
        return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message


@app.route('/project/update', methods=['POST'])
def projectUpdate():
    try:
        data = request.json
        id = data["id"]
        name = data["name"]
        employee = Employee.query.filter_by(id=id).first()
        if id and name and request.method == 'POST':
            employee.name = name
            db.session.commit()
            response = jsonify('Les informations du projet ont été modifiées')
            return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/project/delete/', methods=['POST'])
def deleteProject():
    try:
        json = request.json
        id = json['id']

        project = Project.query.filter_by(id=id).first()
        db.session.delete(project)
        db.session.commit()
        resultat = jsonify('Projet supprimé ♠♦')
        return resultat
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message
    finally:
        db.session.rollback()
        db.session.close()


if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port="3000")
