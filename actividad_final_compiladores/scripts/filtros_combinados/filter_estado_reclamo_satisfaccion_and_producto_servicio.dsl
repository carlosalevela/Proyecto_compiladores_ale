load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Resuelto" AND column "nivel_satisfaccion" == "Neutral" AND column "producto_servicio" != "Detergente líquido";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;
