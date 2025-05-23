load "reclamos_clientes_colombia.csv";
filter column "responsable" == "Ana Sánchez";
filter column "fecha_respuesta" >= "2025-04-01";
filter column "fecha_respuesta" <= "2025-04-30";
aggregate count column "id_reclamo";
aggregate average column "nivel_satisfaccion_mapeada";
print;
