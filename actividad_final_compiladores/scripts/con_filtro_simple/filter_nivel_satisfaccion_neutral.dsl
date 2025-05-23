load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Neutral";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;