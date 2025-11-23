from flask import Flask, render_template, request, redirect, url_for, session
import time
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' # MUST be secured in production!

# --- Simulated Database ---
USERS = {'user': 'password'} # Simple user/pass for demo
QSE_RATES = {
    'QNBQ': {'name': 'QNB Group', 'rate': 18.50, 'change': 0.05, 'color': 'success'},
    'QIBK': {'name': 'Qatar Islamic Bank', 'rate': 21.30, 'change': -0.15, 'color': 'danger'},
    'DHBK': {'name': 'Doha Bank', 'rate': 3.10, 'change': 0.00, 'color': 'warning'},
    'MARK': {'name': 'Al-Maha Group', 'rate': 9.85, 'change': 0.35, 'color': 'success'},
}

# --- Routes ---

@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # Pass simulated data and colors to the professional template
    return render_template('dashboard.html', rates=QSE_RATES, current_time=time.strftime("%H:%M:%S"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if USERS.get(username) == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid credentials.')
    return render_template('login.html', error=None)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Running directly will expose port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
