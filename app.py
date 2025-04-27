from flask import Flask, jsonify, render_template, redirect

app = Flask(__name__)

# Estado inicial do LED
led_state = {'status': 'off'}

@app.route('/')
def index():
    return render_template('index.html', led_status=led_state['status'])

@app.route('/set_led_on')
def set_led_on():
    led_state['status'] = 'on'
    return redirect('/')

@app.route('/set_led_off')
def set_led_off():
    led_state['status'] = 'off'
    return redirect('/')

@app.route('/get_led_state')
def get_led_state():
    return jsonify(led_state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
