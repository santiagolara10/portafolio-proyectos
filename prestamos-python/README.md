# Análisis de solicitudes de préstamos con Python

**Autor:** Santiago Lara. Proyecto académico individual, Introducción a Ciencia de Datos, LEAD University.

## Objetivo
Explorar información de solicitudes de préstamos de vivienda y desarrollar una primera aproximación a la clasificación de su estado de aprobación.

## Trabajo realizado
- Revisión de tipos de datos, valores faltantes y duplicados.
- Imputación, preparación de variables y exportación de un dataset limpio.
- Estadísticas descriptivas y visualizaciones.
- Implementación de regresión logística, división entrenamiento/prueba y evaluación mediante matriz de confusión y métricas de clasificación.

## Archivos y ejecución
El código está en [analisis_prestamos.ipynb](analisis_prestamos.ipynb).

El cuaderno identifica los datos como Home Loan Approval Dataset (Dream Housing Finance), obtenidos de Kaggle. No se recuperó el enlace exacto de la descarga ni el CSV original; no se redistribuyen los datos. Para ejecutar se necesita el archivo original `loan_sanction_train.csv` en esta carpeta. El CSV limpio de la entrega no sustituye directamente esa entrada.

Desde la raíz del repositorio:
```sh
python -m pip install -r requirements.txt
python -m jupyter lab
```
Abrir el cuaderno y ejecutar sus celdas en orden.

## Alcance y mejoras pendientes
Es una práctica introductoria, no un sistema de decisiones crediticias. La variable objetivo corresponde a aprobación histórica, no a impago.

El código original imputa y codifica datos antes de separar entrenamiento y prueba. Para evaluar generalización correctamente, ese preprocesamiento debe aprenderse solo con entrenamiento, dentro de un pipeline. También corresponde revisar la codificación de variables nominales y comparar con una línea base.

No se ejecutó nuevamente durante la preparación del portafolio ni se publican métricas como resultados validados. Las dependencias no están fijadas ni se ha verificado su compatibilidad en un entorno nuevo.
