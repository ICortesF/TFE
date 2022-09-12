import sys, getopt

#Ej. Llamada simple python3 app.py -a P 3650.5 28079 Malo      
#Ej. Llamada ficheros python3 app.py -b -i entrada.csv -o salida.csv  

def print_help():
  print('app.py -a/b -i ifle=fichero_entrada -o ofile=fichero_salida Tipología PrecioM2Venta Municipio Estado')
  print('               -h                          Ayuda')
  print('               -a                          CasodeUsoA Rules')
  print('               -b                          CasodeUsoB Rules')
  print('               -i ifle=fichero_entrada     Procesa un fichero .csv')
  print('               -o ofile=fichero_salida     Guarda los resultados en un fichero .csv file')
  print('               Tipología                   P/U ->Plurifamiliar/Unifamiliar')
  print('               PrecioM2Venta               decimal precio de la oferta')
  print('               Municipio                   Cod.Ine')
  print('               Estado                      Muy Bueno/Bueno/Malo/Muy Malo')



def main(argv):
    casodeuso = "B"
    tipologia = "U"
    precioM2Venta=2935
    municipio="28079"
    estado="Muy Bueno"
    inputfile = ""
    outputfile = ""

    try:
      opts, args = getopt.getopt(argv,"habi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print_help()
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
        print_help()
        sys.exit()
      elif opt in ("-a"):
        casodeuso = "A"
      elif opt in ("-b"):
        casodeuso = "B"
      elif opt in ("-i", "--ifile"):
        inputfile = arg
      elif opt in ("-o", "--ofile"):
        outputfile = arg
    if len(args)<4 and len(inputfile)<1:
        print_help()
        sys.exit()
    else:
        if len(inputfile)<1:
            tipologia =  args[0]
            precioM2Venta=float(args[1])
            municipio=args[2]
            estado=args[3]
          
    
    import pyDMNrules
    dmnRules =  pyDMNrules.DMN()

   

if __name__ == "__main__":
    main(sys.argv[1:])
