import sys, getopt

def main(argv):
    casodeuso = "B"
    tipologia = "U"
    precioM2Venta=2935
    municipio="28079"
    estado="Muy Bueno"
    inputfile = ""
    outputfile = ""
    rulesfile = "Rules/CasodeUsoA.xlsx"
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
          

if __name__ == "__main__":
    main(sys.argv[1:])
