from datetime import datetime
import pandas as pd
from pandas import DataFrame
from pykrx import stock

pd.set_option('display.max_columns', None)
# # 날짜를 조회할떄, 형태를 포멧해줌.
today=datetime.today().strftime("%y%m%d")
# #   get_market_ticker_list 메소드를 이용하여 kospi의 모든 종목의 티커를 list형태로 담아줌
# #  market=옵션을 통해 , 코스피,코스닥의 모든 종목을 가져올수 있음.
ticker_list = stock.get_market_ticker_list(date=today,market="KONEX")
print(len(ticker_list))

# # 각각의 종목을 담아줄 list정의
# symbol_list=[]
# #  for문 통해서, 종목별로 하나씩 가져옴
# for ticker in ticker_list:
#     symbol = stock.get_market_ticker_name(ticker)
#     symbol_list.append(symbol)


# 코스피에 대한 총 종목수 조회를 위해 사이즈를 알아봄
# print(len(symbol_list))


# print(symbol_list)
# print(ticker_list)
# print(len(ticker_list))


# 01
# 모든 코스피종목에 대한 20221026에 대한 티커 정보
#   티커(종목코드) 시가 고가 저가 종가 거래량 거래대금 등락률 get_market_ohlcv_by_ticker
# df = stock.get_market_ohlcv_by_ticker(date="20221026", market="KOSPI")
# print(df.head())

# 02
# 특정 종목에 대한 정보 조회 ticker옵션을 통해, fromdate todate 옵션을 통해 원하는 날짜 범위 지정 가능
# 날짜별), 시가 고가 저가 종가 거래량  get_market_ohlcv_by_date
# df = stock.get_market_ohlcv_by_date(fromdate="20221025", todate="20221030", ticker="095570")
# print(df)

# 03
# 코스피의 모든 종목에 대한 변화되는 값 조회 stock.get_market_price_change_by_ticker
# 티커별) 종목명 시가 종가 변동폭 등락률 거래량 거래대금
# df = stock.get_market_price_change_by_ticker(fromdate="20211027", todate="20221027",market="KOSPI")
# print(df.head())


# 04
# 코스피 지수에 대한 정보 조회 stock.get_index_ohlcv_by_date
# 날짜별 ) 시가 고가 저가 종가 거래량 거래대금
# df = stock.get_index_ohlcv_by_date("20101001", "20201030", "1001")
# print(df.head())



# 주요지수에 대한 코드 조회  ex)1001은 코스피
# df= stock.get_index_ticker_list();
# print(df)
# myframe=DataFrame(df)
# filename='주식.csv'
# myframe.to_csv(filename,encoding='UTF-8',index=False)

