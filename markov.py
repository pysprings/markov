from collections import defaultdict


class Start:
    pass


class End:
    pass


def train(word_sequence, g):
    states = [Start] + word_sequence + [End]
    state_pairs = zip(states, states[1:])
    for parent, child in state_pairs:
        g[parent].append(child)


def generate(g):
    import random
    result = []
    state = Start
    while state != End:
        result.append(state)
        state = random.choice(g[state])
    return ' '.join(result[1:])


if __name__ == '__main__':
    g = defaultdict(list)
    with open('bee-movie-script.txt') as f:
        for line in f:
            if line.strip():
                train(line.strip().split(), g)
    for _ in range(5):
        print(generate(g))
