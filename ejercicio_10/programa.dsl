load "empleados.csv";
filter column "dias_laborados" > 25;
filter column "salario" > 1200;
count column "dias_laborados" > 25;
count column "salario" > 1200;
count column "salario" between 700 and 1200;
print;