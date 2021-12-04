from flask import Flask, request, jsonify
from db_connection import DatabaseConection
from sensores_connection import SensoresConnection
from reporte_builder import ReporteBuilder

import json

app = Flask(__name__)

sensores_conn = SensoresConnection('http://localhost:8000/data')
db_conn = DatabaseConection()

@app.route("/reportes", methods=['GET'])
def todos_reporte():
    reportes = db_conn.get_reportes()
    return jsonify(reportes)

@app.route("/reporte", methods=['GET'])
def generar_reporte():
    builder = ReporteBuilder(db_conn=db_conn, sensores_conn=sensores_conn)
    builder.calc_gas_utilizada()
    builder.calc_contenido()
    builder.calc_consumo()
    builder.calc_poca_capacidad()
    builder.calc_no_funcionales()
    reporte = builder.reporte
    enviar_correo(reporte)
    guardar_reporte(reporte)
    return reporte.jsonify()

def enviar_correo(reporte):
    recipientes = db_conn.get_recipientes()
    for nombre, correo in recipientes.items():
        print(f'Se envio correo con reporte a {nombre} en {correo}')
        print(f'Adjunto: reporte{reporte.reporte_id}')

def guardar_reporte(reporte):
    db_conn.add_reporte(reporte)

@app.route("/destinatario/nuevo", methods=['POST'])
def anadir_destinatario():
    content = request.json
    db_conn.add_recipiente(content['nombre'], content['correo'])
    return content

@app.route("/destinatario/eliminar", methods=['DELETE'])
def eliminar_destinatario():
    content = request.json
    db_conn.remove_recipiente(content['nombre'])
    return {"msg": f"eliminio {content['nombre']}"}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
