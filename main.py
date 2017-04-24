import os
import query_processor
# from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)
query = query_processor.query_engine('dm_modified.json')
# app.database = 'deals.sqlite'

# def connect_db():
#     return sqlite3.connect(app.database)

@app.route('/results/<ide>')
def display(ide = 'title'):
    # g.db = connect_db()
    # command = 'SELECT * From coupons WHERE item LIKE \'%' + ide + '%\''
    query_command = query.query_parsing(ide)
    item_id_list = query.query_processing()  # rtype: list
    # cur = g.db.execute(command)
    # posts = [dict(item=row[0], img=row[1], link=row[2], description=row[3], feature=row[4]) for row in cur.fetchall()]
    posts = [dict(item=query.data[id]['item'][0], 
                  imag=query.data[id]['imag'][0], 
                  link=query.data[id]['link'],
                  description=query.data[id]['description'], 
                  feature=query.data[id]['feature']) for id in item_id_list]
    # g.db.close()
    return render_template('index.html', posts=posts)

@app.route('/search/', methods=['GET','POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        ide = request.form['name']
        return redirect(url_for('display', ide=ide))

# @app.teardown_appcontext
# def close_db(error):
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()

if __name__ == '__main__':
    app.run()
