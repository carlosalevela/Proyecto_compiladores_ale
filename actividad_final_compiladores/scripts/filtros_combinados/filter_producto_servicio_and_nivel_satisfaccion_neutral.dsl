load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Suavizante" AND column "nivel_satisfaccion" == "Muy insatisfecho" AND column "nivel_satisfaccion" != "Neutral";
aggregate sum column "nivel_satisfaccion_mapeada";
print;
