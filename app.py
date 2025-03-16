from flask import Flask, render_template, redirect, url_for, session, request, flash
import json
import os
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secret key for session management

# Function to load users from user_data.json
def load_users_from_json():
    if os.path.exists('user_data.json'):
        with open('user_data.json', 'r') as file:
            users = json.load(file)
    else:
        users = {}
    return users

# Function to save users to user_data.json
def save_users_to_json(users):
    with open('user_data.json', 'w') as file:
        json.dump(users, file, indent=4)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users = load_users_from_json()
        if email in users and users[email]['password'] == password:
            session['email'] = email
            flash(f"Welcome, {users[email]['first_name']}!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password.", "danger")
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        users = load_users_from_json()
        if email not in users:
            users[email] = {
                'first_name': first_name,
                'last_name': last_name,
                'password': password,
                'balance': random.randint(1000, 10000)
            }
            save_users_to_json(users)
            flash("Account created successfully!", "success")
            return redirect(url_for('login'))
        else:
            flash("Email already exists.", "danger")
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        return redirect(url_for('login'))

    email = session['email']
    users = load_users_from_json()
    if email in users:
        user = users[email]
        return render_template('dashboard.html', user=user, users=users)
    else:
        return redirect(url_for('login'))

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'email' not in session:
        return redirect(url_for('login'))

    email = session['email']
    users = load_users_from_json()
    if request.method == 'POST':
        receiver_email = request.form['receiver']
        amount = int(request.form['amount'])
        if amount <= 0:
            flash("Transfer amount must be positive.", "danger")
        elif receiver_email in users:
            if users[email]['balance'] >= amount:
                users[email]['balance'] -= amount
                users[receiver_email]['balance'] += amount
                save_users_to_json(users)
                flash("Transfer successful!", "success")
            else:
                flash("Insufficient balance.", "danger")
        else:
            flash("Receiver not found.", "danger")
        return redirect(url_for('dashboard'))
    
    return render_template('transfer.html', users=users, current_user=email)

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
