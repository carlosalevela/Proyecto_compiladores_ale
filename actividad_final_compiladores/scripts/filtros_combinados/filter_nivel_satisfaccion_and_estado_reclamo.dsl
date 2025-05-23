load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy satisfecho" AND column "estado_reclamo" != "En proceso";
aggregate average column "nivel_satisfaccion_mapeada";
print;

