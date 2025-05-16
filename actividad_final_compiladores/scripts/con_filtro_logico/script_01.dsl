load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Cerrado" AND column "producto_servicio" != "Suavizante";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "En proceso" AND column "nivel_satisfaccion" != "Muy insatisfecho";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Insatisfecho" AND column "estado_reclamo" != "Cerrado";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Insatisfecho" AND column "estado_reclamo" != "Cerrado";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Pendiente" AND column "nivel_satisfaccion" != "Satisfecho";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Pendiente" AND column "producto_servicio" != "Detergente líquido";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Desinfectante" AND column "nivel_satisfaccion" != "Muy satisfecho";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Resuelto" AND column "producto_servicio" != "Jabón antibacterial";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "En proceso" AND column "nivel_satisfaccion" != "Neutral";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Cerrado" AND column "producto_servicio" != "Shampoo";
aggregate sum column "nivel_satisfaccion_mapeada";
print;
