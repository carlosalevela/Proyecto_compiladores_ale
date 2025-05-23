load "reclamos_clientes_colombia.csv";
filter column "producto_servicio" == "Desinfectante";
aggregate average column "nivel_satisfaccion_mapeada";
print;
