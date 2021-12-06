from flask import Flask, request, jsonify
from proxy import Proxy
from sensores_api import SensoresAPI

import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

sensores_api = SensoresAPI()
proxy = Proxy(sensores_api)

@app.route("/data", methods=['GET'])
def get_data_sensores():
    sensores_data = proxy.request()
    return jsonify(sensores_data)

@app.route("/update-time", methods=['POST'])
def update_time():
    logging.info('Cambia tiempo de sensores')
    content = request.json
    print(content)
    sensor_id = content['sensor_id']
    time = content['new_time']
    return jsonify(sensor_id=sensor_id, time=time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
