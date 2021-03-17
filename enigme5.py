base_pv = 100
memory = {}


def turn(smith=base_pv, me=base_pv):
    if smith <= 0:
        return 1
    if me <= 0:
        return 0

    num = 0

    if (smith, me) in memory:
        return memory[(smith, me)]

    for p in ['smith', 'me']:
        for d in [2, 5, 7]:
            if p == 'smith':
                num += turn(smith, me - d)
            else:
                num += turn(smith - d, me)

    memory[(smith, me)] = num
    return num


result = turn()
print(result % 10**9)