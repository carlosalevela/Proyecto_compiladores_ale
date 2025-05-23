load "reclamos_clientes_colombia.csv";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;