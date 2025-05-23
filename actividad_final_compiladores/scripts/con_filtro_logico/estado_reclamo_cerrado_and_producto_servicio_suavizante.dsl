load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Cerrado" AND column "producto_servicio" != "Suavizante";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;