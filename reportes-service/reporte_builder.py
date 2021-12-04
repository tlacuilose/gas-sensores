from reporte_model import Reporte

class ReporteBuilder():

    def __init__(self, db_conn, sensores_conn):
        self.reporte_ids = 2
        self.reset()
        self.db_conn = db_conn
        self.sensores_conn = sensores_conn

    def reset(self):
        self.reporte_ids += 1
        self._reporte = Reporte(self.reporte_ids)

    @property
    def reporte(self):
        reporte = self._reporte
        self.reset()
        return reporte

    def calc_gas_utilizada(self):
        contenido_sensores = self.sensores_conn.get_info()
        contenido_anterior = self.db_conn.get_contenidos_anteriores()
        utilizacion = []
        for gas_sensor, gas_anterior in zip(contenido_sensores,contenido_anterior):
            util = dict()
            util['gasolinera'] = gas_sensor['gasolinera']
            tanques = []
            _id = 1
            for tanque_sensor, tanque_anterior in zip(gas_sensor['tanques'], gas_anterior['tanques']):
                tanque = dict()
                tanque['tank_id'] = _id
                tanque['utilizacion'] = tanque_sensor['contenido'] - tanque_anterior['contenido']
                tanques.append(tanque)
                _id += 1

            util['tanques'] = tanques
            utilizacion.append(util)
        self._reporte.gas_utilizada = utilizacion

    def calc_contenido(self):
        contenido_sensores = self.sensores_conn.get_info()
        contenido = []
        for gas_sensor in contenido_sensores:
            cont = dict()
            cont['gasolinera'] = gas_sensor['gasolinera']
            tanques = []
            _id = 1
            for tanque_sensor in gas_sensor['tanques']:
                tanque = dict()
                tanque['tank_id'] = _id
                tanque['contenido'] = tanque_sensor['contenido']
                tanques.append(tanque)
                _id += 1

            cont['tanques'] = tanques
            contenido.append(cont)
        self._reporte.contenido_en_tanques = contenido

    def calc_consumo(self):
        contenido_sensores = self.sensores_conn.get_info()
        contenido = []
        for gas_sensor in contenido_sensores:
            cont = dict()
            cont['gasolinera'] = gas_sensor['gasolinera']
            tanques = []
            _id = 1
            for tanque_sensor in gas_sensor['tanques']:
                tanque = dict()
                tanque['tank_id'] = _id
                tanque['consumo_por_dia'] = tanque_sensor['consumo_por_dia']
                tanques.append(tanque)
                _id += 1

            cont['tanques'] = tanques
            contenido.append(cont)
        self._reporte.consumo_por_tanque = contenido


    def calc_poca_capacidad(self):
        contenido_sensores = self.sensores_conn.get_info()
        contenido = []
        for gas_sensor in contenido_sensores:
            poca = False
            for tanque_sensor in gas_sensor['tanques']:
                if tanque_sensor['contenido'] / tanque_sensor['capacidad'] >= 1/5:
                    poca = True
                    break
            if poca:
                contenido.append(gas_sensor['gasolinera'])
        self._reporte.gasolineras_poca_capacidad = contenido

    def calc_no_funcionales(self):
        contenido_sensores = self.sensores_conn.get_info()
        contenido = []
        for gas_sensor in contenido_sensores:
            for tanque in gas_sensor['tanques']:
                if tanque['funcional'] == 0:
                    contenido.append(tanque['tank_id'])
        self._reporte.sensores_no_funcionales = contenido

