load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "En proceso" AND column "nivel_satisfaccion" != "Neutral";
aggregate sum column "nivel_satisfaccion_mapeada";
print;