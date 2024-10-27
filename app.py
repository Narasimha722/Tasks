from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # your MySQL username
    password="Mass@7989",  # replace with your MySQL password
    database="user_data"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    dob = request.form['dob']
    address = request.form['address']
    email = request.form['email']
    phone_number = request.form['phone_number']
    college_name = request.form['college_name']

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO user_details (name, age, dob, address, email, phone_number, college_name) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (name, age, dob, address, email, phone_number, college_name)
    )
    db.commit()
    cursor.close()
    
    return redirect(url_for('index'))

@app.route('/view')
def view():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user_details")
    data = cursor.fetchall()
    cursor.close()
    return render_template('view.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
