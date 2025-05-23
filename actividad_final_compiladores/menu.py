import os
import subprocess
import sys

CATEGORIAS = {
    "1": ("solo_aggregates", "Solo Agregaciones"),
    "2": ("con_filtro_simple", "Filtro Simple"),
    "3": ("con_filtro_logico", "Filtro Lógico Compuesto"),
    "4": ("filtros_combinados", "Filtros Combinados")
}

def mostrar_menu():
    print("=== MENÚ DE CONSULTAS DSL ===")
    for key, (_, nombre) in CATEGORIAS.items():
        print(f"{key}. {nombre}")
    print("0. Salir")

def listar_scripts(categoria):
    carpeta = f"scripts/{categoria}"
    archivos = [f for f in os.listdir(carpeta) if f.endswith(".dsl")]
    archivos.sort()
    return archivos

def ejecutar_dsl(path):
    with open(path, 'r', encoding='utf-8') as f:
        contenido = f.read()
    print("Contenido del script DSL:\n")
    print(contenido)
    # Aquí deberías invocar tu parser/intérprete de DSL real

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <ruta_script.dsl>")
    else:
        ejecutar_dsl(sys.argv[1])

def ejecutar_script(path_script):
    print(f"\n📄 Ejecutando: {path_script}\n")
    subprocess.run(["python", "main.py", path_script])
    input("\n🔁 Presiona Enter para continuar...")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige una categoría: ")

        if opcion == "0":
            print("👋 Hasta luego.")
            break

        if opcion not in CATEGORIAS:
            print("❌ Opción no válida.\n")
            continue

        categoria, nombre = CATEGORIAS[opcion]
        scripts = listar_scripts(categoria)

        print(f"\n📂 Scripts disponibles en '{nombre}':")
        for i, script in enumerate(scripts, start=1):
            print(f"{i}. {script}")
        idx = input("Selecciona un script (número): ")

        try:
            idx = int(idx) - 1
            script_name = scripts[idx]
            script_path = f"scripts/{categoria}/{script_name}"
            ejecutar_script(script_path)
        except (ValueError, IndexError):
            print("❌ Opción inválida.\n")

if __name__ == "__main__":
    main()
