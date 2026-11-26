# Laboratorio 4 · EDA de INVACOM_DW
Universidad Técnica Nacional · ISW-911 Minería de Datos

## Integrantes
- Gaudy Yuliana Chacón Alpizar
- Joab Mauricio Montero Montero
- Ignacio Araya Rojas
- Stuarth Fabricio Miranda Rojas

## Fuente
El análisis usa exclusivamente INVACOM_DW (FACT_VENTAS, DIM_TIEMPO, DIM_PRODUCTO, DIM_CLIENTE). Los CSV históricos de Northwind se conservan como antecedentes, no se consumen en el notebook. La sustitución de datos abiertos corresponde al alcance solicitado por el grupo.

## Ejecución
1. Clonar el repositorio y ejecutar `python -m pip install -r requirements.txt`.
2. Desde un equipo con acceso a Oracle ejecutar `python exportar_invacom_dw.py`. Ingresar DSN (por ejemplo localhost:1521/XEPDB1, o el servicio real), usuario INVACOM_DW por defecto y contraseña cuando se solicite. También acepta ORACLE_DSN, ORACLE_USER, ORACLE_PASSWORD por variables de entorno. Nunca publicar credenciales.
3. Revisar y publicar `datos/invacom_dw/invacom_dw_ventas.csv` y `datos/invacom_dw/manifest.json` (sin caracteres invisibles: carpeta invacom_dw). El exportador concilia contra los hechos de Oracle y genera SHA-256.
4. Abrir lab4_IC2025.ipynb; conservar REF_GIT fijado al commit de la extracción, ejecutar todas las celdas, guardar salidas y publicar data_process.csv si se requiere reproducir la entrega. Alternativamente ejecutar `jupyter nbconvert --to notebook --execute --inplace lab4_IC2025.ipynb`.
5. Entregar lab4_IC2025.ipynb en el campus.

## Controles
Referencias históricas TKT-17: 2155 líneas, 51317 unidades, bruto 1354458.59, descuento 88665.83, neto 1265792.76. Se validan los totales reales contra el manifiesto, no se fuerzan las cifras históricas. Los importes y sus derivados quedan fuera de los predictores de cantidad. No se crean nulos artificiales. Se propone árbol de regresión.

## Resultados y validación final
- Extracción real de Oracle: 2.155 filas, 16 columnas, 830 pedidos; 0 nulos y 0 claves de pedido/producto duplicadas.
- Dataset procesado: 2.155 filas, 188 columnas (181 predictores, 6 columnas de auditoría y 1 objetivo), 0 nulos, 0 duplicados, 7 gráficos y 0 errores de ejecución.
- Totales conciliados: 51.317 unidades; bruto 1.354.458,59; descuento 88.665,83; neto 1.265.792,76.
- Atípicos IQR: cantidad 87, precio derivado 98, tasa derivada 20, bruto 163, descuento 314, neto 170. Se conservan los valores válidos.
- Notebook ejecutado íntegramente con la copia local de la extracción original verificada por SHA-256. La conexión HTTP externa no estaba disponible en el entorno de ejecución; por defecto, el notebook lee el commit fijo `59b90ec4a45c9d40731f49990f3df39ece7fcc73` desde GitHub. Para repetir sin red, establecer `LAB4_LOCAL_DIR` al directorio que contiene los dos archivos originales.
- SHA-256 del CSV procesado: `d56bb8d86ee3f0193fc0a6f243b60e8c3cd3ea920caae8708d59953dfeee524d`.
- Entrega académica: `lab4_IC2025.ipynb` (con salidas y gráficos). La carga al campus virtual corresponde al equipo. Confirmar autorización docente para usar el DW en lugar de datos abiertos si aún no se ha confirmado.
