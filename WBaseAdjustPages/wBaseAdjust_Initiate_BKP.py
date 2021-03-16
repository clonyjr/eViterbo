dfWikibaseItems = pd.DataFrame
        property_with_no_value = '''None, snak_type='somevalue'''
        religioes = {'Católica': 'Q8'
                     ,'Cristã Ortodoxa': 'Q69'
                     ,'Protestante': 'Q68'
                     ,'Anglicana': 'Q67'
                     ,'Hindu': 'Q66'
                     ,'Budista': 'Q65'
                     ,'Islmâmica': 'Q64'
                     ,'Judaica': 'Q63'}

        columns_Pessoas = ['_pageName','nome_completo','nome_outras_grafias','pai','mãe','cônjuge','filhos','irmãos'
            ,'data_nascimento','local_nascimento','data_morte','local_morte','residência1','data_inicio_residência1'
            ,'data_fim_residência1','residência2','data_inicio_residência2','data_fim_residência2','residência3'
            ,'data_inicio_residência3','data_fim_residência3','residência4','data_inicio_residência4'
            ,'data_fim_residência4','residência5','data_inicio_residência5','data_fim_residência5','residência6'
            ,'data_inicio_residência6','data_fim_residência6','residência7','data_inicio_residência7'
            ,'data_fim_residência7','residência8','data_inicio_residência8','data_fim_residência8','residência9'
            ,'data_inicio_residência9','data_fim_residência9','religião','sexo','local_enterramento'
            ,'Formação_1','Instituição_de_Formação_1','data_inicio_formação_1','data_fim_formação_1','Formação_2'
            ,'Instituição_de_Formação_2','data_inicio_formação_2','data_fim_formação_2','Formação_3'
            ,'Instituição_de_Formação_3','data_inicio_formação_3','data_fim_formação_3','Posto_1','Arma_1'
            ,'data_posto_1','data_fim_posto_1','Posto_2','Arma_2','data_posto_2','data_fim_posto_2','Posto_3','Arma_3'
            ,'data_posto_3','data_fim_posto_3','Posto_4','Arma_4','data_posto_4','data_fim_posto_4','Posto_5','Arma_5'
            ,'data_posto_5','data_fim_posto_5','Posto_6','Arma_6','data_posto_6','data_fim_posto_6','Posto_7','Arma_7'
            ,'data_posto_7','data_fim_posto_7','Posto_8','Arma_8','data_posto_8','data_fim_posto_8','Cargo_1'
            ,'Instituição_Cargo_1','data_inicio_cargo_1','data_fim_cargo_1','Cargo_2','Instituição_Cargo_2'
            ,'data_inicio_cargo_2','data_fim_cargo_2','Cargo_3','Instituição_Cargo_3','data_inicio_cargo_3'
            ,'data_fim_cargo_3','Cargo_4','Instituição_Cargo_4','data_inicio_cargo_4','data_fim_cargo_4','Cargo_5'
            ,'Instituição_Cargo_5','data_inicio_cargo_5','data_fim_cargo_5','Cargo_6','Instituição_Cargo_6'
            ,'data_inicio_cargo_6','data_fim_cargo_6','Cargo_7','Instituição_Cargo_7','data_inicio_cargo_7'
            ,'data_fim_cargo_7','Cargo_8','Instituição_Cargo_8','data_inicio_cargo_8','data_fim_cargo_8','Cargo_9'
            ,'Instituição_Cargo_9','data_inicio_cargo_9','data_fim_cargo_9','Actividade_1','data_inicio_actividade_1'
            ,'data_fim_actividade_1','Local_de_Actividade_1','Actividade_2','data_inicio_actividade_2'
            ,'data_fim_actividade_2','Local_de_Actividade_2','Actividade_3','data_inicio_actividade_3'
            ,'data_fim_actividade_3','Local_de_Actividade_3','Actividade_4','data_inicio_actividade_4'
            ,'data_fim_actividade_4','Local_de_Actividade_4','Actividade_5','data_inicio_actividade_5'
            ,'data_fim_actividade_5','Local_de_Actividade_5','Actividade_6','data_inicio_actividade_6'
            ,'data_fim_actividade_6','Local_de_Actividade_6','Actividade_7','data_inicio_actividade_7'
            ,'data_fim_actividade_7','Local_de_Actividade_7','Actividade_8','data_inicio_actividade_8'
            ,'data_fim_actividade_8','Local_de_Actividade_8','Actividade_9','data_inicio_actividade_9'
            ,'data_fim_actividade_9','Local_de_Actividade_9']

        r_file = open(datasetpath+pessoa_file, 'rb').read()
        result = chardet.detect(r_file)
        file_encoding = result['encoding']
        df_pessoas = pd.read_csv(datasetpath+pessoa_file
                                    ,encoding=file_encoding
                                    ,header=0
                                    ,usecols=columns_Pessoas)
        df_pessoas = df_pessoas.reindex(columns=df_pessoas.columns.tolist())
        df_pessoas_nomes = df_pessoas['_pageName'].replace(' ', '_', regex=True)
        df_pessoas = df_pessoas.replace(['\[','\]'], ['',''], regex=True)
        df_pessoas = df_pessoas.fillna(0)

        column_formacao = ['Formação_1','Formação_2','Formação_3']
        column_residencia = ['residência1','residência2','residência3','residência4',
                             'residência5','residência6','residência7','residência8','residência9']
        column_cargo =  ['Cargo_1','Cargo_2','Cargo_3','Cargo_4','Cargo_5','Cargo_6','Cargo_7','Cargo_8','Cargo_9']
        column_inst_cargo = ['Instituição_Cargo_1','Instituição_Cargo_2','Instituição_Cargo_3','Instituição_Cargo_4',
                             'Instituição_Cargo_5','Instituição_Cargo_6','Instituição_Cargo_7','Instituição_Cargo_8',
                             'Instituição_Cargo_9']
        column_posto =  ['Posto_1','Posto_2','Posto_3','Posto_4','Posto_5','Posto_6','Posto_7','Posto_8']
        column_arma =  ['Arma_1','Arma_2','Arma_3','Arma_4','Arma_5','Arma_6','Arma_7','Arma_8']
        column_actividade =  ['Actividade_1','Actividade_2','Actividade_3','Actividade_4','Actividade_5','Actividade_6',
                              'Actividade_7','Actividade_8','Actividade_9']
        column_loc_actividade =  ['Local_de_Actividade_1','Local_de_Actividade_2','Local_de_Actividade_3',
                                  'Local_de_Actividade_4','Local_de_Actividade_5','Local_de_Actividade_6',
                                  'Local_de_Actividade_7','Local_de_Actividade_8','Local_de_Actividade_9']

        formacao_id = ['Q29','Q70','Q71','Q72','Q73','Q74','Q75','Q76','Q77','Q78','Q79','Q80']
        datas_qualifiers={'residência':['data_inicio_residência','data_fim_residência'],
                          'formação':['data_inicio_formação_','data_fim_formação_'],
                          'posto':['data_posto_','data_fim_posto_'],
                          'cargo':['data_inicio_cargo_','data_fim_cargo_'],
                          'actividade':['data_inicio_actividade_','data_fim_actividade_']}
        #datas_qualifiers['residência'][1]+'1' devolve data_fim_residência1
        instituicoes_qualifiers= {'formação':'Instituição_de_Formação_',
                                   'cargo':'Instituição_Cargo_'
                                   }
        locais_qualifiers= {'actividade':'Local_de_Actividade_'}

        print(df_pessoas_nomes.head(10))
        for i in range(len(df_pessoas)):
            nome_outras_grafias = self.get_Properties_Values(df_pessoas['nome_outras_grafias'][i])
            local_nascimento = self.get_Wikibase_Qid(df_pessoas['local_nascimento'][i])
            local_morte = self.get_Wikibase_Qid(df_pessoas['local_morte'][i])
            local_enterramento = self.get_Wikibase_Qid(df_pessoas['local_enterramento'][i])
            if df_pessoas['religião'][i] not in religioes.keys():
                religiao_values = object_without_properties
            else: religiao_values = {'value': religioes[df_pessoas['religião'][i]], 'snak_type':'value'}
            nome_completo = object_without_properties
            if df_pessoas['nome_completo'][i] != 0:
                nome_completo = {'value': df_pessoas['nome_completo'][i],'snak_type':'value' }
            residencias = []
            qualifiers_residencia = []
            qualifiers_formacao = []
            qualifiers_cargo = []
            qualifiers_posto = []
            qualifiers_actividade = []
            for idx_res in range(len(column_residencia)):
                idx_dt_ini = idx_res + 1
                residencias.append(self.get_Wikibase_Qid(df_pessoas[column_residencia[idx_res]][i]))
                resid_data_ini = self.adjust_Time_Value(df_pessoas[datas_qualifiers['residência'][0]+ str(idx_dt_ini)][i])
                resid_data_fim = self.adjust_Time_Value(df_pessoas[datas_qualifiers['residência'][1]+ str(idx_dt_ini)][i])
                if resid_data_ini != '0':
                    qualifiers_residencia.append(wdi_core.WDTime(prop_nr='P9',
                                                      time=self.parse_To_Wikibase_Time(resid_data_ini),
                                                                 is_qualifier=True))
                else: qualifiers_residencia.append(wdi_core.WDTime(prop_nr='P9',
                                                                   time=None, snak_type='somevalue',is_qualifier=True))
                if resid_data_fim != '0':
                    qualifiers_residencia.append(wdi_core.WDTime(prop_nr='P10',
                                                      time=self.parse_To_Wikibase_Time(resid_data_fim),
                                                                 is_qualifier=True))
                else: qualifiers_residencia.append(wdi_core.WDTime(prop_nr='P10',
                                                                   time=None, snak_type='somevalue',is_qualifier=True))
            instituicoes_de_formacoes = [self.get_Wikibase_Qid(df_pessoas['Instituição_de_Formação_1'][i])
                ,self.get_Wikibase_Qid(df_pessoas['Instituição_de_Formação_2'][i])
                ,self.get_Wikibase_Qid(df_pessoas['Instituição_de_Formação_3'][i])
                                         ]
            formacoes = []
            for idx_f in range(len(column_formacao)):
                idx_formacao = idx_f + 1
                formacoes.append(self.get_Wikibase_Qid(df_pessoas[column_formacao[idx_f]][i]))
                formacao_dt_ini = self.adjust_Time_Value(df_pessoas[datas_qualifiers['formação'][0] + str(idx_formacao)][i])
                formacao_dt_fim = self.adjust_Time_Value(df_pessoas[datas_qualifiers['formação'][1] + str(idx_formacao)][i])
                if formacao_dt_ini != '0':
                    qualifiers_formacao.append(wdi_core.WDTime(prop_nr='P9',
                                                               time=self.parse_To_Wikibase_Time(formacao_dt_ini),
                                                               is_qualifier=True))
                else: qualifiers_formacao.append(wdi_core.WDTime(prop_nr='P9',time=None, snak_type='somevalue',is_qualifier=True))
                if formacao_dt_fim != '0':
                    qualifiers_formacao.append(wdi_core.WDTime(prop_nr='P10',
                                                               time=self.parse_To_Wikibase_Time(formacao_dt_fim),
                                                               is_qualifier=True))
                else: qualifiers_formacao.append(wdi_core.WDTime(prop_nr='P10',time=None, snak_type='somevalue',is_qualifier=True))

            for idx_inst_for in range(len(instituicoes_de_formacoes)):
                qualifiers_formacao.append(wdi_core.WDItemID(prop_nr='P28', value=instituicoes_de_formacoes[idx_inst_for]['value'],
                                                             snak_type=instituicoes_de_formacoes[idx_inst_for]['snak_type'],
                                                             is_qualifier=True))
                qualifiers_formacao.append(wdi_core.WDItemID(prop_nr='P12', value=instituicoes_de_formacoes[idx_inst_for]['value'],
                                                             snak_type=instituicoes_de_formacoes[idx_inst_for]['snak_type'],
                                                             is_qualifier=True))
            postos = []
            armas = []
            for idx_p in range(len(column_posto)):
                idx_posto = idx_p + 1
                print("appending " + str(column_posto[idx_p]) + " : " + str(df_pessoas[column_posto[idx_p]][i]) + " of position " + str(i))
                postos.append(self.get_Wikibase_Qid(df_pessoas[column_posto[idx_p]][i]))
                posto_dt_ini = self.adjust_Time_Value(df_pessoas[datas_qualifiers['posto'][0]+ str(idx_posto)][i])
                posto_dt_fim = self.adjust_Time_Value(df_pessoas[datas_qualifiers['posto'][1]+ str(idx_posto)][i])
                if posto_dt_ini != '0':
                    qualifiers_posto.append(wdi_core.WDTime(prop_nr='P9',
                                                            time=self.parse_To_Wikibase_Time(posto_dt_ini),
                                                            is_qualifier=True))
                else:qualifiers_posto.append(wdi_core.WDTime(prop_nr='P9',time=None,snak_type='somevalue',is_qualifier=True))
                if posto_dt_fim != '0':
                    qualifiers_posto.append(wdi_core.WDTime(prop_nr='P10',
                                                            time=self.parse_To_Wikibase_Time(posto_dt_fim),
                                                            is_qualifier=True))
                else:qualifiers_posto.append(wdi_core.WDTime(prop_nr='P10',time=None,snak_type='somevalue',is_qualifier=True))
                armas.append(self.get_Wikibase_Qid(df_pessoas[column_arma[idx_p]][i]))
                qualifiers_posto.append(wdi_core.WDItemID(prop_nr='P52', value=armas[idx_p]['value'],
                                                          snak_type=armas[idx_p]['snak_type'],
                                                          is_qualifier=True))
            cargos = []
            instituicoes_cargos = []
            for idx_c in range(len(column_cargo)):
                idx_cargo = idx_c + 1
                cargos.append(self.get_Wikibase_Qid(df_pessoas[column_cargo[idx_c]][i]))
                cargo_dt_ini = self.adjust_Time_Value(df_pessoas[datas_qualifiers['cargo'][0]+ str(idx_cargo)][i])
                cargo_dt_fim = self.adjust_Time_Value(df_pessoas[datas_qualifiers['cargo'][1]+ str(idx_cargo)][i])
                if cargo_dt_ini != '0':
                    qualifiers_cargo.append(wdi_core.WDTime(prop_nr='P9',
                                                            time=self.parse_To_Wikibase_Time(cargo_dt_ini),
                                                            is_qualifier=True))
                else: qualifiers_cargo.append(wdi_core.WDTime(prop_nr='P9',time=None, snak_type='somevalue',is_qualifier=True))
                if cargo_dt_fim != '0':
                    qualifiers_cargo.append(wdi_core.WDTime(prop_nr='P10',
                                                            time=self.parse_To_Wikibase_Time(cargo_dt_fim),
                                                            is_qualifier=True))
                else:qualifiers_cargo.append(wdi_core.WDTime(prop_nr='P10',time=None, snak_type='somevalue',is_qualifier=True))
                instituicoes_cargos.append(self.get_Wikibase_Qid(df_pessoas[column_inst_cargo[idx_c]][i]))
                qualifiers_cargo.append(wdi_core.WDItemID(prop_nr='P12', value=instituicoes_cargos[idx_c]['value'],
                                                          snak_type=instituicoes_cargos[idx_c]['snak_type'],
                                                          is_qualifier=True))
            actividades = []
            for idx_ac in range(len(column_actividade)):
                idx_actividade = idx_ac + 1
                actividades.append(self.get_Wikibase_Qid(df_pessoas[column_actividade[idx_ac]][i]))
                actividade_dt_ini = self.adjust_Time_Value(df_pessoas[datas_qualifiers['actividade'][0]+ str(idx_actividade)][i])
                actividade_dt_fim = self.adjust_Time_Value(df_pessoas[datas_qualifiers['actividade'][1]+ str(idx_actividade)][i])
                if actividade_dt_ini != '0':
                    qualifiers_actividade.append(wdi_core.WDTime(prop_nr='P9',
                                                                 time=self.parse_To_Wikibase_Time(actividade_dt_ini),
                                                                 is_qualifier=True))
                else: qualifiers_actividade.append(wdi_core.WDTime(prop_nr='P9',time=None,snak_type='somevalue',is_qualifier=True))
                if actividade_dt_fim != '0':
                    qualifiers_actividade.append(wdi_core.WDTime(prop_nr='P10',time=self.parse_To_Wikibase_Time(actividade_dt_fim),
                                                                 is_qualifier=True))
                else:qualifiers_actividade.append(wdi_core.WDTime(prop_nr='P10',time=None,snak_type='somevalue',is_qualifier=True))

            locais_de_actividades = []
            for idx_loc_ac in range(len(column_loc_actividade)):
                locais_de_actividades.append(self.get_Wikibase_Qid(df_pessoas[column_loc_actividade[idx_loc_ac]][i]))
                qualifiers_actividade.append(wdi_core.WDItemID(prop_nr='P57', value=locais_de_actividades[idx_loc_ac]['value'],
                                                               snak_type=locais_de_actividades[idx_loc_ac]['snak_type'],
                                                               is_qualifier=True))

            data= [wdi_core.WDString(prop_nr='P17', value=nome_completo['value'], snak_type=nome_completo['snak_type']),
                   wdi_core.WDString(prop_nr='P20', value=nome_outras_grafias['value'],
                                     snak_type=nome_outras_grafias['snak_type']),
                   wdi_core.WDItemID(prop_nr='P4', value=local_nascimento['value'],
                                     snak_type=local_nascimento['snak_type']),
                   wdi_core.WDItemID(prop_nr='P5', value=local_morte['value'], snak_type=local_morte['snak_type']),
                   wdi_core.WDItemID(prop_nr='P33', value=local_enterramento['value'],
                                     snak_type=local_enterramento['snak_type']),
                   wdi_core.WDItemID(prop_nr='P27', value=religiao_values['value'],
                                     snak_type=religiao_values['snak_type']),
                   wdi_core.WDString(prop_nr='P34', value=df_pessoas['_pageName'][i], snak_type='value')]
            print('======== TESTAR INSERÇÃO QUALIFIERS RESIDENCIAS PARA UM REGISTRO!! ======')
            for idx_residencias in range(len(residencias)):
                data.append(wdi_core.WDItemID(prop_nr='P26', value=residencias[idx_residencias]['value'],
                                     snak_type=residencias[idx_residencias]['snak_type'],
                                              qualifiers=qualifiers_residencia))
            for idx_formacoes in range(len(formacoes)):
                data.append(wdi_core.WDItemID(prop_nr='P48', value=formacoes[idx_formacoes]['value'],
                                              snak_type=formacoes[idx_formacoes]['snak_type'],
                                              qualifiers=qualifiers_formacao))
            for idx_postos in range(len(postos)):
                print("inserting posto " + str(postos[idx_postos]['value']))
                data.append(wdi_core.WDItemID(prop_nr='P50', value=postos[idx_postos]['value'],
                                              snak_type=postos[idx_postos]['snak_type'],
                                              qualifiers=qualifiers_posto))
            for idx_cargos in range(len(cargos)):
                print("inserting posto " + str(cargos[idx_cargos]['value']))
                data.append(wdi_core.WDItemID(prop_nr='P8', value=cargos[idx_cargos]['value'],
                                     snak_type=cargos[idx_cargos]['snak_type'],
                                              qualifiers=qualifiers_cargo))
            for idx_actividades in range(len(actividades)):
                data.append(wdi_core.WDItemID(prop_nr='P56', value=actividades[idx_actividades]['value'],
                                     snak_type=actividades[idx_actividades]['snak_type'],
                                              qualifiers=qualifiers_actividade))
            if df_pessoas['pai'][i] != 0:
                description_pai = 'Esse objeto representa o pai da pessoa: ' + df_pessoas['_pageName'][i]
                QID_pai = self.create_new_item_on_wiki(df_pessoas['pai'][i], description_pai)
                data.append(wdi_core.WDItemID(prop_nr='P22', value=QID_pai,snak_type='value'))
            else: data.append(wdi_core.WDItemID(prop_nr='P22', value=object_without_properties['value']
                                                ,snak_type=object_without_properties['snak_type']))
            if df_pessoas['mãe'][i] != 0:
                description_mae = 'Esse objeto representa o pai da pessoa: ' + df_pessoas['_pageName'][i]
                QID_mae = self.create_new_item_on_wiki(df_pessoas['mãe'][i], description_mae)
                data.append(wdi_core.WDItemID(prop_nr='P23', value=QID_mae,snak_type='value'))
            else: data.append(wdi_core.WDItemID(prop_nr='P23', value=object_without_properties['value']
                                                ,snak_type=object_without_properties['snak_type']))
            if df_pessoas['sexo'][i] == 'masculino':
                data.append(wdi_core.WDItemID(prop_nr='P6', value='Q6',snak_type='value'))
            elif df_pessoas['sexo'][i] == 'feminino':
                data.append(wdi_core.WDItemID(prop_nr='P6', value='Q6',snak_type='value'))
            else: data.append(wdi_core.WDItemID(prop_nr='P6', value=object_without_properties['value']
                                                ,snak_type=object_without_properties['snak_type']))
            if df_pessoas['filhos'][i] != 0:
                description_filhos = 'Esse objeto representa o filho da pessoa: ' + df_pessoas['_pageName'][i]
                QID_filho = self.create_new_item_on_wiki(df_pessoas['filhos'][i], description_filhos)
                data.append(wdi_core.WDItemID(prop_nr='P21', value=QID_filho,snak_type='value'))
            else: data.append(wdi_core.WDItemID(prop_nr='P21', value=object_without_properties['value']
                                                ,snak_type=object_without_properties['snak_type']))
            if df_pessoas['cônjuge'][i] != 0:
                description_conjuge = 'Esse objeto representa o cônjuge da pessoa: ' + df_pessoas['_pageName'][i]
                QID_conjuge = self.create_new_item_on_wiki(df_pessoas['cônjuge'][i], description_conjuge)
                data.append(wdi_core.WDItemID(prop_nr='P24', value=QID_conjuge,snak_type='value'))
            else: data.append(wdi_core.WDItemID(prop_nr='P24', value=object_without_properties['value']
                                                ,snak_type=object_without_properties['snak_type']))
            print("inserting brothers: ")
            print(df_pessoas['irmãos'][i])
            if df_pessoas['irmãos'][i] != 0:
                description_irmaos = 'Esse objeto representa o irmão da pessoa: ' + df_pessoas['_pageName'][i]
                QID_irmaos = self.create_new_item_on_wiki(df_pessoas['irmãos'][i], description_irmaos)
                data.append(wdi_core.WDItemID(prop_nr='P25', value=QID_irmaos,snak_type='value'))
            else: data.append(wdi_core.WDItemID(prop_nr='P25', value=object_without_properties['value']
                                                ,snak_type=object_without_properties['snak_type']))
            data_nascimento = self.adjust_Time_Value(df_pessoas['data_nascimento'][i])
            if data_nascimento != '0':
                data.append(wdi_core.WDTime(prop_nr='P2', time=self.parse_To_Wikibase_Time(data_nascimento)))
            else: data.append(wdi_core.WDTime(prop_nr='P2', time=None, snak_type='somevalue'))
            data_morte = self.adjust_Time_Value(df_pessoas['data_morte'][i])
            if data_morte != '0':
                data.append(wdi_core.WDTime(prop_nr='P3', time=self.parse_To_Wikibase_Time(data_morte)))
            else: data.append(wdi_core.WDTime(prop_nr='P3', time=None, snak_type='somevalue'))

            wd_item = wdi_core.WDItemEngine(data=data) # create new item
            wd_item.set_label(label=df_pessoas['_pageName'][i],lang='pt')
            wd_item.set_description(description='Pessoa',lang='pt')
            wd_item.write(self.login_instance)
            item_id = wd_item.entity_metadata.get('id') #retrieve item id