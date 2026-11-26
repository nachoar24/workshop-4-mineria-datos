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
4. Abrir lab4_IC2025.ipynb; fijar REF_GIT al commit de la extracción, ejecutar todas las celdas, guardar salidas y publicar data_process.csv. Alternativamente ejecutar `jupyter nbconvert --to notebook --execute --inplace lab4_IC2025.ipynb`.
5. Entregar lab4_IC2025.ipynb en el campus.

## Controles
Referencias históricas TKT-17: 2155 líneas, 51317 unidades, bruto 1354458.59, descuento 88665.83, neto 1265792.76. Se validan los totales reales contra el manifiesto, no se fuerzan las cifras históricas. Los importes y sus derivados quedan fuera de los predictores de cantidad. No se crean nulos artificiales. Se propone árbol de regresión.

## Estado
Código adaptado; pendiente exportar desde una instancia Oracle accesible y ejecutar el notebook. El CSV procesado anterior no corresponde a esta versión y no debe utilizarse para entregar.
