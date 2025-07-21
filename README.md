# Technical Indicators for Taiwanese Stocks  
This project fetches historical stock price data from the TWSE and visualizes three major technical indicators: RSI, MACD, and Bollinger Bands. The workflow is fully modularized into Python scripts and displays the results interactively using `matplotlib`.

## 📁 Files  
main.py — Main script that runs the entire pipeline (data collection, calculation, plotting)  
grab.py — Grabs the latest 5 months of stock data from TWSE open API  
macd.py — Calculates and plots the MACD indicator  
rsi.py — Calculates and plots the RSI indicator  
burlin.py — Calculates and plots Bollinger Bands  
ex_macd.png / ex_rsi.png / ex_布林.png — Example plots (MACD, RSI, Bollinger Band)  
NotoSansCJK-Black.ttc — Font file for displaying Chinese labels in plots  
__pycache__/ — Compiled Python cache directory (auto-generated)  

## 📊 What It Does  
The pipeline:  
- Sends requests to the Taiwan Stock Exchange API to download recent historical data  
- Converts ROC calendar format to Gregorian for correct sorting  
- Calculates RSI (Relative Strength Index), MACD (Moving Average Convergence Divergence), and Bollinger Bands  
- Generates interactive plots with customized Chinese fonts  
- Automatically displays all plots without closing previous ones (`plt.ion()` enabled)  

## 🧾 Dependencies  
You’ll need the following Python packages:  
```python
pandas  
matplotlib  
requests  
datetime  
python-dateutil  
