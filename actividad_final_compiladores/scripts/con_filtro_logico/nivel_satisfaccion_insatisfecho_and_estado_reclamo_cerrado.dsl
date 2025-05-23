load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Insatisfecho" AND column "estado_reclamo" != "Cerrado";
aggregate sum column "nivel_satisfaccion_mapeada";
print;