from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    r = requests.get("http://192.168.1.188/wflexp.json")
    windspeed = r.json()['windavg10']
    windspeed = "  wind  " + windspeed 
    temp = r.json()['tempout']
    temp = "Temperature    " + temp 
    
    dirt = r.json()['winddir']
    dirt = "  at   " + dirt + "  degrees"
    out = temp + "\n   " + windspeed + dirt
    
    return out


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')