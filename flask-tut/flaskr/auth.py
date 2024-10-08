import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

# bp = Blueprint
# Creates a Blueprint named 'auth'. __name__ is passed
# so that the bp knows where it is defined 

# url_prefix = prepended to all URLs 

### Register
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'

        if error is None: 
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password))
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} already exists"
            else:
                return redirect(url_for("auth.login"))
            
        flash(error)
    
    return render_template('auth/register.html')

# note: ? = a placeholder value 
### Login
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None: 
            error = 'Incorrect username or password'
        elif not check_password_hash(user['password'], password): 
            error = 'Incorrect username or password'

        if error is None: 
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)

    return render_template('auth/login.html')


### Session
# user id stored in a session, below is used to retrieve 
# think of a session cookie 
@bp.before_app_request
def load_logged_in_user(): 
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id)
        ).fetchone()


### Logout
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

### Require Authentication in Other Views
# Creating, editing and deleting blog posts requires a user
# to be logged in. A decorator can be used to check this for
# each view it is applied to. 

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs): 
        if g.user is None: 
            return redirect(url_for('auth.login'))

        return view(**kwargs)
    
    return wrapped_view






