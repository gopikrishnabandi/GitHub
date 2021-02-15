"""Assess a betting strategy. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
Copyright 2018, Georgia Institute of Technology (Georgia Tech) 			  		 			     			  	   		   	  			  	
Atlanta, Georgia 30332 			  		 			     			  	   		   	  			  	
All Rights Reserved 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
Template code for CS 4646/7646 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
Georgia Tech asserts copyright ownership of this template and all derivative 			  		 			     			  	   		   	  			  	
works, including solutions to the projects assigned in this course. Students 			  		 			     			  	   		   	  			  	
and other users of this template code are advised not to share it with others 			  		 			     			  	   		   	  			  	
or to make it available on publicly viewable websites including repositories 			  		 			     			  	   		   	  			  	
such as github and gitlab.  This copyright statement should not be removed 			  		 			     			  	   		   	  			  	
or edited. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
We do grant permission to share solutions privately with non-students such 			  		 			     			  	   		   	  			  	
as potential employers. However, sharing with other current or future 			  		 			     			  	   		   	  			  	
students of CS 7646 is prohibited and subject to being investigated as a 			  		 			     			  	   		   	  			  	
GT honor code violation. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
-----do not edit anything above this line--- 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
Student Name: Tucker Balch (replace with your name) 			  		 			     			  	   		   	  			  	
GT User ID: tb34 (replace with your User ID) 			  		 			     			  	   		   	  			  	
GT ID: 900897987 (replace with your GT ID) 			  		 			     			  	   		   	  			  	
""" 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
import numpy as np 			  		 			     			  	   		   	  			  	
import matplotlib.pyplot as plt 			  		 			     			  	   		   	  			  	
def author(): 			  		 			     			  	   		   	  			  	
        return 'tb34' # replace tb34 with your Georgia Tech username. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
def gtid(): 			  		 			     			  	   		   	  			  	
	return 900897987 # replace with your GT ID number 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
def get_spin_result(win_prob): 			  		 			     			  	   		   	  			  	
	result = False 			  		 			     			  	   		   	  			  	
	if np.random.random() <= win_prob: 			  		 			     			  	   		   	  			  	
		result = True 			  		 			     			  	   		   	  			  	
	return result 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
def test_code(length): 			  		 			     			  	   		   	  			  	
	win_prob = 9.0/19.0 # set appropriately to the probability of a win 			  		 			     			  	   		   	  			  	
	#np.random.seed(gtid()) # do this only once 
	wins = np.zeros((length, 20))
	for j in range(length):
		winnings = np.zeros(20)
		ewin = 0
		i = 0
		while ewin < 5:
			won = False
			bet = 1
			while not won:
				won = get_spin_result(win_prob)
				i = i+1
				if won == True:
					ewin = ewin + bet
					winnings[i] = ewin
				else:
					ewin = ewin - bet
					winnings[i] = ewin
					bet = bet * 2
		winnings[i+1:] = 80
		wins[j, :] = winnings
	print(wins)
	
	
if __name__ == "__main__":
	test_code(3) 
	