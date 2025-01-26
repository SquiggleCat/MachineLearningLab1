import random

class Markov:
    def __init__(self):
        self.state = 'I'
        # keys are current state, values are a list of possible next states
        self.rep = {
            # probabilities are out of 100 so integers can be used
            ' ':[(50, 'A'), (50, 'L')],
            'A':[(40, 'M'), (60, 'L')],
            'M':[(80, ' '), (20, '!')],
            'L':[(100, 'I')],
            'I':[(20, ' '), (25, 'N'), (55, 'V')],
            'V':[(100, 'E')],
            'N':[(100, 'E')],
            'E':[(100, '!')],
            '!':[(70, ' '), (20, 'I'), (10, '!')]
        }
    '''
    Return the current state and follow an arrow to the next state
    '''
    def advance(self):
        current = self.state
        self.state = choose(self.rep[current])
        return current

'''
Given a list of possible states and their respective weights, return one state.
'''
def choose(list):
    # "unzip" the (weight, state) pairs into two lists
    weights, states = zip(*list, strict=True)
    # return a random (weighted) state
    return random.choices(states, weights)[0] # returns a list with 1 element otherwise


if __name__ == '__main__':
    markov = Markov() # set up the Markov chain
    for _ in range(10): # 10 lines
        for __ in range(100): # 100 chars each
            # print the current state, move to the next
            print(markov.advance(), end='')
        print()