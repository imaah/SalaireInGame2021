from hashlib import sha256

a_range = 5000
house_gap = 10

goal = "ccee0f6b78bba5eff19a89678252a0fcece57d3b80458ceeb41c92bfdfa645ce"

for x in range(-(a_range + house_gap), a_range + house_gap, house_gap):
    y = 0
    mult = -1
    while -a_range <= y <= a_range:

        for day in range(1, 32):

            for month in range(2, 4):
                to_encode = f"{day}/{month}@{x},{y}"
                encoded = sha256(to_encode.encode()).hexdigest()

                if encoded == goal:
                    print(to_encode)
        mult -= 1
        y = x * mult

        if x == y == 0:
            break
