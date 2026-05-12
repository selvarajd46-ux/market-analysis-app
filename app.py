import streamlit as st
import yfinance as yf
import pandas_ta as ta
import pandas as pd

st.set_page_config(page_title="Share Market Option Signals", layout="wide")

st.title("📈 Market Analysis & Option Calls")
st.write("இந்த ஆப் தற்போதைய சந்தையை அனலைஸ் செய்து 'Call' அல்லது 'Put' சிக்னல்களை வழங்கும்.")

symbol = st.text_input("Enter Symbol (e.g., ^NSEI for Nifty, RELIANCE.NS):", "^NSEI")

if st.button("Analyze Market"):
    try:
        # Download daily data for long-term trend (EMA 200)
        daily_data = yf.download(symbol, period="1y", interval="1d", progress=False)
        
        # Download intraday data for momentum (RSI)
        intraday_data = yf.download(symbol, period="5d", interval="15m", progress=False)
        
        if not daily_data.empty and not intraday_data.empty:
            # Calculate indicators on appropriate timeframes
            daily_data['EMA_200'] = ta.ema(daily_data['Close'], length=200)
            intraday_data['RSI'] = ta.rsi(intraday_data['Close'], length=14)
            intraday_data['MACD'] = ta.macd(intraday_data['Close'], fast=12, slow=26, signal=9)['MACD_12_26_9']
            
            # Get latest values
            last_daily = daily_data.iloc[-1]
            last_intraday = intraday_data.iloc[-1]
            
            price = last_intraday['Close']
            rsi_val = last_intraday['RSI']
            macd_val = last_intraday['MACD']
            ema_200 = last_daily['EMA_200']
            
            # Display Stats
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Current Price", f"₹{price:.2f}")
            col2.metric("RSI (14)", f"{rsi_val:.2f}")
            col3.metric("MACD", f"{macd_val:.4f}")
            col4.metric("EMA (200-day)", f"₹{ema_200:.2f}")

            # Enhanced Signal Logic
            st.subheader("📊 Our Analysis:")
            
            # Determine trend
            is_uptrend = price > ema_200
            is_downtrend = price < ema_200
            
            # RSI signals
            is_oversold = rsi_val < 35
            is_overbought = rsi_val > 65
            is_neutral = 35 <= rsi_val <= 65
            
            # MACD signal
            macd_positive = macd_val > 0
            
            signal_strength = 0
            signal_type = None
            
            # BUY CALL Logic (Uptrend + Oversold)
            if is_uptrend and is_oversold and macd_positive:
                signal_strength = 3  # Strong
                signal_type = "CALL"
            elif is_uptrend and is_oversold:
                signal_strength = 2  # Moderate
                signal_type = "CALL"
            elif is_uptrend and is_neutral and macd_positive:
                signal_strength = 1  # Weak
                signal_type = "CALL"
            
            # BUY PUT Logic (Downtrend + Overbought)
            elif is_downtrend and is_overbought and not macd_positive:
                signal_strength = 3  # Strong
                signal_type = "PUT"
            elif is_downtrend and is_overbought:
                signal_strength = 2  # Moderate
                signal_type = "PUT"
            elif is_downtrend and is_neutral and not macd_positive:
                signal_strength = 1  # Weak
                signal_type = "PUT"
            
            # Display signal
            if signal_type == "CALL":
                if signal_strength == 3:
                    st.success("🎯 **STRONG BUY CALL**: Uptrend + Oversold + Positive MACD")
                elif signal_strength == 2:
                    st.success("📈 **BUY CALL**: Uptrend + Oversold")
                else:
                    st.info("💡 **WEAK BUY CALL**: Uptrend with neutral momentum")
                    
            elif signal_type == "PUT":
                if signal_strength == 3:
                    st.error("🎯 **STRONG BUY PUT**: Downtrend + Overbought + Negative MACD")
                elif signal_strength == 2:
                    st.error("📉 **BUY PUT**: Downtrend + Overbought")
                else:
                    st.info("💡 **WEAK BUY PUT**: Downtrend with neutral momentum")
            else:
                st.warning("⚖️ **HOLD/WAIT**: No clear signal at this moment")
            
            # Charts
            st.subheader("📉 Price Charts")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Daily Trend (with EMA 200)**")
                chart_data = daily_data[['Close', 'EMA_200']].tail(100)
                st.line_chart(chart_data)
            
            with col2:
                st.write("**15-min Momentum (RSI)**")
                st.line_chart(intraday_data['RSI'].tail(50))
            
            # Disclaimer
            st.info("⚠️ **Disclaimer**: This is for educational purposes only. Not financial advice. Always do your own research before trading.")
            
        else:
            st.error("Unable to fetch data. Check symbol and try again.")
            
    except Exception as e:
        st.error(f"Error: {str(e)}")