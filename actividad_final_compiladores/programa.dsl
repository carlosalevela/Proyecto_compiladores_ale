

load "reclamos_clientes_colombia.csv";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;



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



load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Insatisfecho";
filter column "nivel_satisfaccion" == "Muy satisfecho" AND column "estado_reclamo" != "En proceso";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Insatisfecho";
filter column "producto_servicio" == "Toallas húmedas" AND column "nivel_satisfaccion" != "Satisfecho";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy insatisfecho";
filter column "producto_servicio" == "Suavizante" AND column "nivel_satisfaccion" != "Neutral";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy insatisfecho";
filter column "nivel_satisfaccion" == "Muy satisfecho" AND column "producto_servicio" != "Shampoo";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Muy satisfecho";
filter column "nivel_satisfaccion" == "Muy satisfecho" AND column "estado_reclamo" != "Pendiente";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Cloro";
filter column "estado_reclamo" == "Pendiente" AND column "nivel_satisfaccion" != "Satisfecho";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Desinfectante";
filter column "nivel_satisfaccion" == "Muy insatisfecho" AND column "producto_servicio" != "Desinfectante";
aggregate sum column "nivel_satisfaccion_mapeada";
aggregate average column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Cerrado";
filter column "nivel_satisfaccion" == "Satisfecho" AND column "estado_reclamo" != "Resuelto";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Jabón antibacterial";
filter column "estado_reclamo" == "Pendiente" AND column "producto_servicio" != "Shampoo";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "estado_reclamo" == "Resuelto";
filter column "nivel_satisfaccion" == "Neutral" AND column "producto_servicio" != "Detergente líquido";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate sum column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Suavizante";
filter column "producto_servicio" == "Suavizante" AND column "nivel_satisfaccion" != "Insatisfecho";
aggregate count column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "nivel_satisfaccion" == "Satisfecho";
filter column "producto_servicio" == "Papel higiénico" AND column "nivel_satisfaccion" != "Satisfecho";
aggregate average column "nivel_satisfaccion_mapeada";
aggregate count column "nivel_satisfaccion_mapeada";
print;

load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Suavizante";
filter column "estado_reclamo" == "En proceso" AND column "producto_servicio" != "Suavizante";
aggregate average column "nivel_satisfaccion_mapeada";
print;