from flask import Flask,render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
app.config['SQLALCHEMY_SECRET_KEY'] = '123232'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(127), nullable=False, unique=True)
    massage = db.Column(db.text, nullable=False)
    
    def __str__(self):
        return self.subject



@app.route('/')
def index():
    return 'Hello, Flask'

@app.route('/contact',methods=['GET','POST',])
def contact():
    if request.methods == 'POST':
        contact=Contact(
            full_name =request.form.get('firstname'),
            phone=request.form.get('phone'),
            email =request.form.get('email'),
            massage =request.form.get('massage')
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template('contact.html')
if __name__ == '__main__ ':
    app.run(debug=True)