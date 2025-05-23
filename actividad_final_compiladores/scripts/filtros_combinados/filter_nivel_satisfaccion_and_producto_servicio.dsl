load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy insatisfecho" AND column "producto_servicio" == "Desinfectante";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;
