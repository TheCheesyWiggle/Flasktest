from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='templates', static_folder='staticFiles')

app.secret_key = "Hello fellow programmer"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
'''Database code'''
class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column("name", db.String(100))
    password = db.Column("password", db.String(100))

    def __init__(self, name, password):
        self.name = name
        self.password = password


@app.route("/welcome")
def welcome():
    '''Defines what happens at the route /welcome this allows us to welcome the user'''
    if "user" in session:
        user = session["user"]
        return render_template("welcome.html")
    else:
        return redirect(url_for('login_page'))



@app.route("/login", methods =['GET','POST'])
def login_page():
    '''Defines what happens at the route /login this allows the user to login and us to redirect them to the welcome page'''
    if request.method=='POST':
        user = request.form['username']
        pw = request.form['password']
        session["user"] = user
        usr = users(user,pw)
        if login(usr):
            if "user" in session:
                return redirect(url_for('welcome'))
    flash("Login failed", "info")            
    return render_template("login.html")
    #hash pw

def login(usr):
    try:
        usr_found = users.query.filter_by(name=usr).first()
        if usr_found.password == usr.password:
            return True
        else:
            return False
    except:
        print("Cannot find user in database.\nConsider signing up")
    # add feed back to the user if the username or pass word is incorrect


@app.route("/logout")
def logout():
    '''Defines what happens when you logout'''
    session.pop("user", None)
    return redirect(url_for("login_page"))


@app.route("/signup", methods =['GET','POST'])
def signup_page():
    '''Defines what happens at the route /sign up, this allows the user to create an account'''
    if request.method=='POST':
        
        user = request.form['username']
        pw = request.form['password']
        valid_pw = request.form['validate_password']
        session["user"] = user

        usr = users(user,pw)
        db.session.add(usr)

        if signup_sucess(valid_pw, usr):
            session["user"] = user

            if "user" in session:
                db.session.commit()
                return redirect(url_for('welcome'))
    return render_template("signup.html")
    
 
def signup_sucess(valid_pw,usr):
    '''
    Try block attempts to find a user with the same name.
    if no such user exists then it raises and error and the except block will execute.
    '''
    try:
        usr_found = users.query.filter_by(name=usr).first()
        if usr.password != valid_pw or usr_found == None:
            return False
        else:
            return True
    # add feed back to the user if username is taken
    #hash pw
    except:
        print("An exception")
        raise
        

@app.route("/view")
def view():
    '''displays database'''
    return render_template("view.html", values = users.query.all())
#needs protecting


@app.route("/")
def home():
    '''Defines what happens at the route at the defalt site, gateway to the rest of the website'''
    db.create_all()
    return render_template("index.html")

def main():
    app.run(host="0.0.0.0",port=80,debug=True)

main()