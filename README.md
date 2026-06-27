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

Los datos provienen de un dataset público de Kaggle con transacciones marcadas como fraude. (Añade aquí el nombre exacto del dataset y el enlace de Kaggle si lo deseas, por ejemplo: `https://www.kaggle.com/` seguido del dataset).

Nota: por razones de licencia/privacidad, el dataset no está incluido en este repositorio. Descarga los datos de Kaggle y coloca el/los archivo(s) CSV en la carpeta `data/`.

## Requisitos

- Python 3.8+
- Jupyter Notebook / JupyterLab
- Dependencias (puedes instalarlas con pip):

```bash
pip install -r requirements.txt
```

Si no existe `requirements.txt`, las librerías mínimas recomendadas son:

- numpy
- pandas
- scikit-learn
- matplotlib
- seaborn
- imbalanced-learn (opcional, para balanceo de clases)
- xgboost o lightgbm (opcional, para modelos de boosting)

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
- src/                 -> Código fuente (preprocesamiento, entrenamiento, utilidades)
- models/              -> Modelos entrenados / checkpoints
- reports/             -> Visualizaciones y reportes
- README.md            -> Este archivo
- requirements.txt     -> Dependencias del proyecto

Ajusta esta estructura según cómo organizaste el repo.

## Uso

- Explora los notebooks en `notebooks/` para ver el flujo de trabajo.
- Usa los scripts en `src/` para ejecutar preprocesamiento o entrenamiento desde línea de comandos. Ejemplo:

```bash
python src/train.py --data data/transactions.csv --output models/model.pkl
```

(Sustituye por los comandos reales que tengas en el proyecto).

## Flujo de trabajo y metodologías

1. Carga y limpieza de datos: manejo de valores faltantes, formatos y tipos.
2. Ingeniería de features: creación de variables temporales, agregados por usuario/cuenta, normalización/estandarización.
3. Balanceo de clases: técnicas como undersampling, oversampling (SMOTE) o ajuste de pesos en el modelo.
4. Selección y entrenamiento de modelos: regresión logística, Random Forest, XGBoost/LightGBM, redes neuronales, etc.
5. Evaluación: validación cruzada, curvas ROC/PR, matriz de confusión, precisión/recall/F1.

## Evaluación y métricas

Para problemas de fraude (clases desbalanceadas) se recomienda usar métricas como:

- AUC-ROC
- Precision-Recall AUC
- Precision, Recall, F1-score (especialmente Recall si priorizas capturar fraudes)
- Matriz de confusión

Incluye validación temporal si los datos están ordenados por tiempo.

## Resultados esperados

En `reports/` deberías encontrar gráficos y tablas con los resultados de los experimentos (por ejemplo: curvas ROC, importancia de features, métricas por modelo).

## Cómo reproducir los experimentos

1. Coloca los datos en `data/`.
2. Ejecuta los notebooks en orden (o scripts) tal como se indica en `notebooks/`.
3. Guarda los artefactos en `models/` y los reportes en `reports/`.

Para automatizar, puedes usar un script `run_experiments.sh` o un Makefile.

## Contribuciones

Si quieres contribuir:

1. Abre un issue describiendo la propuesta o el bug.
2. Crea un branch nuevo para tu trabajo.
3. Envía un pull request con una descripción clara de los cambios.

## Licencia

Añade aquí la licencia del proyecto (por ejemplo, MIT). Si no estás seguro, añade un archivo `LICENSE` con la licencia que prefieras.

## Contacto

Para preguntas o sugerencias, contacta a: carmele9 (puedes añadir tu email aquí si lo deseas).


---

README generado y adaptado para el proyecto AML_Detection_Project. Asegúrate de ajustar enlaces, nombres de archivos y comandos según el contenido real del repositorio.