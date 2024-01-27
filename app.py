# app.py

from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')  # Use your actual MongoDB connection URI

# Contact form route
@app.route('/contactform', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        # Handle form submission logic here
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Create a unique database for each day with "details" in the name (format: details_yyyy_mm_dd)
        today_date = datetime.now().strftime("%Y_%m_%d")
        db = client["details" + today_date]

        # Insert a new document into the 'users' collection of the daily database
        user_data = {
            'name': name,
            'email': email,
            'message': message
        }
        db.users.insert_one(user_data)

        # Redirect to a thank-you page after form submission
        return render_template('thankyou.html')

    # Render the contact form for GET requests
    return render_template('contactform.html')



if __name__ == '__main__':
    app.run(debug=True)
