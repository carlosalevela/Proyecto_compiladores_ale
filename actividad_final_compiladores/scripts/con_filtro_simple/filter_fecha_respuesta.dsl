load "reclamos_clientes_colombia.csv";
filter column "fecha_respuesta" == "2025-03-25";
aggregate count column "id_reclamo";
print;

