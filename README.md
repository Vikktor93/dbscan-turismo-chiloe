# Análisis Espacial de Turismo en Chiloé con DBSCAN

Este proyecto utiliza algoritmos de Machine Learning no supervisado (DBSCAN) para identificar *hotspots* turísticos y descubrir patrones espaciales en el Archipiélago de Chiloé, Chile.

## 🎯 Objetivo
Implementar clustering basado en densidad (Density-Based Spatial Clustering of Applications with Noise) para segmentar datos geográficos de turistas. El algoritmo permite identificar formas irregulares de agrupamiento costero y aislar anomalías (outliers), visualizando los resultados mediante animaciones interactivas.

## 🛠️ Tecnologías y Librerías Utilizadas
* **Python 3.14**
* **Scikit-Learn**: Para la implementación del modelo DBSCAN y el uso de la métrica espacial Haversine.
* **Pandas / Numpy**: Para la manipulación, limpieza y estructuración de los datos numéricos.
* **Plotly**: Para generar el mapa interactivo y la animación temporal de los clústeres.
* **SciPy**: Específicamente `scipy.spatial.ConvexHull` para dibujar las áreas sombreadas (bordes) alrededor de los grupos.
* **Jupyter**: Para la fase de experimentación interactiva.

## 🚀 Instalación y Configuración (Usando Miniconda)

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Vikktor93/dbscan-turismo-chiloe.git
   cd dbscan-turismo-chiloe
   ```

2. Crear el entorno virtual con Miniconda utilizando el archivo de configuración:
   ```bash
   conda env create -f environment.yml
   ```

3. Activar el entorno virtual:
   ```bash
   conda activate dbscan-chiloe
   ```

## 🗂️ Estructura del Repositorio
* `/data`: Contiene los datasets (crudos y procesados).
* `/notebooks`: Cuadernos Jupyter con los análisis exploratorios iniciales.
* `/src`: Scripts modulares en Python con la lógica de carga, modelado y visualización.

## 👥 Equipo de Desarrollo
* **Victor Saldivia Vera** - *Desarrollador Principal (Líder Técnico)*
* **Carla Vargas Pacheco** - *Co-Desarrolladora (Visualización y Animación)*