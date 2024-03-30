import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def calculate_macd(df):
    df['收盤價'] = df['收盤價'].astype(float)
    short_ema = df['收盤價'].ewm(span=12, adjust=False).mean()
    long_ema = df['收盤價'].ewm(span=26, adjust=False).mean()
    MACD = short_ema - long_ema
    signal = MACD.ewm(span=9, adjust=False).mean()
    MACD_hist = MACD - signal
    df = df.assign(MACD=MACD, DEA=signal, MACD_Hist=MACD_hist)

    # 載入中文字型
    font_path = r'C:\Users\USER\OneDrive\桌面\v_code\18HW\NotoSansCJK-Black.ttc'
    myfont = fm.FontProperties(fname=font_path)

    # 繪製MACD圖
    fig1 = plt.figure(figsize=(12,6))
    plt.plot(df['日期'], MACD, label='MACD', color='blue')
    plt.plot(df['日期'], signal, label='DEA', color='red')
    plt.bar(df['日期'], MACD_hist, label='MACD_Hist', color='green')
    plt.title('MACD 指標', fontproperties=myfont)
    plt.xlabel('日期', fontproperties=myfont)
    plt.ylabel('MACD', fontproperties=myfont)
    plt.xticks(rotation=45, fontproperties=myfont)
    plt.legend(prop=myfont)
    plt.grid(True)
    plt.show()

    return df