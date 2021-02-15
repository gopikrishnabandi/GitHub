# import pandas as pd 
# import numpy as np


# dates=pd.date_range('01/01/2020',periods=8)
# df=pd.DataFrame(np.random.randn(8,4),index=dates,columns=['A','B','C','D'])
# print(df)
# print(df[1:])
# print(df[:-1])

"""MC1-P2: Optimize a portfolio."""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import scipy.optimize as spo
from util import get_data, plot_data

def f(allocs,normed,sv):
    #normed=prices/prices.values[0]
    alloced=normed.multiply(allocs)
    pos_vals=alloced.multiply(sv)
    port_val=pos_vals.sum(axis=1)
    dr=(port_val/port_val.shift(1))-1
    std_dev=dr.std()
    return std_dev

# This is the function that will be tested by the autograder
# The student must update this code to properly implement the functionality
def optimize_portfolio(sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,1,1), \
    syms=['GOOG','AAPL','GLD','XOM'], gen_plot=False):

    sv=1000000
    rfr=0.0
    sf=252.0

    # Read in adjusted closing prices for given symbols, date range
    dates = pd.date_range(sd, ed)
    prices_all = get_data(syms, dates)  # automatically adds SPY

    prices_all.fillna(method="ffill",inplace=True)
    prices_all.fillna(method="bfill",inplace=True)

    prices = prices_all[syms]  # only portfolio symbols
    prices_SPY = prices_all['SPY']  # only SPY, for comparison later

    # find the allocations for the optimal portfolio
    # note that the values here ARE NOT meant to be correct for a test case
    # allocs = np.asarray([0.2, 0.2, 0.3, 0.3]) # add code here to find the allocations

    n=len(syms)
    guess = 1.0/n
    
    #Generate array allocs for
    a_list=[guess]*n
    allocs=np.asarray(a_list)
    #print 'Allocs:',allocs
    normed=prices/prices.values[0]

    my_bounds=[(0.0,1.0) for i in normed.columns]
    #print "Bounds:", my_bounds

    my_constraints = ({ 'type': 'eq', 'fun': lambda inputs: 1.0 - np.sum(inputs) })

    my_result=spo.minimize(f,allocs,args=(normed,sv,), method='SLSQP', constraints=my_constraints, bounds=my_bounds, options={'disp':True})
    opt_allocs=my_result.x
    opt_sddr=my_result.fun
    #normed=prices/prices.values[0]
    alloced=normed.multiply(opt_allocs)
    pos_vals=alloced.multiply(sv)
    port_val=pos_vals.sum(axis=1)

    cr, adr, sddr, sr = [0.25, 0.001, 0.0005, 2.1] # add code here to compute stats
    dr=(port_val/port_val.shift(1))-1
    cr=(port_val[-1]/port_val[0])-1
    adr=dr.mean()
    sddr=opt_sddr
    a=np.sqrt(sf)
    sr=a*((dr.subtract(rfr)).mean())/sddr

    # Get daily portfolio value
    # port_val = prices_SPY # add code here to compute daily portfolio values
    

    # Compare daily portfolio value with SPY using a normalized plot
    if gen_plot:
        # add code to plot here
	port_val = port_val/port_val[0]
	prices_SPY = prices_SPY/prices_SPY[0]
        df_temp = pd.concat([port_val, prices_SPY], keys=['Portfolio', 'SPY'], axis=1)
	plot_data(df_temp, title="Daily portfolio value and SPY")
        pass

    return opt_allocs, cr, adr, sddr, sr

def test_code():
    # This function WILL NOT be called by the auto grader
    # Do not assume that any variables defined here are available to your function/code
    # It is only here to help you set up and test your code

    # Define input parameters
    # Note that ALL of these values will be set to different values by
    # the autograder!

    start_date = dt.datetime(2008,6,1)
    end_date = dt.datetime(2009,6,1)
    symbols = ['IBM', 'X', 'GLD']

    # Assess the portfolio
    allocations, cr, adr, sddr, sr = optimize_portfolio(sd = start_date, ed = end_date,\
        syms = symbols, \
        gen_plot = False)

    # Print statistics
    print "Start Date:", start_date
    print "End Date:", end_date
    print "Symbols:", symbols
    print "Allocations:", allocations
    print "Sharpe Ratio:", sr
    print "Volatility (stdev of daily returns):", sddr
    print "Average Daily Return:", adr
    print "Cumulative Return:", cr

if __name__ == "__main__":
    # This code WILL NOT be called by the auto grader
    # Do not assume that it will be called
    test_code()





"""Optimize a portfolio 
Python 3.6
CS7646 Project 2
Mike Tong (mtong31)
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import scipy.optimize as spo
from util import get_data, plot_data

def assess_portfolio(
    sd = dt.datetime(2008,1,1), ed = dt.datetime(2009,1,1), \
    syms = ['GOOG','AAPL','GLD','XOM'], \
    allocs=[0.1,0.2,0.3,0.4], \
    sv=1000000, rfr=0.0, sf=252.0, \
    gen_plot=False):
    
    """
    sd = Start date (datetime format)
    ed = End date (datetime format)
    syms = List of symbols
    alllocs = allocation of syms, sums to 1.0
    sv = starting value (dollars)
    rfr = Risk free return
    sf = sampling frequency 
    """
    
    # read in adjusted closing prices for given symbols, date range
    # adding SPY to allocation for calulations and trading days
    dates = pd.date_range(sd.date(), ed.date())
    df_all = get_data(syms, dates)  # automatically adds SPY
    df = df_all[syms] 
    
    # get daily portfolio value    
    df_nrm          = df / df.ix[0,:] 
    allocated       = df_nrm * allocs
    position_values = allocated * sv
    port_value      = position_values.sum(axis = 1)
    # daily returns (y_{t} = x_{t}/x_{t-1} - 1
    d_returns       = port_value.copy() 
    d_returns       = (port_value/port_value.shift(1) - 1)
    d_returns       = d_returns[1:]
    
    # Below are desired output values
    
    # cumulative return (final - initial) - 1
    cr   = port_value[-1] / port_value[0] - 1
    # average daily return
    adr  = d_returns.mean()
    # standard deviation of daily return
    sddr = d_returns.std()
    # sharpe ratio ((Mean - Risk free rate)/Std_dev)
    daily_rfr     = (1.0 - rfr)**(1/252) - 1 #Should this be sampling freq instead of 252? 
    sr            = (d_returns - daily_rfr).mean() / sddr
    sr_annualized = sr * (sf**0.5)
    
    # compare daily portfolio value with SPY using a normalized plot
    if gen_plot:
        df_nrm_SPY = df_all['SPY'] / df_all['SPY'].ix[0,:]
        
        port_value_norm = port_value / port_value.ix[0,:]
        port_vs_SPY = df_nrm_SPY.copy()
        port_vs_SPY = port_vs_SPY.to_frame().join(port_value_norm.to_frame('Portfolio'))
    
        ax_portfolio = port_vs_SPY.plot(title = 'Daily Returns against SPY', grid = True, legend = 'reverse')
        ax_portfolio.set_xlabel('Date')
        ax_portfolio.set_ylabel('Normalized Price')
        plt.show()
    
    # end value
    ev = port_value[-1]
    
    return cr, adr, sddr, sr_annualized, ev


def compute_sddr(alloc, df_norm):
    allocation = df_norm * alloc
    portfolio  = allocation.sum(axis = 1)
    
    #Compute daily returns below
    d_returns       = portfolio.copy() 
    d_returns       = (portfolio / portfolio.shift(1)) - 1
    d_returns.ix[0] = 0
    
    return(d_returns.std())   


# This is the function that will be tested by the autograder
# The student must update this code to properly implement the functionality
def optimize_portfolio(sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,1,1), \
    syms=['GOOG','AAPL','GLD','XOM'], gen_plot=False):
    """Inputs:
           sd       = start date
           ed       = end date
           syms     = ticker symbols
           gen_plot = Boolean to generate a plot
       Output:
           allocs = Allocation
           cr   = cumulative return
           adr  = average daily rate of return
           sddr = standard deviation of daily return
           sr   = sharpe ratio
    """
    dates = pd.date_range(sd, ed)
    prices_all = get_data(syms, dates)  # automatically adds SPY
    prices = prices_all[syms]  

    df_norm = prices / prices.ix[0, :] 
    allocs_i = [1./len(syms)] * len(syms) #Initial conditions for minimizer function
    boundary_c = ([0., 1.],) * len(syms) #Boundary condition for allocation values    
        
    allocs = spo.minimize(compute_sddr, allocs_i, args = (df_norm,), method = 'SLSQP',\
                             options={'disp' : False}, bounds= boundary_c, \
                             constraints = ({'type':'eq', 'fun' : lambda allocs : 1.0 - allocs.sum()})) #Constrain expected output
        
    # find the allocations for the optimal portfolio
    cr, adr, sddr, sr = assess_portfolio(sd, ed, syms, allocs.x, 1, gen_plot = gen_plot)
    
    return allocs.x, cr, adr, sddr, sr

def test_code():
    # This function WILL NOT be called by the auto grader
    # Do not assume that any variables defined here are available to your function/code
    # It is only here to help you set up and test your code

    # Define input parameters
    # Note that ALL of these values will be set to different values by
    # the autograder!

    start_date = dt.datetime(2008,6,1)
    end_date = dt.datetime(2009,6,1)
    symbols = ['IBM', 'X', 'GLD']

    # Assess the portfolio
    allocations, cr, adr, sddr, sr = optimize_portfolio(sd = start_date, ed = end_date,\
        syms = symbols, \
        gen_plot = 1)

    print("Start Date:          ", start_date)
    print("End Date:            ", end_date)
    print("Symbols:             ", symbols)
    print("Allocations:         ", allocations)
    print("Sharpe Ratio:        ", sr)
    print("Volatility:          ", sddr)
    print("Average Daily Return:", adr)
    print("Cumulative Return:   ", cr)

if __name__ == "__main__":

    test_code()