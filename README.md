# AML Detection Project

Este proyecto analiza y predice transacciones fraudulentas usando un dataset público de Kaggle (transacciones marcadas como fraude). Incluye el preprocesamiento de datos, exploración, entrenamiento de modelos y evaluación.

## Tabla de contenidos
- [Descripción](#descripción)
- [Dataset](#dataset)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Flujo de trabajo y metodologías](#flujo-de-trabajo-y-metodologías)
- [Evaluación y métricas](#evaluación-y-métricas)
- [Resultados esperados](#resultados-esperados)
- [Cómo reproducir los experimentos](#cómo-reproducir-los-experimentos)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Descripción

Este repositorio contiene código y notebooks para la detección de transacciones fraudulentas (Anti-Money Laundering / AML) usando técnicas de ciencia de datos y aprendizaje automático. El objetivo es explorar el dataset, crear features relevantes, entrenar modelos supervisados y evaluar su rendimiento para detectar fraudes.

## Dataset

Los datos provienen de un dataset público de Kaggle con transacciones marcadas como fraude https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download.

Nota: por razones de gran tamaño (excede 400 MB), el dataset no está incluido en este repositorio. Descarga los datos de Kaggle y coloca el/los archivo(s) CSV en la carpeta `data/`.

## Requisitos

- Python 3.8+
- Jupyter Notebook / JupyterLab
- Dependencias (puedes instalarlas con pip)

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/carmele9/AML_Detection_Project.git
cd AML_Detection_Project
```

2. Crea y activa un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

## Estructura del proyecto

- data/                -> Carpeta para los datasets (no incluída en el repo)
- notebooks/           -> Notebooks de análisis exploratorio y experimentos
- models/              -> Mejor Modelo entrenado / checkpoints
- app.py               -> Visualizacion y reporte con Streamlit
- README.md            -> Este archivo
- requirements.txt     -> Dependencias del proyecto

## Uso

- Explora los notebooks en `notebooks/` para ver el flujo de trabajo.
- Usa los scripts en `notebooks/` para ejecutar preprocesamiento o entrenamiento. 


## Flujo de trabajo y metodologías

1. Carga y limpieza de datos: manejo de valores faltantes, formatos y tipos.
2. Ingeniería de features: creación de variables, agregados por usuario/cuenta, normalización/estandarización.
3. Selección y entrenamiento de modelos: regresión logística, Random Forest, XGBoost, Gradient Boosting.
5. Evaluación: curvas ROC/PR, matriz de confusión, precisión/recall/F1.

## Evaluación y métricas

Para problemas de fraude (clases desbalanceadas) se recomienda usar métricas como:

- AUC-ROC
- Precision-Recall AUC
- Precision, Recall, F1-score (especialmente Recall si priorizas capturar fraudes)
- Matriz de confusión

## Resultados esperados

En `app.py` deberías encontrar gráficos y tablas con los resultados de los experimentos.

## Cómo reproducir los experimentos

1. Coloca los datos en `data/`.
2. Ejecuta los notebooks en orden (o scripts) tal como se indica en `notebooks/`.
3. Guarda los artefactos en `models/`.

## Contribuciones

Si quieres contribuir:

1. Abre un issue describiendo la propuesta o el bug.
2. Crea un branch nuevo para tu trabajo.
3. Envía un pull request con una descripción clara de los cambios.

## Licencia

Añade aquí la licencia del proyecto (por ejemplo, MIT). Si no estás seguro, añade un archivo `LICENSE` con la licencia que prefieras.
