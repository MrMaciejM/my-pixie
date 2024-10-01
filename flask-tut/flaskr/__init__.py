import os 
from flask import Flask, jsonify, render_template
import psycopg2
from datetime import datetime

# create_app is the application factory function 

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load test config if passed in
        app.config.from_mapping(test_config)
    
    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    #  user: “postgres”,
    #  host: “localhost”,
    #  database: “pixie-db”,
    #  password: “admin”

    def get_db_connection():
         conn = psycopg2.connect(host='localhost',
                                 database='pixie-db',
                                 user='postgres',
                                 password='admin'                                 
                                 )
         return conn


    # a simple page / return test data for now
    @app.route('/home')
    def fetch_data():      
           
           conn = get_db_connection()
           cur = conn.cursor()
           cur.execute('SELECT time_posted FROM posts;')
           posts = cur.fetchall()
           
           curUser = conn.cursor()
           curUser.execute('SELECT username FROM users')
           postsUser = curUser.fetchall()


           cur.close()
           curUser.close()
           
           conn.close()

           print(posts)
           print(postsUser)

           formatted_posts = [{'date_posted': post[0].isoformat() if post[0] is not None else None} for post in posts]

           formatted_users = {'username': postsUser}

           return jsonify(formatted_posts, formatted_users) 

        # return {
        #     "author": "maciej",
        #     "data": "dev"
        # }
    
    from . import db
    db.init_app(app)

    from . import auth 
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app