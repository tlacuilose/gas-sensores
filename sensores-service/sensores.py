from flask import Flask, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class SensoresData(Resource):
    def get(self):
        # Proxy y agrupar info de sensores
        return [
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

class SensoresConfig(Resource):
    def post(self):
        # Proxy cambia tiempo de sensores
        json_data = request.get_json(force=True)
        sensor_id = json_data['sensor_id']
        time = json_data['new_time']
        return jsonify(sensor_id=sensor_id, time=time)

api.add_resource(SensoresData, '/data')
api.add_resource(SensoresConfig, '/update-time')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
