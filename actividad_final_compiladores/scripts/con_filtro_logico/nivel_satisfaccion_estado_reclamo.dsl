load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Insatisfecho" AND column "estado_reclamo" != "Cerrado";
aggregate count column "nivel_satisfaccion_mapeada";
print;