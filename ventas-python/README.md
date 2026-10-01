# Análisis exploratorio de ventas con Python

**Autor:** Santiago Lara. Proyecto académico individual, Introducción a Ciencia de Datos, LEAD University.

## Objetivo
Explorar ventas semanales de tiendas, sus variaciones por período y su relación con semanas festivas y variables del entorno.

## Trabajo realizado
- Carga y revisión de datos, conversión de fechas y búsqueda de valores faltantes y duplicados.
- Creación de variables temporales y agrupaciones por tienda, mes y trimestre.
- Estadísticas descriptivas, distribuciones, correlaciones y gráficos comparativos.
- Documentación del análisis en Jupyter Notebook.

## Archivos y ejecución
El código está en [analisis_ventas.ipynb](analisis_ventas.ipynb).

El trabajo identifica como fuente el [Walmart Dataset de Kaggle](https://www.kaggle.com/datasets/yasserh/walmart-dataset). El CSV no se incluye. Obtenerlo de la fuente respetando sus condiciones y guardar `Walmart_Sales.csv` en esta carpeta.

Desde la raíz del repositorio:
```sh
python -m pip install -r requirements.txt
python -m jupyter lab
```
Abrir el cuaderno y ejecutar sus celdas en orden.

## Alcance
No se ejecutó nuevamente al preparar este portafolio, por ausencia del CSV original. Las dependencias no están fijadas ni se ha verificado su compatibilidad en un entorno nuevo.

Las comparaciones anuales requieren revisar que los períodos tengan igual cobertura. El indicador festivo no prueba un efecto causal. Las correlaciones describen asociación y no constituyen por sí solas una prueba de significancia. No se publican cifras de impacto comercial.
