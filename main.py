import pandas as pd
import os
import glob

folder_path = 'src\\data\\raw'

excel_files = glob.glob( os.path.join(folder_path, '*.xlsx'))

if not excel_files:
    print("Nenhum arquivo encontrado")
else:

    dfs = []

    for excel_file in excel_files:

        try:
            #leio o arquivo do excel
            df_temp = pd.read_excel(excel_file)

            #pegar o nome do arquivo
            file_name = os.path.basename(excel_file)
            
            df_temp['filename'] = file_name


            #Criação da coluna location
            if 'brasil' in file_name.lower():
                df_temp['location'] = 'br'
            elif 'france' in file_name.lower():
                df_temp['location'] = 'fr'
            elif 'italian' in file_name.lower():
                df_temp['location'] = 'it'

            #Criação da coluna campanha
            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')

            #Guarda dados tratados dentro de uma dataframe
            dfs.append(df_temp)

            
            
        except Exception as e:
            print(f"Erro ao ler o arquivo {excel_file} : {e}")

if dfs:

    #concatena todas as tabelas salvas no dfs em uma única tabela
    result = pd.concat(dfs, ignore_index=True)            
            
    #caminho de saída
    output_file = os.path.join('src', 'data', 'ready', 'clean.xlsx')
        
    #configurando o motor de escrita
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    #leva os dados do resultado a serem escritos no motor do excel configurado
    result.to_excel(writer, index=False)

    #salva o arquivo de excel
    writer._save()
else:
    print("nenhum dado para ser salvo")

