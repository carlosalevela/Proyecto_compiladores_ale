load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy satisfecho" AND column "estado_reclamo" != "Pendiente";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;
