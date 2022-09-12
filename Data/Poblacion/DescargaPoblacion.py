import requests
from bs4 import BeautifulSoup
import pandas as pd
import jsonpickle
import sys

def elimina_MUN(cadena):
    cadena =  cadena.replace('MUN_','')
    return '"'+cadena+'"'


URL = "https://www.ine.es/dynt3/inebase/es/index.htm?padre=517&capsel=525"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

table_elements = soup.find_all("a", class_="titulo t4")

for table_element in table_elements:
    try:
        tableid = table_element.attrs['id']
        table = tableid.replace('t_','')
        URL_TABLE = "http://servicios.ine.es/wstempus/jsstat/ES/DATASET/"+table+"?nult=5"
        table_json = requests.get(URL_TABLE)
       
        contenido = table_json.content

        result = jsonpickle.decode(contenido)
        #dicionario de municipios 
        muni_dic = result['dimension']['municipios']['category']['label']
        
        matriz = pd.DataFrame(list(muni_dic.items()), columns=['Municipio','Nombre'])
        dimensiones_dic = result['dimension']['Per']['category']['label']
        for value_dim in dimensiones_dic.values():
            matriz[value_dim]= 0
        num_annos=len(dimensiones_dic)
    
        total_regs = result['size'][0] 
        valores = result['value']
        fila = 0
        contador = 0
        sexo = 1
        for valor in  valores:
            contador = contador +1
            n_anno = contador%num_annos
            if (fila<total_regs):
                if(n_anno!= 0):
                    if sexo == 1:
                        columna = matriz.columns[n_anno+1]
                        matriz.at[fila, columna] = valor
                else:
                    if sexo == 1:
                        columna = matriz.columns[6]
                        matriz.at[fila, columna] = valor
                    if sexo<3:
                        sexo = sexo+1
                    else:
                        sexo = 1
                        fila = fila +1
        cod_provincia = matriz.at[0,'Municipio']
        cod_provincia = cod_provincia[-2:]
        matriz=matriz.drop(matriz.index[[0]])
        matriz['AumentoPoblacion']= matriz[matriz.columns[2]]-matriz[matriz.columns[6]]
        matriz['Municipio'] = matriz['Municipio'].apply(elimina_MUN)
        sys.displayhook(matriz)
        outputfile = "Data/Poblacion/"+cod_provincia+".csv"
        matriz.to_csv(outputfile, index=False, decimal=',', sep=';')
    
    except Exception as e:
        print("Error Tabla"+table)