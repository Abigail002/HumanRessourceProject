from config import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    departmentId = db.Column(db.Integer, db.ForeignKey(
        'department.id'), nullable=True)
    # backref cré de façon virtuel une variable department dans la classe employee
    department = db.relationship(
        'Department', backref='employee', foreign_keys=[departmentId])
    isHeadOf = db.Column(db.Integer, db.ForeignKey(
        'department.id'), nullable=True)
    manager = db.relationship(
        'Department', backref='employeeIs', foreign_keys=[isHeadOf])


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)


    # backref cré de façon virtuel une variable department dans la classe employee
"""     employees = db.relationship('Employee', backref='department')
    head = db.relationship('Employee', backref='headOfDepartment')
 """


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)


# Table d'association
projectMembers = db.Table('project_members', db.Column('emplyee_id', db.ForeignKey('employee.id'), primary_key=True),
                          db.Column('project_id', db.ForeignKey('project.id'), primary_key=True))
