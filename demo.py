from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__) # this gets the name of the file so Flask knows it's name
bcrypt = Bcrypt(app)  # creates a bcrypt object from our flask app

app.config['SECRET_KEY'] = '849f0e1d6060d989d46dd50f29f5b0b2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
      return "User({}, {})".format(self.username,self.email)
  def checkHash():
      Current = db.session.query(username(self.username))
      return Current.password

@app.route("/index")  
@app.route("/")                          # this tells you the URL the method below is related to
def hello_world():
    return "<p>Hello, World!</p>"        # this prints HTML to the webpage

  
@app.route("/home")  
def home():
    flash('Hello world')
    return render_template('home.html', subtitle='Second Page', text='This is the second page') 

  
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    try:
        if form.validate_on_submit(): # checks if entries are valid
            pw_hash = bcrypt.generate_password_hash(form.password.data).encode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password=pw_hash)
            db.session.add(user)
            db.session.commit()
            flash(f"Account created for {form.email.data}!")
            #return redirect(url_for('home')) # if so - send to home page
    except:
        flash("your account already exists")
        return render_template('register.html', title='Register', form=form)
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
      #User_Query = 
      user = checkHash()
      print(user)
     
    return render_template('login.html', title='Login', form=form)
    

    
if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")