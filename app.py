from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)

ESP32_IP = "192.168.15.92"  # IP da sua ESP32 na rede Wi-Fi

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led_on')
def led_on():
    requests.get(f"{ESP32_IP}/led/on")
    return redirect('/')

@app.route('/led_off')
def led_off():
    requests.get(f"{ESP32_IP}/led/off")
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
