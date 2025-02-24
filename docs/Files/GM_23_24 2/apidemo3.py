from pokemontcgsdk import Card
import matplotlib.pyplot as plt

out = Card.where(q='name:charizard')
types = []

for card in out:
    if card.types:
        types += [card.types[0]]

plt.hist(types)
plt.show()