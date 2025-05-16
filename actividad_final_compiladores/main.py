import sys
import os
from antlr4 import *
from CSVQueryDSLLexer import CSVQueryDSLLexer
from CSVQueryDSLParser import CSVQueryDSLParser
from MyCSVVisitor import MyCSVVisitor

def ejecutar_script(path_script):
    input_stream = FileStream(path_script, encoding='utf-8')
    lexer = CSVQueryDSLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CSVQueryDSLParser(token_stream)
    tree = parser.prog()
    visitor = MyCSVVisitor()
    visitor.visit(tree)

def ejecutar_carpeta(path_folder):
    archivos = [f for f in os.listdir(path_folder) if f.endswith(".dsl")]
    archivos.sort()
    for archivo in archivos:
        print(f"\n=== Ejecutando script: {archivo} ===\n")
        ejecutar_script(os.path.join(path_folder, archivo))

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <ruta_script_o_carpeta>")
        sys.exit(1)

    ruta = sys.argv[1]

    if os.path.isfile(ruta) and ruta.endswith(".dsl"):
        ejecutar_script(ruta)
    elif os.path.isdir(ruta):
        ejecutar_carpeta(ruta)
    else:
        print(f"Error: '{ruta}' no es un archivo .dsl ni una carpeta válida.")
        sys.exit(1)

if __name__ == "__main__":
    main()
