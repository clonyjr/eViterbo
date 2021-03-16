print("===== DATAFRAME COORDENADAS FINAL ======")
        print(dfInstituicao.values)
        dfWikibaseItems = pd.DataFrame(instituicao,columns=['nome'
            ,'urleviterbo'
            ,'outras_denominações'
            ,'sigla'
            ,'local_inst'
            ,'tipo_inst'
            ,'antecessora'
            ,'sucessora'
            ,'data_fundação'
            ,'data_extinção'
            ,'paralisação_início'
            ,'paralisação_fim'
            ,'item_id'])

        print(dfWikibaseItems)
        dfWikibaseItems.to_csv(datasetpath+'instituicao_wikibase_item_Teste.csv', index = True, header=True)


for index_to_check in range(len(column_name)):
                if(dataframe_to_check.iloc[index_to_check][column_name[7]]!=0):
                    localizacao = {
                    'localização1':dataframe_to_check.iloc[index_to_check][column_name[7]]
                    ,'localização2':dataframe_to_check.iloc[index_to_check][column_name[10]]
                    ,'localização3':dataframe_to_check.iloc[index_to_check][column_name[13]]
                    ,'localização4':dataframe_to_check.iloc[index_to_check][column_name[16]]
                    ,'localização5':dataframe_to_check.iloc[index_to_check][column_name[19]]
                    ,'localização6':dataframe_to_check.iloc[index_to_check][column_name[22]]
                    ,'localização7':dataframe_to_check.iloc[index_to_check][column_name[25]]
                    ,'localização8':dataframe_to_check.iloc[index_to_check][column_name[28]]
                    }
            return localizacao
            
            data=[wdi_core.WDUrl(prop_nr='P30',value=url_coord)
                            ,wdi_core.WDGlobeCoordinate(prop_nr='P29', latitude=lat,longitude=long,precision=0.0001)
                            ,wdi_core.WDString(prop_nr='P46', value=dataframe_to_check.iloc[index_to_check][column_name[7])
                            ,wdi_core.WDString(prop_nr='P35', value=dataframe_to_check.iloc[index_to_check][column_name[7])]]
                        wd_item = wdi_core.WDItemEngine(data=data) # create new item
                        wd_item.set_label(label=dfCoordenadas['_pageName'][i],lang='pt')
                        item_id = wd_item.entity_metadata.get('id') #retrieve item id
                        wd_item.write(self.login_instance)