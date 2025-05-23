load "reclamos_clientes_colombia.csv";
aggregate count column "estado_reclamo";
aggregate count column "producto_servicio";
aggregate count column "cliente";
aggregate count column "descripcion_reclamo";
print;