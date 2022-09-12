# TFG: Tablas de decisión en la Ingeniería del Conocimiento, caso de uso.

-   **Autor**: Israel Alejandro Cortés Flores
-   **Director**: Juan David Granada Mejía

## Descripción de la propuesta
<p> En este trabajo se desarrolla una aplicación consola en el lenguaje Python que implementa un caso de uso con tablas de decisión en formáto DMN. Pudiendo ejecutar decisiones sobre un dataframe panda.</p>

> Todos los datos utilizados han sido obtenidos de fuentes públicas y se encuentran en la carpeta Datos junto con los programas para su tratamiento.

## Instrucciones de uso
### Ejecutar la decisión para un inmueble
~~~
app.py -a/b Tipología PrecioM2Venta Municipio Estado  
               -a                          	CasodeUsoA  
               -b                         	CasodeUsoB  
               Tipología                  	P/U ->Plurifamiliar/Unifamiliar  
               PrecioM2Venta            	Precio de la oferta (decimal)   
               Municipio                   	Código INE
               Estado                      	Muy Bueno/Bueno/Malo/Muy Malo
~~~
### Ejecutar la decisión a un fichero.csv con los datos de inmuebles
~~~
app.py -a/b -i ifle=fichero_entrada -o ofile=fichero_salida 
               -a                         	CasodeUsoA 
               -b                         	CasodeUsoB 
               -i ifle=fichero_entrada     	Procesa un fichero .csv con las siguientes columnas 
                                            (Tipología;PrecioM2Venta;Municipio;Estado)
               -o ofile=fichero_salida     	Guarda los resultados en un fichero .csv en la columna CalificaInversion
~~~
