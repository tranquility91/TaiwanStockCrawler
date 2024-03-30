import grab
import macd
import rsi
import burlin
import matplotlib.pyplot as plt
 
plt.ion()  # 啟用交互模式，即畫圖時不關閉視窗，可以一次顯示多張圖

stock_id = '00881'

# 抓取股票資料
df = grab.grab_stock_data(stock_id)

# 計算並繪製 RSI    
RSI = rsi.calculate_rsi(df)

# 計算並繪製 MACD
df = macd.calculate_macd(df)

# 計算並繪製布林帶
Burlin = burlin.calculate_and_plot_bollinger_bands(df)

plt.show(block=True)# 顯示圖表，並等待使用者關閉視窗