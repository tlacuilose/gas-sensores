class SensoresAPI():
    def __init__(self):
        self.sensores = [
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

    def request(self):
        print('Request api sensores')
        return self.sensores
