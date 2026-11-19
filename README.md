# Workshop 4 · EDA del Proyecto 1 de INVACOM

Universidad Técnica Nacional · ISW-911 Minería de Datos

## Integrantes

- Gaudy Yuliana Chacón Alpizar
- Joab Mauricio Montero Montero
- Ignacio Araya Rojas
- Stuarth Fabricio Miranda Rojas

## Fuente y alcance

Esta versión se basa en las fuentes Northwind del Proyecto 1 de INVACOM, según la aclaración del grupo. Esa selección sustituye el criterio de elegir datos abiertos de Costa Rica indicado en el punto 2 del PDF original del Workshop 4.

Se conservan completos los cinco CSV usados en el alcance comercial del Proyecto 1, dentro de `datos/northwind/`. Sus huellas y conteos se documentan en `manifest.json`. Northwind es un escenario ficticio de ejemplo, como explica [Microsoft](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/northwind-install).

El notebook descarga los CSV de un commit fijo de este repositorio público y verifica sus huellas SHA-256. Integra las líneas de pedido con pedidos, productos, clientes y categorías, conservando 2.155 líneas de 830 pedidos. El análisis selecciona los atributos comerciales y mantiene disponibles los archivos originales completos.

Se concilian 51.317 unidades, importe bruto 1.354.458,59, descuento monetario 88.665,83 e importe neto 1.265.792,76 con las reglas del Proyecto 1. Se propone un árbol de regresión para la cantidad vendida por línea.

## Archivos y ejecución

- `lab4_IC2025.ipynb` contiene el desarrollo documentado y ejecutado, con siete gráficos.
- `data_process.csv` contiene 2.155 filas y 208 columnas numéricas, sin nulos finales.
- `datos/northwind/` contiene las cinco fuentes originales completas y su manifiesto.

Instala las dependencias con `python -m pip install -r requirements.txt` y abre el notebook en Jupyter, VS Code con Jupyter o Google Colab. Ejecuta las celdas en orden para repetir el EDA y generar el CSV.

El notebook diferencia las columnas de predicción de las de auditoría. Los identificadores y los importes calculados a partir de la cantidad se conservan para conciliación. Las imputaciones, la codificación, la estandarización y la conservación de los atípicos se justifican dentro del proceso.

El archivo solicitado para subir al campus es `lab4_IC2025.ipynb`.
