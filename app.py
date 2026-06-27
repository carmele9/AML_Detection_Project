import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)
from sklearn.model_selection import train_test_split

# ----------------------------
# CONFIGURACIÓN
# ----------------------------
st.set_page_config(
    page_title="Fraud Detection System",
    layout="wide"
)

pio.templates.default = "plotly_white"

st.title("💳 Fraud Detection Dashboard")

# ----------------------------
# MODELO + DATA
# ----------------------------
model = joblib.load("models/best_model_XGBoost.joblib")

@st.cache_data
def load_data():
    df = pd.read_csv("data/AIML Dataset.csv")
    return df

df = load_data()

# ----------------------------
# OVERVIEW
# ----------------------------
st.sidebar.header("Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total transacciones", len(df))
col2.metric("% Fraude", f"{df['isFraud'].mean()*100:.2f}%")
col3.metric("Variables", df.shape[1])

# ----------------------------
# EDA
# ----------------------------
st.subheader("Exploración de datos")

# Tipos de transacción
type_counts = df["type"].value_counts().reset_index()
type_counts.columns = ["type", "count"]

fig = px.bar(
    type_counts,
    x="type",
    y="count",
    color="type",
    title="Distribución de tipos de transacción",
    color_discrete_sequence=["#584ac3", "#eb8e3e", "#2ca070", "#663871"]
)
st.plotly_chart(fig, use_container_width=True)

# Distribución amount
st.write("Distribución del importe")

option = st.selectbox("Transformación", ["Normal", "Log"])

if option == "Log":
    values = np.log1p(df["amount"])
    title = "Distribución Log(Amount)"
else:
    values = df["amount"]
    title = "Distribución Amount"

fig = px.histogram(
    values,
    nbins=100,
    title=title,
    color_discrete_sequence=["#584ac3"]
)
st.plotly_chart(fig, use_container_width=True)

# Fraude por tipo
fraud_by_type = df.groupby("type")["isFraud"].mean().reset_index()

fig = px.bar(
    fraud_by_type,
    x="type",
    y="isFraud",
    color="type",
    title="Tasa de fraude por tipo de transacción",
    color_discrete_sequence=["#eb8e3e", "#2ca070", "#663871", "#584ac3"]
)
st.plotly_chart(fig, use_container_width=True)

# Evolución temporal
fraud_time = df.groupby("step")["isFraud"].sum().reset_index()

fig = px.line(
    fraud_time,
    x="step",
    y="isFraud",
    title="Evolución del fraude en el tiempo",
    color_discrete_sequence=["#584ac3"]
)
st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# TRAIN / TEST
# ----------------------------
X = df.drop("isFraud", axis=1)
y = df["isFraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    stratify=y,
    random_state=42
)

y_pred = model.predict(X_test)

if hasattr(model, "predict_proba"):
    y_prob = model.predict_proba(X_test)[:, 1]
else:
    y_prob = y_pred

# ----------------------------
# MÉTRICAS
# ----------------------------
st.subheader("Métricas del modelo")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Precision", f"{precision_score(y_test, y_pred):.3f}")
col2.metric("Recall", f"{recall_score(y_test, y_pred):.3f}")
col3.metric("F1", f"{f1_score(y_test, y_pred):.3f}")
col4.metric("ROC-AUC", f"{roc_auc_score(y_test, y_prob):.3f}")

# ----------------------------
# PREDICCIÓN EN TIEMPO REAL
# ----------------------------
st.subheader("Predicción en tiempo real")

amount = st.number_input("Amount", min_value=0.0)
type_tx = st.selectbox("Transaction Type", df["type"].unique())

oldbalanceOrg = st.number_input("Old Balance Origin")
newbalanceOrig = st.number_input("New Balance Origin")
oldbalanceDest = st.number_input("Old Balance Dest")
newbalanceDest = st.number_input("New Balance Dest")

if st.button("Predecir fraude"):

    input_data = pd.DataFrame([[
        amount,
        type_tx,
        oldbalanceOrg,
        newbalanceOrig,
        oldbalanceDest,
        newbalanceDest
    ]], columns=[
        "amount",
        "type",
        "oldbalanceOrg",
        "newbalanceOrig",
        "oldbalanceDest",
        "newbalanceDest"
    ])

    prob = model.predict_proba(input_data)[0][1]

    st.write(f"Probabilidad de fraude: {prob:.4f}")

    if prob < 0.3:
        st.success("APROBADO")
    elif prob < 0.7:
        st.warning("REVISIÓN MANUAL")
    else:
        st.error("BLOQUEADO")

# ----------------------------
# MATRIZ DE CONFUSIÓN (PLOTLY)
# ----------------------------
st.subheader("Matriz de Confusión")

cm = confusion_matrix(y_test, y_pred)

fig = go.Figure(data=go.Heatmap(
    z=cm,
    x=["Pred No Fraude", "Pred Fraude"],
    y=["Real No Fraude", "Real Fraude"],
    colorscale="Blues",
    text=cm,
    texttemplate="%{text}"
))

fig.update_layout(
    title="Matriz de Confusión",
)

st.plotly_chart(fig, use_container_width=True)