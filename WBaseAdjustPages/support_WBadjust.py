'''=== POPULATE RELIGION PROPERTIES ENTITY ==='''
        relig_entity_values = {}
        relig_props = {}
        for row in ws.iter_cols(min_col=1,
                                max_col=1,
                                min_row=3,
                                max_row=9,
                                values_only=True):
            relig_prop_id = 'P27'
            relig_entity_values = {row}
        relig_props[relig_prop_id]=relig_entity_values
        list = relig_props['P27']
        i =0
        #while i < 7:
         #   for value in list:
                #print(value[i])
                #wd_item = wdi_core.WDItemEngine()
                #wd_item.set_label(value[i], lang="pt")
                #wd_item.write(self.login_instance)
         #   i +=1
        '''=== POPULATE FORMAÇÃO PROPERTIES ENTITY ==='''
    def create_formacao(self):
        formacao_entity_values = {}
        formacao_props = {}
        formacao_properties = {'P30':''}
        for row in ws.iter_cols(min_col=2,
                                max_col=2,
                                min_row=3,
                                max_row=13,
                                values_only=True):
            formacao_prop_id = 'P48'
            formacao_entity_values = {
                'P47':row
            }
        formacao_props[formacao_prop_id]=formacao_entity_values
        print(formacao_props)
        print(formacao_entity_values)
        for key in formacao_entity_values.keys():
            prop_id = key
        itemid = ['Q70','Q71','Q72','Q73','Q74','Q75','Q76','Q77','Q78','Q79','Q80']
        list = formacao_entity_values['P47']
        for i in range(len(list)):
            print(list[i])
            data=[wdi_core.WDUrl(prop_nr='P30', value=None, snak_type='somevalue')]
            wd_item = wdi_core.WDItemEngine(wd_item_id=itemid[i],data=data)
            #wd_item.set_label(value[i], lang="pt")
            #wd_item = wdi_core.WDItemEngine(data=data)
            #wd_item.set_label(list[i], lang="pt")
            wd_item.write(self.login_instance)
            
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
        tipo_inst_props[tipo_inst_prop_id]=tipo_inst_entity_values
        #print(tipo_inst_props)
        list = tipo_inst_props[tipo_inst_prop_id]
        itemid = ['Q52','Q53','Q54','Q55','Q56','Q57','Q58','Q59','Q60','Q61']
        i =0
        while i < 10:
            for value in list:
                #wd_item = wdi_core.WDItemEngine(wd_item_id=itemid[i])
                #wd_item.set_label(value[i], lang="pt")
                #wd_item.write(self.login_instance)
                #data=[wdi_core.WDString(prop_nr=tipo_inst_prop_id, value=value[i])]
                #self.create_new_wikibase_item(data)
                print(value[i])
            i +=1
        #data=[wdi_core.WDString(prop_nr=tipo_inst_prop_id, value=value[i])]
        #self.create_new_wikibase_item(data)
        
        http://ieeta-eviterbo.web.ua.pt/index.php/Albuquerque,_Badajoz,_Espanha
        http://ieeta-eviterbo.web.ua.pt/index.php/Fortaleza,_Ceará,_Brasil
        http://ieeta-eviterbo.web.ua.pt/index.php/Largo_das_Carvalheiras,_Braga,-            