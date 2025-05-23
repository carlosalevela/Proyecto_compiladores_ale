load "reclamos_clientes_colombia.csv";
filter (column "fecha_respuesta" == "" OR column "fecha_respuesta" == null);
filter (column "nivel_satisfaccion" == "" OR column "nivel_satisfaccion" == "N/A");
aggregate count column "id_reclamo";
print;
