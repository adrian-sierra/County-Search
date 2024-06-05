from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from case_number import *

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
    date_of_birth = db.Column(db.String(8), nullable=False)
    case_type = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<County Search %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    # case_number = caseNumberGenerator("Civil")
    # print(case_number)
    if request.method == 'POST':
        case_plaintiff = request.form['plaintiff']
        case_lastName = request.form['last-name']
        case_firstName = request.form['first-name']
        case_middleName = request.form['middle-name']
        case_dateOfBirth = request.form['dob']
        case_caseType = request.form['case-type']
        case_caseNumber = caseNumberGenerator(case_caseType)

        new_case = CountySearch(plaintiff=case_plaintiff, 
                                case_number=case_caseNumber,
                                last_name=case_lastName, 
                                first_name=case_firstName, 
                                middle_name=case_middleName, 
                                date_of_birth=case_dateOfBirth, 
                                case_type=case_caseType)

        try:
            db.session.add(new_case)
            db.session.commit()
            return redirect('/')
        except:
            return "error"
        
    else:
        cases = CountySearch.query.order_by(CountySearch.last_name).all()
        return render_template('index.html', cases=cases)

@app.route('/delete/<int:id>')
def delete(id):
    case_to_delete = CountySearch.query.get_or_404(id)

    try:
        db.session.delete(case_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "error"

@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/results')
def results():
    return render_template("results.html")

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
