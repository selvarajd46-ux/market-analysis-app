# 📈 Share Market Analysis & Option Signals

A Streamlit app that analyzes stock/index data using technical indicators to generate trading signals for Call and Put options.

## Features

✅ **Real-time Market Analysis**
- Analyzes NSE stocks and indices
- Supports any stock symbol (e.g., ^NSEI, RELIANCE.NS, INFY.NS)

✅ **Technical Indicators**
- EMA (200-day) for long-term trend
- RSI (14) for momentum on 15-min candles
- MACD for confirmation

✅ **Signal Generation**
- **BUY CALL**: Uptrend + Oversold conditions
- **BUY PUT**: Downtrend + Overbought conditions
- **HOLD/WAIT**: No clear signal
- Signal strength levels: Strong, Moderate, Weak

✅ **Visual Charts**
- Daily trend chart with EMA 200
- 15-minute RSI momentum chart

## Installation

```bash
pip install -r requirements.txt
```

## Running the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## How to Use

1. Enter a stock symbol (e.g., `^NSEI` for Nifty, `RELIANCE.NS` for Reliance)
2. Click **Analyze Market**
3. View the signals and charts
4. Make informed trading decisions

## Supported Symbols

- **Indices**: `^NSEI` (Nifty 50), `^BSESN` (Sensex)
- **Stocks**: `RELIANCE.NS`, `INFY.NS`, `TCS.NS`, `WIPRO.NS`, etc.
- **Cryptocurrencies**: `BTC-USD`, `ETH-USD`

## Signal Logic

### BUY CALL (Bullish)
- Price > EMA(200) + RSI < 35 + MACD > 0 = **STRONG**
- Price > EMA(200) + RSI < 35 = **MODERATE**
- Price > EMA(200) + Neutral RSI + MACD > 0 = **WEAK**

### BUY PUT (Bearish)
- Price < EMA(200) + RSI > 65 + MACD < 0 = **STRONG**
- Price < EMA(200) + RSI > 65 = **MODERATE**
- Price < EMA(200) + Neutral RSI + MACD < 0 = **WEAK**

## ⚠️ Disclaimer

This app is for **educational purposes only**. It is not financial advice. Always conduct your own research and consult with financial advisors before making trading decisions.

## Technologies Used

- **Streamlit**: Web framework
- **yfinance**: Stock data download
- **pandas-ta**: Technical analysis indicators
- **pandas**: Data manipulation

## License

MIT License - Feel free to use and modify!
