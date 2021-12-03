import json

class Reporte():
    def __init__(self):
        self.gas_utilizada = []
        self.contenido_en_tanques = []
        self.consumo_por_tanque = []
        self.gasolineras_poca_capacidad = []
        self.sensores_no_funcionales = []

    def jsonify(self):
        return json.loads(json.dumps(self.__dict__))
