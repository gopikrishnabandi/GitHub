#Plot High Prices for IBM
import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df=pd.read_csv("data/IBM.csv")
    count_of_records=df.count[]
    print('Count of Records',count_of_records)
    df['High'].plot()
    plt.xlabel('Index')
    plt.ylabel('High Prices')
    plt.show()
    

if __name__=="__main__":
    test_run()