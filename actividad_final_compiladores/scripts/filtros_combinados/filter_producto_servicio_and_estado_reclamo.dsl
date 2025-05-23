load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Jabón antibacterial" AND column "estado_reclamo" == "Pendiente";
aggregate sum column "nivel_satisfaccion_mapeada";
print;