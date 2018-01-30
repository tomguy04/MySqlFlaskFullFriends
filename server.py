from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from datetime import datetime
app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriends')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friendslist")
    print friends
    return render_template('index.html', all_friends=friends)

# Insert into database starting with the root route, then the index from root sends us to this route.
@app.route('/friends', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
   
    query = "INSERT INTO friendslist (name, age, created_at, updated_at, month_day, year) VALUES (:name, :age, NOW(), NOW(), concat(monthname(NOW()),' ',day(NOW())), year(NOW()))"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'name': request.form['name'],
             'age':  request.form['age']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
