load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Resuelto" AND column "nivel_satisfaccion" != "Muy insatisfecho";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy insatisfecho";
filter column "nivel_satisfaccion" == "Neutral" AND column "producto_servicio" != "Cloro";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Cloro" AND column "estado_reclamo" != "En proceso";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Shampoo";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Satisfecho";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy insatisfecho";
filter column "estado_reclamo" == "Pendiente" AND column "producto_servicio" != "Toallas húmedas";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Pendiente";
filter column "estado_reclamo" == "Pendiente" AND column "producto_servicio" != "Papel higiénico";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy insatisfecho";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy insatisfecho";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Limpiavidrios";
filter column "estado_reclamo" == "Cerrado" AND column "nivel_satisfaccion" != "Muy satisfecho";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Limpiavidrios";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "En proceso";
filter column "producto_servicio" == "Cepillo de baño" AND column "nivel_satisfaccion" != "Muy satisfecho";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Resuelto" AND column "producto_servicio" != "Shampoo";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Pendiente";
filter column "producto_servicio" == "Toallas húmedas" AND column "estado_reclamo" != "En proceso";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Detergente líquido";
filter column "estado_reclamo" == "Pendiente" AND column "producto_servicio" != "Shampoo";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Pendiente";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "En proceso";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy insatisfecho" AND column "estado_reclamo" != "En proceso";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Insatisfecho";
filter column "producto_servicio" == "Desinfectante" AND column "estado_reclamo" != "En proceso";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Papel higiénico";
filter column "nivel_satisfaccion" == "Insatisfecho" AND column "producto_servicio" != "Desinfectante";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy satisfecho";
filter column "estado_reclamo" == "Resuelto" AND column "producto_servicio" != "Cepillo de baño";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy insatisfecho";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Toallas húmedas";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "En proceso";
filter column "producto_servicio" == "Detergente líquido" AND column "nivel_satisfaccion" != "Neutral";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Toallas húmedas" AND column "estado_reclamo" != "Resuelto";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy insatisfecho";
filter column "producto_servicio" == "Cepillo de baño" AND column "estado_reclamo" != "Resuelto";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Neutral" AND column "estado_reclamo" != "Resuelto";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Resuelto";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Limpiavidrios";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Cerrado" AND column "nivel_satisfaccion" != "Insatisfecho";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Cepillo de baño";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy satisfecho" AND column "producto_servicio" != "Cepillo de baño";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Cerrado" AND column "nivel_satisfaccion" != "Neutral";
aggregate count column "nivel_satisfaccion_mapeada";
print;