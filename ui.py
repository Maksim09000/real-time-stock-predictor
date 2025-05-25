import streamlit as st
from data_fetcher import fetch_stock_data
from model_trainer import train_model
from predictor import predict_next
import pandas as pd
import matplotlib.pyplot as plt

def launch_app():
    st.set_page_config(page_title="Real-Time Stock Predictor", layout="wide", initial_sidebar_state="auto")
    st.markdown("""<style>body { background-color: #0e1117; color: white; }</style>""", unsafe_allow_html=True)
    st.title("📈 Real-Time Stock Market Predictor")
    
    symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, MSFT)", "AAPL")
    
    if st.button("Fetch & Predict"):
        df = fetch_stock_data(symbol)
        model = train_model(df)
        latest_row = df.iloc[-1]
        prediction = predict_next(model, latest_row)
        
        st.subheader(f"Predicted Next Close Price: ${prediction:.2f}")
        
        df['Prediction'] = df['4. close'].shift(-1)
        st.line_chart(df[['4. close', 'Prediction']].dropna())
        
        df.to_csv(f"outputs/{symbol}_prediction.csv")
        st.success(f"Saved predictions to outputs/{symbol}_prediction.csv")
