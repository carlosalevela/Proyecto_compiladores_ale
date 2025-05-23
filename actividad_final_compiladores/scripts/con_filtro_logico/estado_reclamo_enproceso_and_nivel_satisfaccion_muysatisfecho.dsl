load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "En proceso" AND column "nivel_satisfaccion" != "Muy insatisfecho";
aggregate average column "nivel_satisfaccion_mapeada";
print;