load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion_mapeada" <= 2;
aggregate count column "id_reclamo";
print;