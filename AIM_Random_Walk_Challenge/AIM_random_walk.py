""" This is a code to simulate the random walk of a mouse in a 3x3 maze """

#packages
import numpy as np

#Dictionary of the cells of the maze and the probability of the mousing moving to the next
state_dict = {'1': np.array([['2', '4'],
                             [.5,.5]]),
              '2': np.array([['1', '3', '5'],
                             [.33333334,.33333333,.33333333]]),
              '3': np.array([['2', '6'],
                             [.5,.5]]),
              '4': np.array([['1', '5', '7'],
                             [.33333334,.33333333,.33333333]]),
              '5': np.array([['2', '4', '6', '8'],
                             [.25,.25,.25,.25]]),
              '6': np.array([['3', '5', '9'],
                             [.33333334,.33333333,.33333333]]),
              '7': np.array([['4', '8'],
                             [.5,.5]]),
              '8': np.array([['7', '5', '9'],
                             [.33333334,.33333333,.33333333]]),
              '9': np.array([['6', '8'],
                             [.5,.5]])}

#Markov - random walking class
class Markov(object):
    """ This class implements the random walk using our state_dict """

    def __init__(self, state_dict):
        self.state_dict = state_dict
        self.state = list(self.state_dict.keys())[0]

    def check_state(self): #Check the current state
        return self.state

    def set_state(self, state): #Set a state manually
        self.state = state
        #print('State is now: %s' % (self.state))

    def next_state(self): #Take a random step
        A = self.state_dict[self.state]
        self.state = np.random.choice(a=list(A[0]), p=list(A[1]))
        #print('New State: %s' % (self.state))


#Experiment Starts here

experiment = Markov(state_dict) #Instance

max_steps = 100 # Arbitrary number to make sure the random walk does not become computationally expensive
number_of_runs = 10000 #Number of experimental runs


for start_position in range(1,10):
    #store the results
    three = 0
    seven = 0
    neither = 0
    
    print ("Starting position - ",start_position, "\n")
    
    for i in range(number_of_runs):
        experiment.set_state(str(start_position))
        #print("\nloop ",i)
        j = 0
        while j <= max_steps:
            j += 1
            state = experiment.check_state()
            #print(state, sep=' ', end='', flush=True) 

            #checking if 3 or 7 is reached, stopping the walk if so
            if state == '3':
                three += 1
                break
            elif state == '7':
                seven += 1
                break
            elif j == max_steps:
                neither += 1
            experiment.next_state()

    print ("Three - ", three)
    print ("Seven - ", seven)
    print ("Neither - ", neither)
    print ("Probability of reaching 3 before 7 = ", round(three * 1.0 / (three + seven + neither),2))
    print ("-----------------------------------------------------------------------")