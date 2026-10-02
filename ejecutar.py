"""Ejecuta los dos análisis con los CSV incluidos y guarda sus resultados."""
from pathlib import Path
import nbformat
from nbclient import NotebookClient

def main():
    raiz = Path(__file__).resolve().parent
    archivos = [raiz / "ventas-python" / "analisis_ventas.ipynb", raiz / "prestamos-python" / "analisis_prestamos.ipynb"]
    for archivo in archivos:
        cuaderno = nbformat.read(archivo, as_version=4)
        NotebookClient(cuaderno, timeout=180, kernel_name="python3", resources={"metadata": {"path": str(archivo.parent)}}).execute()
        nbformat.write(cuaderno, archivo)
        print(f"Completado: {archivo.relative_to(raiz)}")

if __name__ == "__main__":
    main()
