load "reclamos_clientes_colombia.csv";
filter (column "nivel_satisfaccion" == "Muy insatisfecho" OR column "nivel_satisfaccion" == "Muy satisfecho") AND column "producto_servicio" != "Shampoo";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;
