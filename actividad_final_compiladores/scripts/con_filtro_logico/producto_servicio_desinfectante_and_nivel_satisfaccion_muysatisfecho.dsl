load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Desinfectante" AND column "nivel_satisfaccion" != "Muy satisfecho";
aggregate sum column "nivel_satisfaccion_mapeada";
print;