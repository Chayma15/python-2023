from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Add a secret key for session encryption

@app.route('/', methods=['GET'])
def index():
    # Check if 'counter' exists in the session, if not, initialize it
    if 'counter' not in session:
        session['counter'] = 0

    # Increment the counter by 1 each time the root route is visited
    session['counter'] += 1

    # Render the template with the counter value
    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session', methods=['GET'])
def destroy_session():
    # Clear the session and redirect to the root route
    session.clear()
    return redirect(url_for('index'))

@app.route('/increment', methods=['GET'])
def increment_counter():
    # Increment the counter by 2
    session['counter'] += 2
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
