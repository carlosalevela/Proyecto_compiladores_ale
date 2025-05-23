load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Cerrado" AND column "nivel_satisfaccion" == "Satisfecho" AND column "estado_reclamo" != "Resuelto";
aggregate sum column "nivel_satisfaccion_mapeada";
print;
