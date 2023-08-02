from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play', methods=['GET'])
def play_default():
    return render_template('index.html', num_boxes=3, color='blue')

@app.route('/play/<int:x>', methods=['GET'])
def play_x_times(x):
    return render_template('index.html', num_boxes=x, color='blue')

@app.route('/play/<int:x>/<color>', methods=['GET'])
def play_x_times_color(x, color):
    return render_template('index.html', num_boxes=x, color=color)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
