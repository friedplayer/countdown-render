
from flask import Flask, send_file
import countdown_generator

app = Flask(__name__)

@app.route('/countdown.png')
def serve_image():
    countdown_generator.generate_image()
    return send_file("countdown.png", mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
