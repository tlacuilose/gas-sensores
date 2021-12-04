from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/data", methods=['GET'])
def get_data_sensores():
    # Proxy y agrupar info de sensores
    sensores = [
    { 
        'gasolinera': 'Pemex1',
        'tanques': [
            {
                'tank_id': 1,
                'contenido': 20,
                'capacidad': 100,
                'consumo_por_dia': 3,
                'funcional': 1
            },
            {
                'tank_id': 2,
                'contenido': 30,
                'capacidad': 100,
                'consumo_por_dia': 3,
                'funcional': 0
            },
            {
                'tank_id': 3,
                'contenido': 40,
                'capacidad': 100,
                'consumo_por_dia': 3,
                'funcional': 1
            },
        ]
    },
    { 
        'gasolinera': 'Pemex2',
        'tanques': [
            {
                'tank_id': 4,
                'contenido': 20,
                'capacidad': 100,
                'consumo_por_dia': 3,
                'funcional': 1
            },
            {
                'tank_id': 5,
                'contenido': 30,
                'capacidad': 100,
                'consumo_por_dia': 3,
                'funcional': 0
            },
            {
                'tank_id': 6,
                'contenido': 40,
                'capacidad': 100,
                'consumo_por_dia': 3,
                'funcional': 1
            },
        ]
    }]
    return jsonify(sensores)

@app.route("/update-time", methods=['POST'])
def update_time():
    # Proxy cambia tiempo de sensores
    content = request.json
    print(content)
    sensor_id = content['sensor_id']
    time = content['new_time']
    return jsonify(sensor_id=sensor_id, time=time)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
