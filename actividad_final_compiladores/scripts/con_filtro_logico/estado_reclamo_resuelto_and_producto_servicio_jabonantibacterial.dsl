load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Resuelto" AND column "producto_servicio" != "Jabón antibacterial";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;