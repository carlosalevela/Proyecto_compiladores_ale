load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Pendiente";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;