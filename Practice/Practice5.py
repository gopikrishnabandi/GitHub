import pandas as pd 


def test_run():
    start_date='2010-01-22'
    end_date='2010-01-26'
    dates=pd.date_range(start_date,end_date)
    print(dates) #we get a list of datetime indexes
    print(dates[0])#First DateTimeIndex 
    #Creating an empty dataframe with index as above dates, by default index is 0,1,2..
    df1=pd.DataFrame(index=dates)
    print(df1)#Empty dataframe with index as dates

    #Join SPY(S&P 500) Data to above df1
    #Read SPY Data into a temporary dataframe
    dfSPY=pd.read_csv("data/SPY.csv",index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
    #The above is done so that we can join with df1 whose index is dates,convert dates to datetime objects,get only columns we need,csv has to consider nan values as not a number and not like a string NaN
    
    
    #Join two DataFrames Using DataFrame.join()
    df1=df1.join(dfSPY)
    #By default dataframe does a left join, 
    print(df1)
    #drop nan values
    df1=df1.dropna()
    print(df1)

    #we can write above steps in 1 line, df1=df1.join(dfSPY,how="inner"), so that instead of left matching will only come




if __name__=="__main__":
    test_run()