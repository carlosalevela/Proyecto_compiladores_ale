load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Toallas húmedas" AND column "nivel_satisfaccion" != "Satisfecho";
aggregate count column "nivel_satisfaccion_mapeada";
print;
