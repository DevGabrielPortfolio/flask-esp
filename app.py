from flask import Flask, render_template, redirect, Response
import requests

app = Flask(__name__)

# IP atual da ESP32
ESP32_IP = "http://192.168.15.92"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led_on')
def led_on():
    try:
        response = requests.get(f"{ESP32_IP}/led/on", timeout=2)
        response.raise_for_status()
        return redirect('/')
    except requests.exceptions.RequestException as e:
        print(f"Erro ao tentar ligar o LED: {e}")
        return Response(f"Erro: {e}", status=500)

@app.route('/led_off')
def led_off():
    try:
        response = requests.get(f"{ESP32_IP}/led/off", timeout=2)
        response.raise_for_status()
        return redirect('/')
    except requests.exceptions.RequestException as e:
        print(f"Erro ao tentar desligar o LED: {e}")
        return Response(f"Erro: {e}", status=500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
