from flask import Flask,render_template,url_for,flash,redirect
from forms import Registrationform, loginform
app = Flask(__name__)

app.config['SECRET_KEY']='0f7c5b2ec00084158954f3c8b6ef5551'
posts = [
    {
        'tittle':'abi',
        'author':'myauthor'
    },
    {
        'tittle':'abishek',
        'author':'corey'

    }
]

@app.route("/")
@app.route("/home")




def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register():
    form =Registrationform()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register',form=form)
 
@app.route("/login")
def login():
    form=loginform()
    return render_template('login.html', title='login',form=form)
 


if __name__ == '__main__':
    app.run(debug=True)









