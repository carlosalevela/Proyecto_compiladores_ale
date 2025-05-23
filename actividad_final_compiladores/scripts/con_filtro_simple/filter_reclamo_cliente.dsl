load "reclamos_clientes_colombia.csv";
filter column "cliente" == "Juan Pérez";
filter column "fecha_reclamo" >= "2025-01-01";
filter column "fecha_reclamo" <= "2025-03-31";
aggregate count column "id_reclamo";
aggregate average column "nivel_satisfaccion_mapeada";
print;
