# Workshop 4 · Minería de Datos

Universidad Técnica Nacional, ISW-911. Integrante: Ignacio Araya.

## Dataset

Se conserva la descarga original del consolidado de accidentes de tránsito con víctimas de COSEVI, Costa Rica, período 2020-2025. Contiene 93.699 filas y 21 columnas.

- Fuente oficial [COSEVI](https://datosabiertos.csv.go.cr/datasets/193472/consolidado-de-accidentes-de-transito-con-victimas/).
- Licencia publicada por la fuente [ODC-PDDL](https://opendefinition.org/licenses/odc-pddl/).
- Descarga realizada el 18 de noviembre de 2026.
- El archivo usa separador punto y coma y codificación Windows-1252, aunque su nombre en el portal termina en UTF8.
- SHA-256 de los bytes originales `63cd529d8ec47c3cfc12e372fc70d28c7875fdfca90f3d7fca0ffc3cad291e81`.

## Ejecución

Instala los paquetes de `requirements.txt` y abre `lab4_IC2025.ipynb` en Jupyter, VS Code o Google Colab. Ejecuta todas las celdas en orden. El notebook descarga el CSV de este repositorio público, realiza el EDA y guarda `data_process.csv` en la carpeta de ejecución.

## Entregables y resultados

- `lab4_IC2025.ipynb` contiene el desarrollo documentado y ejecutado, con siete gráficos.
- `data_process.csv` contiene las 93.699 observaciones y 82 columnas numéricas resultantes del EDA, sin nulos finales.
- `datos/accidentes_cosevi_2020_2025.csv` conserva el dataset completo de origen.

El objetivo de clasificación es distinguir accidentes con personas fallecidas o heridas graves de accidentes con solo heridos leves. Se propone un árbol de decisión y se justifica su configuración. La imputación, la conservación de atípicos y la codificación de cada tipo de variable se documentan en el notebook.

Para ejecutarlo localmente, instala las dependencias en tu entorno de Python con `python -m pip install -r requirements.txt`, abre el notebook en VS Code con Jupyter o en otro editor compatible y ejecuta todas las celdas. También puede abrirse en Google Colab. El dataset se lee de un commit fijo de este repositorio público.

El archivo solicitado para subir al campus virtual es `lab4_IC2025.ipynb`.
