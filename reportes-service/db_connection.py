class DatabaseConection():
    def __init__(self):
        self.reportes_anteriores = [
        { 
            'reporte_id': 1,
            'gas_utlizada': [
                { 
                    'gasolinera': 'Pemex1',
                    'tanques': [
                        {
                            'tank_id': 0,
                            'utilizacion': 20,
                        },
                        {
                            'tank_id': 1,
                            'utilizacion': 30,
                        },
                        {
                            'tank_id': 2,
                            'utilizacion': 40,
                        },
                    ]
                },
                { 
                    'gasolinera': 'Pemex2',
                    'tanques': [
                        {
                            'tank_id': 3,
                            'utilizacion': 20,
                        },
                        {
                            'tank_id': 4,
                            'utilizacion': 30,
                        },
                        {
                            'tank_id': 5,
                            'utilizacion': 40,
                        },
                    ]
                }
            ],
            'contenido_en_tanques': [
                { 
                    'gasolinera': 'Pemex1',
                    'tanques': [
                        {
                            'tank_id': 1,
                            'contenido': 20,
                        },
                        {
                            'tank_id': 2,
                            'contenido': 30,
                        },
                        {
                            'tank_id': 3,
                            'contenido': 40,
                        },
                    ]
                },
                { 
                    'gasolinera': 'Pemex2',
                    'tanques': [
                        {
                            'tank_id': 4,
                            'contenido': 20,
                        },
                        {
                            'tank_id': 5,
                            'contenido': 30,
                        },
                        {
                            'tank_id': 6,
                            'contenido': 40,
                        },
                    ]
                }
            ],
            'consumo_por_tanque': [
                { 
                    'gasolinera': 'Pemex1',
                    'tanques': [
                        {
                            'tank_id': 1,
                            'consumo_por_dia': 20,
                        },
                        {
                            'tank_id': 2,
                            'consumo_por_dia': 30,
                        },
                        {
                            'tank_id': 3,
                            'consumo_por_dia': 40,
                        },
                    ]
                },
                { 
                    'gasolinera': 'Pemex2',
                    'tanques': [
                        {
                            'tank_id': 4,
                            'consumo_por_dia': 20,
                        },
                        {
                            'tank_id': 5,
                            'consumo_por_dia': 30,
                        },
                        {
                            'tank_id': 6,
                            'consumo_por_dia': 40,
                        },
                    ]
                }
            ],
            'gasolineras_poca_capacidad': ['pemex1', 'pemex2'],
            'sensores_no_funcionales': ['2', '5']
        },
        { 
            'reporte_id': 2,
            'gas_utlizada': [
                { 
                    'gasolinera': 'Pemex1',
                    'tanques': [
                        {
                            'tank_id': 0,
                            'utilizacion': 20,
                        },
                        {
                            'tank_id': 1,
                            'utilizacion': 30,
                        },
                        {
                            'tank_id': 2,
                            'utilizacion': 40,
                        },
                    ]
                },
                { 
                    'gasolinera': 'Pemex2',
                    'tanques': [
                        {
                            'tank_id': 3,
                            'utilizacion': 20,
                        },
                        {
                            'tank_id': 4,
                            'utilizacion': 30,
                        },
                        {
                            'tank_id': 5,
                            'utilizacion': 40,
                        },
                    ]
                }
            ],
            'contenido_en_tanques': [
                { 
                    'gasolinera': 'Pemex1',
                    'tanques': [
                        {
                            'tank_id': 1,
                            'contenido': 20,
                        },
                        {
                            'tank_id': 2,
                            'contenido': 30,
                        },
                        {
                            'tank_id': 3,
                            'contenido': 40,
                        },
                    ]
                },
                { 
                    'gasolinera': 'Pemex2',
                    'tanques': [
                        {
                            'tank_id': 4,
                            'contenido': 20,
                        },
                        {
                            'tank_id': 5,
                            'contenido': 30,
                        },
                        {
                            'tank_id': 6,
                            'contenido': 40,
                        },
                    ]
                }
            ],
            'consumo_por_tanque': [
                { 
                    'gasolinera': 'Pemex1',
                    'tanques': [
                        {
                            'tank_id': 1,
                            'consumo_por_dia': 20,
                        },
                        {
                            'tank_id': 2,
                            'consumo_por_dia': 30,
                        },
                        {
                            'tank_id': 3,
                            'consumo_por_dia': 40,
                        },
                    ]
                },
                { 
                    'gasolinera': 'Pemex2',
                    'tanques': [
                        {
                            'tank_id': 4,
                            'consumo_por_dia': 20,
                        },
                        {
                            'tank_id': 5,
                            'consumo_por_dia': 30,
                        },
                        {
                            'tank_id': 6,
                            'consumo_por_dia': 40,
                        },
                    ]
                }
            ],
            'gasolineras_poca_capacidad': ['pemex1', 'pemex2'],
            'sensores_no_funcionales': ['2', '5']
        }]

    def get_ultimo_reporte(self):
        return self.reportes_anteriores[-1]

    def get_contenidos_anteriores(self):
        last = self.get_ultimo_reporte()
        return last['contenido_en_tanques']
