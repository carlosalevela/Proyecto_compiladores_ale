load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Pendiente" AND column "producto_servicio" != "Detergente líquido";
aggregate count column "nivel_satisfaccion_mapeada";
print;