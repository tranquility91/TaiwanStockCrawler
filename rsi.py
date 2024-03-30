import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def calculate_rsi(df):
    df['收盤價'] = df['收盤價'].astype(float)  # 將收盤價轉換為浮點數形式   
    delta = df['收盤價'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    RS = gain / loss
    RSI = 100 - (100 / (1 + RS))
    
    # 載入中文字型
    font_path = r'C:\Users\USER\OneDrive\桌面\v_code\18HW\NotoSansCJK-Black.ttc'
    myfont = fm.FontProperties(fname=font_path)
    
    # 繪製RSI圖
    plt.figure(figsize=(12,6))
    plt.plot(df['日期'], RSI, label='RSI', color='purple')
    plt.title('RSI 指標', fontproperties=myfont)
    plt.ylabel('RSI', fontproperties=myfont)
    plt.xlabel('日期', fontproperties=myfont)
    plt.xticks(rotation=45, fontproperties=myfont)
    plt.legend(prop=myfont)
    plt.grid(True)
    plt.show()
    
    return RSI 