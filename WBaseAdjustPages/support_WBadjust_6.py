items_to_create = {'Religião':['P27':'Católica','Judaica','Islâmica','Budista','Hindu','Anglicana','Protestante','Cristã Ortodoxa'],'Formação':}

'''=== POPULATE POSTO PROPERTIES ENTITY ==='''
        posto_entity_values = {}
        posto_props = {}
        for row in ws.iter_cols(min_col=3,
                                max_col=3,
                                min_row=2,
                                max_row=15,
                                values_only=True):
            posto_prop_id = 'P50'
            posto_entity_values = {
                'P55':'',
                'P13': row,
                'P14': row}
        posto_props[posto_prop_id]=posto_entity_values
        print(posto_props)


        
'''=== POPULATE ARMAS PROPERTIES ENTITY ==='''
            armas_entity_values = {}
            armas_props = {}
            for row in ws.iter_cols(min_col=4,
                                    max_col=4,
                                    min_row=2,
                                    max_row=6,
                                    values_only=True):
                armas_prop_id = 'P52'
                armas_entity_values = {
                    'P55':'',
                    'P13': row,
                    'P14': row,
                    'P53': row
                }
            armas_props[armas_prop_id]=armas_entity_values
            print(armas_props)

'''=== POPULATE CARGO PROPERTIES ENTITY ==='''
        cargo_entity_values = {}
        cargo_props = {}
        for row in ws.iter_cols(min_col=5,
                                max_col=5,
                                min_row=2,
                                max_row=24,
                                values_only=True):
            cargo_prop_id = 'P8'
            cargo_entity_values = {
                'P9': '',
                'P10': '',
                'P13': row
                }
        cargo_props[cargo_prop_id]=cargo_entity_values
        print(cargo_props)        

'''=== POPULATE ACTIVIDADE PROPERTIES ENTITY ==='''
        actividade_entity_values = {}
        actividade_props = {}
        for row in ws.iter_cols(min_col=6,
                                max_col=6,
                                min_row=2,
                                max_row=21,
                                values_only=True):
            actividade_prop_id = 'P56'
            actividade_entity_values = {
                'P30':'',
                'P13': row,
                'P14': row
                }
        actividade_props[cargo_prop_id]=actividade_entity_values
        print(actividade_props)

'''=== POPULATE TIPOS DE INSTITUIÇÃO PROPERTIES ENTITY ==='''
        tipo_inst_entity_values = {}
        tipo_inst_props = {}
        for row in ws.iter_cols(min_col=7,
                                max_col=7,
                                min_row=2,
                                max_row=11,
                                values_only=True):
            tipo_inst_prop_id = 'P36'
            tipo_inst_entity_values = {row}
        tipo_inst_props[armas_prop_id]=tipo_inst_entity_values
        print(tipo_inst_props)
        
        
        
        list = relig_props['P27']
        i =0
        print(len(list))
        while i < len(list):
            for value in list:
                print(value[i])
            i +=1