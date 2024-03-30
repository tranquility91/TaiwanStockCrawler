import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def calculate_and_plot_bollinger_bands(df, window=20, num_std=2):
    # 將收盤價轉換為浮點數型別
    df['收盤價'] = df['收盤價'].astype(float)

    # 計算中心線（移動平均線）
    df['MA'] = df['收盤價'].rolling(window=window).mean()

    # 計算上布林帶
    df['Upper'] = df['MA'] + num_std * df['收盤價'].rolling(window=window).std()

    # 計算下布林帶
    df['Lower'] = df['MA'] - num_std * df['收盤價'].rolling(window=window).std()

    # 載入中文字型
    font_path = r'C:\Users\USER\OneDrive\桌面\v_code\18HW\NotoSansCJK-Black.ttc'
    myfont = fm.FontProperties(fname=font_path)

    # 設置圖表大小
    plt.figure(figsize=(12, 6))

    # 設定標題
    plt.title('布林通道', fontproperties=myfont, pad=20)

    # 繪製線圖和布林帶，從第 window 天開始繪製
    plt.plot(df['日期'][window:], df['收盤價'][window:], label='收盤價')
    plt.plot(df['日期'][window:], df['MA'][window:], label='中心線', color='orange')
    plt.plot(df['日期'][window:], df['Upper'][window:], label='上布林帶', color='red', linestyle='--')
    plt.plot(df['日期'][window:], df['Lower'][window:], label='下布林帶', color='green', linestyle='--')

    # 填充布林帶區域
    plt.fill_between(df['日期'][window:], df['Upper'][window:], df['Lower'][window:], color='lightgray', alpha=0.5)

    # 設定圖表其他屬性
    plt.xlabel('日期', fontproperties=myfont)
    plt.ylabel('價格', fontproperties=myfont)
    plt.legend(prop=myfont)
    plt.xticks(rotation=45, fontproperties=myfont)
    plt.grid(True)

    # 顯示圖表
    plt.show()

    return df