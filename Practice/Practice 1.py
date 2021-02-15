import pandas as pd 

def get_mean_volume(symbol):
    df=pd.read_csv("data/{}.csv".format(symbol))
    return df['Volume'].mean()

def test_run():
    for symbol in ['AAPL','IBM']:
        print('Mean Volume for',symbol)
        print(symbol,round(get_mean_volume(symbol),2))

if __name__=="__main__":
    test_run()