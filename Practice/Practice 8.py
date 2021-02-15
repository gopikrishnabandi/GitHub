#Utility Function
import os
import pandas as pd 

def symbol_to_path(symbol,base_dir="data"):
    #return csv file path given ticker symbol
    return os.path.join(base_dir,"{}.csv".format(str(symbol)))
    #os.path by default adds /

def get_data(symbols, dates):
    """Read Stock Data (Adj Close) for given symbols from CSV Files"""
    df=pd.DataFrame(index=dates)
    if 'SPY' not in symbols:#add SPY for reference, if absent
        symbols.insert(0,'SPY')

    for symbol in symbols:
        
        dftemp=pd.read_csv(symbol_to_path(symbol),index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
        dftemp=dftemp.rename(columns={'Adj Close':symbol})
        df=df.join(dftemp)
        if symbol=='SPY':
            df=df.dropna(subset=["SPY"])

    return df

def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']  # SPY will be added in get_data()

    # Get stock data
    df = get_data(symbols, dates)

    print(df)
    #ROW SLICING
    print(df['2010-01-22':'2010-01-26'])
    #column slicing
    print(df[['SPY','GOOG']])
    #ROW AND COLUM SLICING
    print(df['2010-01-22':'2010-01-26'],['SPY','IBM'])

if __name__ == "__main__":
    test_run()