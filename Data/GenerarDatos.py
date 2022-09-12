import os, sys
import pandas as pd

def limpiacomillas(cadena):
    return cadena.replace('"','')

def limpiamun(cadena):
    return cadena [-5:]

def poncomillas(cadena):
    return '"'+cadena+'"'

arr = os.listdir('Data/Poblacion/')

poblaciones = pd.DataFrame(None,columns=['Municipio', 'Nombre','2021','2020','2019','2018','2017','AumentoPoblacion'])

dataTypes = {'Municipio': str , 'Nombre': str,'2021': float,'2020': float,'2019': float,'2018': float,'2017': float,'AumentoPoblacion': float}
for file in arr:
    if file[-3:]=='csv':
        dfInput = pd.read_csv('Data/Poblacion/'+file, dtype=dataTypes, delimiter=';', decimal=',')
        poblaciones = pd.concat([poblaciones,dfInput])

poblaciones['Municipio'] = poblaciones['Municipio'].apply(limpiacomillas)
poblaciones = poblaciones.drop(columns=['2021','2020','2019','2018','2017'])
sys.displayhook(poblaciones)

dataTypes = {'MunicipioPrecio': str , 'PrecioM2MedMunTipo': float}
dfPrecios = pd.read_csv('Data/2022Q2Precios.csv', dtype=dataTypes, delimiter=';', decimal=',')

sys.displayhook(dfPrecios)

dataTypes = {'MunicipioRenta': str, 'RentaMunicipio': float, 'RentaMedia': float}
dfRentas = pd.read_csv('Data/2017RentaHacienda.csv', dtype=dataTypes, delimiter=';', decimal=',')
dfRentas['MunicipioRenta']=dfRentas['MunicipioRenta'].apply(limpiamun)
sys.displayhook(dfRentas)

#dfdatos=dfPrecios.set_index('MunicipioPrecio').join(dfRentas.set_index('MunicipioRenta'), how='left')
#sys.displayhook(dfdatos)

#dfdatos2=dfdatos.join(poblaciones.set_index('Municipio'), how='left')
#sys.displayhook(dfdatos2)


dfdatos = pd.merge(dfPrecios,dfRentas, left_on='MunicipioPrecio', right_on='MunicipioRenta')
sys.displayhook(dfdatos)

dfdatos2 = pd.merge(dfdatos,poblaciones, left_on='MunicipioPrecio', right_on='Municipio')

dfdatos2 = dfdatos2.drop(columns=['MunicipioPrecio','MunicipioRenta'])
dfdatosfin = dfdatos2[["Municipio", "Nombre", "PrecioM2MedMunTipo","RentaMunicipio","RentaMedia","AumentoPoblacion"]]
dfdatosfin["Municipio"] = dfdatosfin["Municipio"].apply(poncomillas)
sys.displayhook(dfdatosfin)
outputfile = "Data/DatosFinales.csv"
dfdatosfin.to_csv(outputfile, index=False, decimal=',', sep=';')