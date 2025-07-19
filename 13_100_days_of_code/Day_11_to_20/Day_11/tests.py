import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

pc= []

for _ in range(2):
    pc.append(random.choice(cards))


while sum(pc) < 17:
    pc.append(random.choice(cards))
    print(pc)

    while sum(pc) > 21 and 11 in pc:
        pc.remove(11)
        pc.append(1)
        



print(pc)
print(sum(pc))