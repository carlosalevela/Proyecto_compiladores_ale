load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Cloro" AND column "estado_reclamo" == "Pendiente" AND column "nivel_satisfaccion" != "Satisfecho";
aggregate count column "nivel_satisfaccion_mapeada";
print;

