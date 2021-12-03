from flask import Flask
from flask_restful import Resource, Api
from db_connection import DatabaseConection
from sensores_connection import SensoresConnection
from reporte_builder import ReporteBuilder

app = Flask(__name__)
api = Api(app)


class ReporteAPI(Resource):
    def __init__(self):
        self.sensores_conn = SensoresConnection('http://localhost:8000/data')
        self.db_conn = DatabaseConection()

    def get(self):
        builder = ReporteBuilder(db_conn=self.db_conn, sensores_conn=self.sensores_conn)
        builder.calc_gas_utilizada()
        builder.calc_contenido()
        builder.calc_consumo()
        builder.calc_poca_capacidad()
        builder.calc_no_funcionales()
        reporte = builder.reporte.jsonify()
        # JSON reporte a json
        # Guardar el reporte nuevo en db
        # Enviar por correo
        return reporte

api.add_resource(ReporteAPI, '/reporte')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
