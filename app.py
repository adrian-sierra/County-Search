from flask import Flask, render_template, request, redirect
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from case_number import *
from file_date import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class CountySearch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_number = db.Column(db.String(30))
    plaintiff = db.Column(db.String(30))
    last_name = db.Column(db.String(15), nullable=False)
    first_name = db.Column(db.String(15), nullable=False)
    middle_name = db.Column(db.String(15))
    address = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date, nullable=False)
    citation_number = db.Column(db.String(10), nullable=False)
    case_status = db.Column(db.String(8), nullable=False)
    case_type = db.Column(db.String(10), nullable=False)
    offense = db.Column(db.String(10), nullable=False)
    offense_date = db.Column(db.Date, nullable=False)
    offense_type = db.Column(db.String(20), nullable=False)
    file_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<County Search %r>' % self.id


@app.route('/')
def index():
        return render_template("index.html")
    
@app.route('/add', methods=['POST', 'GET'])
def add():
    def convert_date(input):
        return date(int(input.split("-")[0]), int(input.split("-")[1]), int(input.split("-")[2]))
        
    if request.method == 'POST':
        case_plaintiff = request.form['plaintiff']
        case_lastName = request.form['last-name']
        case_firstName = request.form['first-name']
        case_middleName = request.form['middle-name']
        case_address = request.form['address']
        case_dateOfBirth = convert_date(request.form['dob'])
        case_caseType = request.form['case-type']
        case_citationNumber = request.form['citation-number']
        case_caseStatus = request.form['case-status']
        case_offense = request.form['offense']
        case_offenseDate = convert_date(request.form['offense-date'])
        case_offenseType = request.form['offense-type']
        case_fileDate = fileDateGenerator(case_offenseDate)
        case_caseNumber = caseNumberGenerator(case_caseType, case_fileDate.year)
        new_case = CountySearch(
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
                                case_type=case_caseType,
                                offense=case_offense,
                                offense_date=case_offenseDate,
                                offense_type=case_offenseType
                                )

        try:
            db.session.add(new_case)
            db.session.commit()
            return redirect('/add')
        except:
            return "error"
        
    else:
        return render_template("add.html")

@app.route('/results')
def results():
    cases = CountySearch.query.order_by(CountySearch.file_date.asc()).all()
    return render_template("results.html", cases=cases)

@app.route('/delete/<int:id>')
def delete(id):
    case_to_delete = CountySearch.query.get_or_404(id)

    try:
        db.session.delete(case_to_delete)
        db.session.commit()
        return redirect('/results')
    except:
        return "error"
    
@app.route('/view/<int:id>')
def view(id):
    case_to_view = CountySearch.query.get(id)
    return render_template("record.html", case_to_view=case_to_view)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
