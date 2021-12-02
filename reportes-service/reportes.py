from flask import Flask
from flask_restful import Resource, Api
import requests
import json

app = Flask(__name__)
api = Api(app)

class Reporte():
    def get_sensores(self):
        r = requests.get("http://localhost:8000/data")
        return r.json()

    def db_info(self):
        return { 'tanques': [
                {
                    'tank_id': 0,
                    'contenido': 40,
                },
                {
                    'tank_id': 1,
                    'contenido': 30,
                },
                {
                    'tank_id': 2,
                    'contenido': 20,
                },
            ]
        }

    def get_utilizacion(self, sensores, db):
        tanques_sensores = sensores['tanques']
        tanques_db = db['tanques']
        res = []
        for sensor, from_db in zip(tanques_sensores, tanques_db):
            util = {
                    'tank_id': sensor['tank_id'],
                    'utilizacion': sensor['contenido'] - from_db['contenido']
            }
            res.append(util)
        return { 'tanques' : res }


    def generar(self):
        sensores_info = self.get_sensores()
        db_info = self.db_info()
        gas_utlizada = self.get_utilizacion(sensores_info, db_info)
        print(gas_utlizada)
        # contenido_actual = self.get_actual(sensores_info)
        # por_dia = self.por_dia(sensores_info, db_info)
        # recibir info en db
        # hacer la comparacion
        # obtener gasolina utilizada
        # obtener contenido actual
        # obtener consumo pordia
        print(sensores_info)
        return sensores_info['tanques']


class ReporteAPI(Resource):
    def get(self):
        reporte = Reporte()
        r = reporte.generar()
        # Vistar /data, para info de sensores
        # Generar reporte
        # enviar por correo
        # guardar en base de datso
        return {'hello': r}
        


api.add_resource(ReporteAPI, '/reporte')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
