def get_cheapest_hotel(number):  #DO NOT change the function's name
        #Variaveis de apoio
        diasLocados = []
        lakewood = []
        bridgewood = []
        ridgewood = []
        valoresKey = dict
        credenciais = ['Regular','Rewards']
        credencialEscolhida = ''


        # Dicionario
        diaSemana ={'sun': {'regular':{ # Dicionario contendo como keys os dias da semana, credencial, hoteis, valor para final de semana e valor para semana
                            'Lakewood' : {'vfds': 90},
                            'Bridgewood' : {'vfds': 60},
                            'Ridgewood' : {'vfds': 150},
                            },
                            'reward':{
                            'Lakewood' : {'vfds': 80},
                            'Bridgewood' : {'vfds': 50},
                            'Ridgewood' : {'vfds': 40}
                            },
                            },
                    'sat': {'regular':{
                            'Lakewood' : {'vfds': 90},
                            'Bridgewood' : {'vfds': 60},
                            'Ridgewood' : {'vfds': 150},
                            },
                            'reward':{
                            'Lakewood' : {'vfds': 80},
                            'Bridgewood' : {'vfds': 50},
                            'Ridgewood' : {'vfds': 40}
                            },
                            },
                    'mon': {'regular':{
                            'Lakewood' : {'vs': 110},
                            'Bridgewood' : {'vs': 160},
                            'Ridgewood' : {'vs': 220},
                            },
                            'reward':{
                            'Lakewood' : {'vs': 80},
                            'Bridgewood' : {'vs': 110},
                            'Ridgewood' : {'vs': 100}
                            },
                            },
                    'tues': {'regular':{
                            'Lakewood' : {'vs': 110},
                            'Bridgewood' : {'vs': 160},
                            'Ridgewood' : {'vs': 220},
                            },
                            'reward':{
                            'Lakewood' : {'vs': 80},
                            'Bridgewood' : {'vs': 110},
                            'Ridgewood' : {'vs': 100}
                            },
                            },
                    'wed': {'regular':{
                            'Lakewood' : {'vs': 110},
                            'Bridgewood' : {'vs': 160},
                            'Ridgewood' : {'vs': 220},
                            },
                            'reward':{
                            'Lakewood' : {'vs': 80},
                            'Bridgewood' : {'vs': 110},
                            'Ridgewood' : {'vs': 100}
                            },
                            },
                    'thur':{'regular':{
                            'Lakewood' : {'vs': 110},
                            'Bridgewood' : {'vs': 160},
                            'Ridgewood' : {'vs': 220},
                            },
                            'reward':{
                            'Lakewood' : {'vs': 80},
                            'Bridgewood' : {'vs': 110},
                            'Ridgewood' : {'vs': 100}
                            },
                            },
                    'fri': {'regular':{
                            'Lakewood' : {'vs': 110},
                            'Bridgewood' : {'vs': 160},
                            'Ridgewood' : {'vs': 220},
                            },
                            'reward':{
                            'Lakewood' : {'vs': 80},
                            'Bridgewood' : {'vs': 110},
                            'Ridgewood' : {'vs': 100}
                            },
                            },
                            }

        entrada = number
            
        for cred in credenciais: # Capturar a entrada da credencial digitada na String e salvar na variavel "Credencial escolhida"
            if cred in entrada: # Se ao percorrer a lista credenciais achar algo igual ao valor de cred
                credencialEscolhida = cred # a variavel credencialEscolhida recebera uma credencial

        for dayS in diaSemana : # Capturar a entrada dos dias, comparar com minha lista 'Days' e se possuir algum elemento dessa lista, adicionar na varivel diasLocados
            if dayS in entrada:# Se ao percorrer a lista credenciais achar algo igual ao valor dayS
                diasLocados.append(dayS)# adicionar as string a lista diasLocados

                
        if credencialEscolhida == 'Regular': # Se a credencial escolhida for Regular, 
            for days, result in diaSemana.items(): # Criando um for para iterar nos dicionarios recuperando keys e valores das keys contidos no dicionario
                if days in diasLocados: # Se algumas das keys do dicionario estiver presente na lista diasAlocados
                        valoresKey = result['regular'] # o dicionario valoresKey recebera todos os resultados da key regular
                        for l in valoresKey['Lakewood'].values(): # percorrer os valores da key Lakewood
                            lakewood += [l] # Adicionar os valores da Key na lista lakewood
                            for b in valoresKey['Bridgewood'].values():# percorrer os valores da key Bridgewood
                                bridgewood +=[b]# Adicionar os valores da Key na lista Bridgewood
                                for r in valoresKey['Ridgewood'].values():# percorrer os valores da key Ridgewood
                                    ridgewood += [r]# Adicionar os valores da Key na lista Ridgewood
                
        elif credencialEscolhida == 'Rewards':# Se a credencial escolhida for Rewards, 
            for days, result in diaSemana.items(): # Criando um for para iterar nos dicionarios recuperando keys e valores das keys contidos no dicionario
                if days in diasLocados: # Se algumas das keys do dicionario estiver presente na lista diasAlocados
                        valoresKey = result['reward']# o dicionario valoresKey recebera todos os resultados da key reward
                        for l in valoresKey['Lakewood'].values():# percorrer os valores da key Lakewood
                            lakewood += [l] #Adicionar os valores da Key na lista lakewood
                            for b in valoresKey['Bridgewood'].values():# percorrer os valores da key Bridgewood
                                bridgewood +=[b]# Adicionar os valores da Key na lista Bridgewood
                                for r in valoresKey['Ridgewood'].values():# percorrer os valores da key Ridgewood
                                    ridgewood += [r]# Adicionar os valores da Key na lista Ridgewood
        else:
            pass

        maisBarato = '' #variavel inicializada
        somaL = sum(lakewood)     #a variavel recebe a soma da lista lakewood           
        somaB = sum(bridgewood)#a variavel recebe a soma da lista bridgewood
        somaR = sum(ridgewood)#a variavel recebe a soma da lista ridgewood
        
        if somaL == somaB or somaR == somaL: # se as somas forem iguais
            maisBarato = 'Ridgewood'
        elif somaL < somaB:
            maisBarato = "Lakewood"
        elif somaB < somaR:
            maisBarato = "Bridgewood"
        
        else:
             pass

        cheapest_hotel = maisBarato
        return cheapest_hotel
