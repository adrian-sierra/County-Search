from flask import Flask, render_template, request, redirect
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from case_number import *
from file_date import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(15), nullable=False)
    first_name = db.Column(db.String(15), nullable=False)
    middle_name = db.Column(db.String(15))
    address = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date, nullable=False)
    plaintiff = db.Column(db.String(30))
    citation_number = db.Column(db.String(10), nullable=False, unique=True)
    case_number = db.Column(db.String(30), nullable=False, unique=True)
    case_status = db.Column(db.String(8), nullable=False)
    case_type = db.Column(db.String(10), nullable=False)
    file_date = db.Column(db.Date, nullable=False)
    offenses = db.relationship('Offense', backref='case', lazy=True)

    def __repr__(self):
        return '<Case %r>' % self.id

class Offense(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    offense_description = db.Column(db.String(20), nullable=False)
    offense_date = db.Column(db.Date, nullable=False)
    offense_type = db.Column(db.String(20), nullable=False)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    
    def __repr__(self):
        return '<Offense %r>' % self.offense_description


@app.route('/')
def index():
        return render_template("index.html")
    
@app.route('/add', methods=['POST', 'GET'])
def add():
    def convertDate(input):
        return date(int(input.split("-")[0]), int(input.split("-")[1]), int(input.split("-")[2]))
    
    def earliestFileDate(date_one, date_two):
        if (date_one.year < date_two.year):
            return date_one
        elif (date_one.year > date_two.year):
            return date_two
        else:
            if (date_one.month < date_two.month):
                return date_one
            elif (date_one.month > date_two.month):
                return date_two
            else:
                if (date_one.day < date_two.day):
                    return date_one
                elif (date_one.day > date_two.day):
                    return date_two
                else:
                    return date_one
        
    if request.method == 'POST':
        
        min_file_date = convertDate(request.form.getlist('offense-date')[0])
        for i in range (1, len(request.form.getlist('offense'))):
            min_file_date = earliestFileDate(min_file_date, convertDate(request.form.getlist('offense-date')[i]))
        # print(min_file_date)

        case_plaintiff = request.form['plaintiff']
        case_lastName = request.form['last-name']
        case_firstName = request.form['first-name']
        case_middleName = request.form['middle-name']
        case_address = request.form['address']
        case_dateOfBirth = convertDate(request.form['dob'])
        case_caseType = request.form['case-type']
        case_citationNumber = request.form['citation-number']
        case_caseStatus = request.form['case-status']
        case_fileDate = fileDateGenerator(min_file_date)
        case_caseNumber = caseNumberGenerator(case_caseType, case_fileDate.year)
        new_case = Case(
                        case_number=case_caseNumber,
                        file_date=case_fileDate,
                        plaintiff=case_plaintiff, 
                        last_name=case_lastName, 
                        first_name=case_firstName, 
                        middle_name=case_middleName, 
                        address=case_address,
                        date_of_birth=case_dateOfBirth,
                        citation_number=case_citationNumber,
                        case_status=case_caseStatus,
                        case_type=case_caseType
                        )
        try:
            db.session.add(new_case)
            for i in range (len(request.form.getlist('offense'))):
                offense_object_to_add = Offense(
                            offense_description=request.form.getlist('offense')[i],
                            offense_date=convertDate(request.form.getlist('offense-date')[i]),
                            offense_type=request.form.getlist('offense-type')[i],
                            case=new_case
                            )
                db.session.add(offense_object_to_add)
            db.session.commit()
            return redirect('/add')
        except:
            return "error"
        
    else:
        return render_template("add.html")

@app.route('/results')
def results():
    cases = Case.query.order_by(Case.file_date.asc()).all()
    return render_template("results.html", cases=cases)

@app.route('/delete/<int:id>')
def delete(id):
    case_to_delete = Case.query.get_or_404(id)
    try:
        for i in range(len(case_to_delete.offenses)):
            db.session.delete(case_to_delete.offenses[i])
        db.session.delete(case_to_delete)
        db.session.commit()
        return redirect('/results')
    except:
        return "error"
    
@app.route('/view/<int:id>')
def view(id):
    case_to_view = Case.query.get(id)
    return render_template("record.html", case_to_view=case_to_view)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
