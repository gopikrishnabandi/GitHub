import numpy as np
import matplotlib.pyplot as plt

def get_spin_result(win_prob):
	result = False
	if np.random.random() <= win_prob:
		result = True
	return result
def test_code(length):
	win_prob = 9.0/19.0 # set appropriately to the probability of a win
	#np.random.seed(gtid()) # do this only once
	plt.figure()
	plt.axis([0,300,-256,100])
	wins = np.zeros((length, 1000))
	for j in range(length):
		winnings = np.zeros(1000)
		ewin = 0
		i = 0
		while ewin < 80:
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
if __name__== "__main__":
    test_code(1000)