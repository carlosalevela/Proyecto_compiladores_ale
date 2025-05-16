load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Desinfectante";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Pendiente";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Neutral";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Satisfecho";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Cerrado";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Neutral";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;
