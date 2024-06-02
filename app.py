import os

from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
users_file = 'users.txt'

# Helper function to read users from file
def read_users():
    users = {}
    if os.path.exists(users_file):
        with open(users_file, 'r') as f:
            for line in f:
                username, password_hash = line.strip().split(',')
                users[username] = password_hash
    return users

# Helper function to write users to file
def write_user(username, password_hash):
    with open(users_file, 'a') as f:
        f.write(f"{username},{password_hash}\n")

# Route for the home page
@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('home.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = read_users()
        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

# Route for the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = read_users()
        if username in users:
            flash('Username already exists', 'danger')
        else:
            password_hash = generate_password_hash(password, method='pbkdf2:sha256')
            write_user(username, password_hash)
            flash('Signup successful! Please login.', 'success')
            return redirect(url_for('login'))
    return render_template('signup.html')

# Route for the dashboard page
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

# Routes for the actions
@app.route('/action1')
def action1():
    if 'username' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    # Add logic for action1 here
    flash('Action 1 executed', 'success')
    return redirect(url_for('dashboard'))

@app.route('/action2')
def action2():
    if 'username' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    # Add logic for action2 here
    flash('Action 2 executed', 'success')
    return redirect(url_for('dashboard'))

@app.route('/action3')
def action3():
    if 'username' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    # Add logic for action3 here
    flash('Action 3 executed', 'success')
    return redirect(url_for('dashboard'))

@app.route('/action4')
def action4():
    if 'username' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    # Add logic for action4 here
    flash('Action 4 executed', 'success')
    return redirect(url_for('dashboard'))

@app.route('/action5')
def action5():
    if 'username' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    # Add logic for action5 here
    flash('Action 5 executed', 'success')
    return redirect(url_for('dashboard'))

# Route for the search functionality
@app.route('/search')
def search():
    if 'username' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    query = request.args.get('query')
    # Add logic for handling search query here
    flash(f'Search results for: {query}', 'success')
    return redirect(url_for('dashboard'))

# Route for the profile page
@app.route('/profile')
def profile():
    if 'username' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    return render_template('profile.html', username=session['username'])

# Route for logging out
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
