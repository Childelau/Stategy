import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as datetime
from datetime import datetime
import baostock as bs
import os
import warnings;warnings.simplefilter('ignore')
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_colwidth', 1000)
bs.login()

#获取当前文件所在位置
file_path = os.getcwd() + '\\data_file\\'
stocks_init_path = file_path + 'stocks.csv'
stocks_pool_path = file_path + 'stocksPool.csv'
print(file_path)
#当天日期
today = datetime.now().strftime('%Y-%m-%d')
print(today)

#先把股票代码tolist存储到file_path.csv文件中
def stocks_list(date = today):
    stocks = bs.query_all_stock(date)
    stocks_data = stocks.get_data()
    stocks_data['isIndex'] = stocks_data['code'].str.contains('sh.000|sz.399|sh.688')
    stocks_data['isSt'] = stocks_data['code_name'].str.contains('/*ST|ST')

    print('test')
    print(stocks_data.info())

    stocks_data.drop(stocks_data[stocks_data['isIndex']==True].index,inplace=True)
    stocks_data.drop(stocks_data[stocks_data['isSt']==True].index,inplace=True)


    stocks_data.to_csv(stocks_init_path)
    
    print('Downloading:' + code)
        
    
stocks_list()


#去除688，去出板块类型




    
































