from datetime import datetime, timedelta
from flask import Flask, jsonify
from flask_cors import CORS
import pytz


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
calibrating = False
global hora_global
global data_atual

sao_paulo_tz = pytz.timezone('America/Sao_Paulo')
data_atual = datetime.now(sao_paulo_tz).strftime("%Y-%m-%d")
hora_global = datetime.now(sao_paulo_tz).strftime("%H:%M")


@app.route('/', methods=['GET'])
def hello():
    return  hora_global


@app.route('/status_calibragem', methods=['GET'])
async def status_calibragem():
    
    global calibragem
    global hora_global
    global tipo_calibragem
    global horarios
    global calibrating
    
    data_atual = datetime.now(sao_paulo_tz).strftime("%Y-%m-%d")
    
    return jsonify({"Porcentagem": calibragem,
                    "Hora_inicio": hora_global,
                    "Tipo": tipo_calibragem,
                    "Data": data_atual,
                    "Horarios": horarios,
                    "Calibrating": calibrating})




if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0',port=5000)
