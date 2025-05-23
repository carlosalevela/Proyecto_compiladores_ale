load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Cerrado" AND column "producto_servicio" != "Shampoo";
aggregate count column "id_reclamo";
print;
