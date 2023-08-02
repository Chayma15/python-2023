from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Add a secret key for session encryption

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Save form data into session
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        session['message'] = request.form['message']
        return redirect(url_for('result'))

    return render_template('index.html')

@app.route('/result', methods=['GET'])
def result():
    # Retrieve form data from session and pass it to the template
    name = session.get('name', '')
    email = session.get('email', '')
    message = session.get('message', '')

    # Clear the session after displaying the data
    session.clear()

    return render_template('result.html', name=name, email=email, message=message)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
