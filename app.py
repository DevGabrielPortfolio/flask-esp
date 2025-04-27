from flask import Flask, jsonify, render_template, redirect

app = Flask(__name__)

# Estado inicial do LED e do servo
led_state = {'status': 'off'}
servo_state = {'status': 'off'}  # Novo estado para o servo

@app.route('/')
def index():
    return render_template('index.html', led_status=led_state['status'], servo_status=servo_state['status'])

@app.route('/set_led_on')
def set_led_on():
    led_state['status'] = 'on'
    servo_state['status'] = 'on'  # Quando ligar a luz, o servo vai para 0°
    return redirect('/')

@app.route('/set_led_off')
def set_led_off():
    led_state['status'] = 'off'
    servo_state['status'] = 'off'  # Quando desligar a luz, o servo vai para 180°
    return redirect('/')

@app.route('/get_led_state')
def get_led_state():
    # Retorna o estado atual do LED e do servo
    return jsonify(led_state, servo_state)

@app.route('/set_servo_on')
def set_servo_on():
    # Manda comando para o servo ir para 0° (ligar luz)
    servo_state['status'] = 'on'
    return redirect('/')

@app.route('/set_servo_off')
def set_servo_off():
    # Manda comando para o servo ir para 180° (desligar luz)
    servo_state['status'] = 'off'
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
