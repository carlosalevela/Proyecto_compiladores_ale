load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Satisfecho";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;