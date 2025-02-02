from Brains.Brain import Brain
import numpy as np


class DummyBrain(Brain):
    def __init__(self):
        return

    def get(self, s):
        available = Brain.get_available(s)
        available.append(None)
        chosen_card = available[np.random.choice(len(available))]
        if chosen_card is not None and chosen_card.color is 0:
            chosen_card.color = np.random.choice(range(1, 5))
        return chosen_card

    def add_observation(self, s, a, r, s_, batch_size):
        return

    def learn(self):
        return
