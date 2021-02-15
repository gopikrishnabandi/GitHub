"""MLT: Utility code.  		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
Copyright 2017, Georgia Tech Research Corporation  		  	   		     		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332-0415  		  	   		     		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		     		  		  		    	 		 		   		 		  
"""  		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
import os  		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
import pandas as pd  
import matplotlib.pyplot as plt		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
# def symbol_to_path(symbol, base_dir=None):  		  	   		     		  		  		    	 		 		   		 		  
#     """Return CSV file path given ticker symbol."""  		  	   		     		  		  		    	 		 		   		 		  
#     if base_dir is None:  		  	   		     		  		  		    	 		 		   		 		  
#         base_dir = os.environ.get("MARKET_DATA_DIR", "../data/")  		  	   		     		  		  		    	 		 		   		 		  
#     return os.path.join(base_dir, "{}.csv".format(str(symbol)))  

def symbol_to_path(symbol,base_dir="data"):
    #return csv file path given ticker symbol
    return os.path.join(base_dir,"{}.csv".format(str(symbol)))
    #os.path by default adds /		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
# def get_data(symbols, dates, addSPY=True, colname="Adj Close"):  		  	   		     		  		  		    	 		 		   		 		  
#     """Read stock data (adjusted close) for given symbols from CSV files."""  		  	   		     		  		  		    	 		 		   		 		  
#     df = pd.DataFrame(index=dates)  		  	   		     		  		  		    	 		 		   		 		  
#     if addSPY and "SPY" not in symbols:  # add SPY for reference, if absent  		  	   		     		  		  		    	 		 		   		 		  
#         symbols = ["SPY"] + list(  		  	   		     		  		  		    	 		 		   		 		  
#             symbols  		  	   		     		  		  		    	 		 		   		 		  
#         )  # handles the case where symbols is np array of 'object'  		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
#     for symbol in symbols:  		  	   		     		  		  		    	 		 		   		 		  
#         df_temp = pd.read_csv(  		  	   		     		  		  		    	 		 		   		 		  
#             symbol_to_path(symbol),  		  	   		     		  		  		    	 		 		   		 		  
#             index_col="Date",  		  	   		     		  		  		    	 		 		   		 		  
#             parse_dates=True,  		  	   		     		  		  		    	 		 		   		 		  
#             usecols=["Date", colname],  		  	   		     		  		  		    	 		 		   		 		  
#             na_values=["nan"],  		  	   		     		  		  		    	 		 		   		 		  
#         )  		  	   		     		  		  		    	 		 		   		 		  
#         df_temp = df_temp.rename(columns={colname: symbol})  		  	   		     		  		  		    	 		 		   		 		  
#         df = df.join(df_temp)  		  	   		     		  		  		    	 		 		   		 		  
#         if symbol == "SPY":  # drop dates SPY did not trade  		  	   		     		  		  		    	 		 		   		 		  
#             df = df.dropna(subset=["SPY"])  		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
#     return df  		  	  

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
  		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):  		  	   		     		  		  		    	 		 		   		 		  
    import matplotlib.pyplot as plt  		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
    """Plot stock prices with a custom title and meaningful axis labels."""  		  	   		     		  		  		    	 		 		   		 		  
    ax = df.plot(title=title, fontsize=12)  		  	   		     		  		  		    	 		 		   		 		  
    ax.set_xlabel(xlabel)  		  	   		     		  		  		    	 		 		   		 		  
    ax.set_ylabel(ylabel)  		  	   		     		  		  		    	 		 		   		 		  
    plt.show()  		

def normalize_data(df):
    return df/df.iloc[0,:]

# def plot_data(df,title='Stock Prices'):
#     df=normalize_data(df)
#     df.plot()
#     ax=df.plot(title=title,fontsize=2)
#     ax.set_xlabel("Date")
#     ax.set_ylabel("Price")
#     plt.show()  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
def get_orders_data_file(basefilename):  		  	   		     		  		  		    	 		 		   		 		  
    return open(  		  	   		     		  		  		    	 		 		   		 		  
        os.path.join(  		  	   		     		  		  		    	 		 		   		 		  
            os.environ.get("ORDERS_DATA_DIR", "orders/"), basefilename  		  	   		     		  		  		    	 		 		   		 		  
        )  		  	   		     		  		  		    	 		 		   		 		  
    )  		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
def get_learner_data_file(basefilename):  		  	   		     		  		  		    	 		 		   		 		  
    return open(  		  	   		     		  		  		    	 		 		   		 		  
        os.path.join(  		  	   		     		  		  		    	 		 		   		 		  
            os.environ.get("LEARNER_DATA_DIR", "Data/"), basefilename  		  	   		     		  		  		    	 		 		   		 		  
        ),  		  	   		     		  		  		    	 		 		   		 		  
        "r",  		  	   		     		  		  		    	 		 		   		 		  
    )  		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
  		  	   		     		  		  		    	 		 		   		 		  
def get_robot_world_file(basefilename):  		  	   		     		  		  		    	 		 		   		 		  
    return open(  		  	   		     		  		  		    	 		 		   		 		  
        os.path.join(  		  	   		     		  		  		    	 		 		   		 		  
            os.environ.get("ROBOT_WORLDS_DIR", "testworlds/"), basefilename  		  	   		     		  		  		    	 		 		   		 		  
        )  		  	   		     		  		  		    	 		 		   		 		  
    )  		  	   		     		  		  		    	 		 		   		 		  
