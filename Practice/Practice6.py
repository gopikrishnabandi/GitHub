import pandas as pd 

def test_run():
    start_date='2010-01-22'
    end_date='2010-01-26'
    dates=pd.date_range(start_date,end_date)
    df1=pd.DataFrame(index=dates)
    symbols=['SPY','AAPL','GOOG','IBM','GLD']
    for symbol in symbols:
        dfSymbol=pd.read_csv("data/{}.csv".format(symbol),index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
        dfSymbol=dfSymbol.rename(columns={'Adj Close':symbol})
        df1=df1.join(dfSymbol,how="inner")

    print(df1)

if __name__=="__main__":
    test_run()