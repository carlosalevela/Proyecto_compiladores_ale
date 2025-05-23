load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Cepillo de baño";
aggregate count column "id_reclamo";
aggregate average column "nivel_satisfaccion_mapeada";
print;