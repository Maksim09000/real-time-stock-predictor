import streamlit as st
import pandas as pd
import altair as alt

def fetch_predictions(symbol, interval):

    data = {
        "datetime": pd.date_range(start='2025-01-01', periods=20, freq='5T'),
        "price": (100 + pd.Series(range(20))).tolist(),
        "prediction": (100 + pd.Series(range(20)) + 0.5).tolist(),
    }
    df = pd.DataFrame(data)
    return df

def launch_app():
    st.set_page_config(
        page_title="Real-Time Stock Predictor",
        layout="wide",
        initial_sidebar_state="expanded",
        page_icon="📈",
    )

    st.markdown(
        """
        <style>
            /* رنگ پس‌زمینه تاریک کل صفحه */
            body, .main, .block-container {
                background-color: #0e1117;
                color: #cbd5e1;
            }
            /* تغییر رنگ عنوان‌ها */
            h1, h2, h3 {
                color: #00ffe7;
            }
            /* دکمه‌ها */
            div.stButton > button:first-child {
                background: linear-gradient(45deg, #00ffe7, #0077ff);
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px 20px;
                transition: all 0.3s ease;
            }
            div.stButton > button:first-child:hover {
                background: linear-gradient(45deg, #0077ff, #00ffe7);
                box-shadow: 0 0 8px #00ffe7;
            }
            /* ورودی متن */
            input[type="text"], select {
                background-color: #1f2937;
                color: #cbd5e1;
                border: none;
                padding: 8px;
                border-radius: 6px;
            }
            /* جدول */
            .stDataFrame table {
                background-color: #1f2937;
                color: #cbd5e1;
                border-radius: 10px;
                border-collapse: separate;
                border-spacing: 0 10px;
            }
        </style>
        """, unsafe_allow_html=True
    )

    st.title(" Real-Time Stock Predictor")

    st.sidebar.header("Forecast settings")
    symbol = st.sidebar.text_input("Stock symbol", "AAPL", max_chars=5)
    interval = st.sidebar.selectbox("time frame", ["1min", "5min", "15min", "30min", "60min"], index=1)
    st.sidebar.write("---")
    run_button = st.sidebar.button("start")

    if run_button:
        with st.spinner("wating..."):
            df = fetch_predictions(symbol, interval)
            st.success(f"Stock predictions{symbol} with time frame {interval} was prepared!")

            tabs = st.tabs(["📊 Price chart", "📈 Forecast cha", "📋 Data"])

            with tabs[0]:
                st.subheader("ctual Price Chart")
                chart = alt.Chart(df).mark_line(color="#00ffe7", point=True).encode(
                    x='datetime:T',
                    y='price:Q',
                    tooltip=['datetime:T', 'price:Q']
                ).interactive()
                st.altair_chart(chart, use_container_width=True)

            with tabs[1]:
                st.subheader("Prediction chart")
                chart2 = alt.Chart(df).mark_line(color="#0077ff", point=True).encode(
                    x='datetime:T',
                    y='prediction:Q',
                    tooltip=['datetime:T', 'prediction:Q']
                ).interactive()
                st.altair_chart(chart2, use_container_width=True)

            with tabs[2]:
                st.subheader("data")
                st.dataframe(df.style.format({"price": "{:.2f}", "prediction": "{:.2f}"}))

                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="download CSV",
                    data=csv,
                    file_name=f"{symbol}_predictions.csv",
                    mime='text/csv',
                )
    else:
        st.info("parameter")

if __name__ == "__main__":
    launch_app()
