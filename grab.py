import requests
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta
import time


def grab_stock_data(stock_id):
    df_list = []
    for i in range(5):
        first_day_of_month = dt.date.today().replace(day=1)   # 取得當月第一天日期
        target_date = first_day_of_month - relativedelta(months=i)
        while True:
            if target_date.weekday() < 5:
                date = target_date.strftime("%Y%m%d")
                break
            else:
                target_date -= relativedelta(days=1)

        stock_data = requests.get(f'https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date={date}&stockNo={stock_id}&response=json&_=1711249081625')
        json_data = stock_data.json()
        df = pd.DataFrame(data=json_data['data'], columns=json_data['fields'])
        df_list.append(df)

        time.sleep(10)  # 延遲10秒，避免網站過快拒絕連線

    df = pd.concat(df_list, ignore_index=True)

    # 修改日期格式並添加索引列，台灣證券是民國年，加1911年才是西元年，才可以正確排序
    df['日期'] = df['日期'].str.replace(r'(\d+)/(\d+)/(\d+)', lambda x: str(int(x.group(1)) + 1911) + '-' + x.group(2) + '-' + x.group(3), regex=True)
    df['日期'] = pd.to_datetime(df['日期'])
    df = df.sort_values(by='日期')
    df.reset_index(drop=True, inplace=True)
    df.index += 1

    return df