import random

suits = ['clubs', 'diamonds', 'hearts', 'spades']
ranks = '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',')
cards = [(r,s) for r in ranks for s in suits]
# print(cards)

random.shuffle(cards)
# print(cards)

hand = [cards.pop() for _ in range(5)]
print(hand)

# Comprehension is dezelfde code als hieronder.
# lst = []
# for r in ranks:
#     for s in suits:
#         lst.append(r+s)
