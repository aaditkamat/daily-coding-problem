```
You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]

One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
```

from random import uniform


def run_markov(start, transition_probabilities, num_steps):
    possible_states = set([x[0] for x in transition_probabilities])
    visits = {state: 0 for state in possible_states}
    for i in range(num_steps):
        num = uniform(0, 1)
        probability_map = list(map(lambda x: (x[1], x[2]), filter(lambda x: x[0] == start, transition_probabilities))) 
        count = 0
        for j in range(len(possible_states)):
            if num <= count + probability_map[j][1]:
                start = probability_map[j][0]
                break
            count += probability_map[j][1]
        visits[start] += 1
    return visits

if __name__ == '__main__':
    transition_probabilities = [
        ('a', 'a', 0.9),
        ('a', 'b', 0.075),
        ('a', 'c', 0.025),
        ('b', 'a', 0.15),
        ('b', 'b', 0.8),
        ('b', 'c', 0.05),
        ('c', 'a', 0.25),
        ('c', 'b', 0.25),
        ('c', 'c', 0.5)
    ]
    print(run_markov('a', transition_probabilities, 5000))
