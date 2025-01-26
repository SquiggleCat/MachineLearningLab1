import random

class Markov:
    def __init__(self):
        self.state = 'I'
        # keys are current state, values are a list of possible next states
        self.rep = {
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
    # probabilities are ints <= 100
    rand = random.randrange(100)
    cumulative_prob = 0
    # check against each possible state and its weight
    for weight, state in list:
        cumulative_prob += weight
        if rand < cumulative_prob: return state

if __name__ == '__main__':
    markov = Markov()
    for _ in range(10):
        for __ in range(100):
            print(markov.advance(), end='')
        print()