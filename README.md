# Laboratorio 4 — Análisis exploratorio de INVACOM_DW

**Universidad Técnica Nacional · ISW-911 Minería de Datos**

## Integrantes

- Gaudy Yuliana Chacón Alpizar
- Joab Mauricio Montero Montero
- Ignacio Araya Rojas
- Stuarth Fabricio Miranda Rojas

## Objetivo y fuente de datos

Aplicar análisis exploratorio de datos (EDA) en Python al Data Warehouse de INVACOM, desarrollado en el Proyecto 1 del curso. El alcance utiliza el DW por solicitud del equipo en sustitución de los datos abiertos indicados en el enunciado original.

La fuente exclusiva es una extracción de Oracle del esquema `INVACOM_DW`, realizada el **26 de noviembre de 2026**. La consulta integra `FACT_VENTAS`, `DIM_TIEMPO`, `DIM_PRODUCTO` y `DIM_CLIENTE`, con una fila por combinación de pedido y producto. Se preservan los importes oficiales almacenados en la tabla de hechos. Los datos se descargan desde GitHub y se verifican mediante SHA-256 antes de analizarlos.

Proyecto de referencia: [INVACOM Data Warehouse](https://github.com/joab1310/invacom-data-warehouse).

## Entregables

| Archivo | Descripción |
| --- | --- |
| [lab4_IC2025.ipynb](lab4_IC2025.ipynb) | Notebook final ejecutado, con documentación, resultados y siete gráficos. |
| [data_process.csv](data_process.csv) | Dataset final de 2.155 filas y 188 columnas. |
| [datos/invacom_dw/invacom_dw_ventas.csv](datos/invacom_dw/invacom_dw_ventas.csv) | Extracción original de Oracle, 16 columnas. |
| [datos/invacom_dw/manifest.json](datos/invacom_dw/manifest.json) | Fecha de extracción, hash SHA-256, conteos y totales conciliados. |
| [sql/01_extraccion_invacom_dw.sql](sql/01_extraccion_invacom_dw.sql) | Consulta SQL de solo lectura al esquema estrella. |
| [exportar_invacom_dw.py](exportar_invacom_dw.py) | Exportador y conciliador de datos reales de Oracle. |
| [requirements.txt](requirements.txt) | Dependencias de Python. |

## Resultados

| Indicador | Resultado |
| --- | ---: |
| Líneas de venta | 2.155 |
| Pedidos únicos | 830 |
| Unidades vendidas | 51.317 |
| Importe bruto | 1.354.458,59 |
| Descuento monetario | 88.665,83 |
| Importe neto | 1.265.792,76 |
| Nulos en la extracción y en el dataset final | 0 |
| Duplicados por pedido y producto | 0 |
| Columnas originales | 16 |
| Columnas finales | 188 |
| Predictores / auditoría / objetivo | 181 / 6 / 1 |
| Gráficos / errores de ejecución | 7 / 0 |

La conciliación coincide con las referencias documentadas del TKT-17 del proyecto INVACOM. Los valores atípicos detectados mediante IQR son: cantidad 87, precio unitario derivado 98, tasa de descuento derivada 20, bruto 163, descuento 314 y neto 170. Se conservan las observaciones válidas para no distorsionar los totales ni la demanda.

## Cobertura del laboratorio

El notebook incluye inspección inicial, nombres de columnas en español, análisis gráfico de nulos y atípicos, funciones de imputación justificadas, conversión de tipos, codificación one-hot, estandarización, correlaciones, selección de un modelo y exportación del dataset. La variable dependiente es `cantidad_vendida`; el modelo candidato es un árbol de decisión de regresión. Los identificadores, importes y sus derivados se excluyen de los predictores para prevenir fuga de información. No se introducen nulos artificiales. El entrenamiento del modelo no forma parte del alcance de selección y justificación solicitado.

## Cómo reproducir el análisis

Se requiere Python y acceso a GitHub. **No es necesario instalar Oracle ni ejecutar nuevamente la extracción** para revisar la entrega publicada.

```bash
git clone https://github.com/nachoar24/workshop-4-mineria-datos.git
cd workshop-4-mineria-datos
python -m pip install -r requirements.txt
jupyter nbconvert --to notebook --execute --inplace lab4_IC2025.ipynb
```

También puede abrirse el notebook en Jupyter o VS Code y ejecutar todas sus celdas. Por defecto, descarga el CSV y el manifiesto del commit fijo [59b90ec](https://github.com/nachoar24/workshop-4-mineria-datos/commit/59b90ec4a45c9d40731f49990f3df39ece7fcc73).

La ejecución documentada utilizó una copia local idéntica por SHA-256, ya que el entorno de ejecución no disponía de acceso HTTP externo. Para repetirla sin conexión, en PowerShell:

```powershell
$env:LAB4_LOCAL_DIR = (Resolve-Path .\datos\invacom_dw).Path
jupyter nbconvert --to notebook --execute --inplace lab4_IC2025.ipynb
Remove-Item Env:LAB4_LOCAL_DIR
```

Huellas SHA-256 de los archivos de la entrega:

- Extracción: `d8fcb1539f76b36b9210d2a08e51df3e9ae371482e929b808fadedad033adc7d`.
- Dataset procesado: `d56bb8d86ee3f0193fc0a6f243b60e8c3cd3ea920caae8708d59953dfeee524d`.

## Nueva extracción (opcional)

Desde un equipo con acceso a Oracle, ejecutar `python exportar_invacom_dw.py`. El programa solicita el DSN (por ejemplo, localhost:1521/XEPDB1, según el servicio configurado) y la contraseña; el usuario predeterminado es INVACOM_DW. También admite las variables ORACLE_DSN, ORACLE_USER y ORACLE_PASSWORD. Nunca publicar credenciales.

El exportador realiza únicamente consultas de lectura, concilia los totales contra FACT_VENTAS y genera el CSV y manifiesto. Una nueva extracción requiere publicar ambos archivos, actualizar explícitamente el commit y hash fijados en el notebook, volver a ejecutar todas las celdas y validar los resultados. La entrega actual queda fijada al lote del 26/11/2026.

## Estado de entrega

Desarrollo técnico completado. El archivo requerido por el enunciado es **lab4_IC2025.ipynb**; el dataset procesado se conserva como entregable adicional. Corresponde al equipo subir el notebook al campus virtual y confirmar la autorización docente para utilizar el DW, si todavía no se ha confirmado.

Las fuentes anteriores que ya no se utilizan se retiraron de la rama principal; su historial permanece en Git.
