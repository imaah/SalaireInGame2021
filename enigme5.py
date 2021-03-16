from copy import copy
base_pv = 100
memory = {}


def turn(smith=base_pv, me=base_pv, actions=None):
    if actions is None:
        actions = []

    if smith <= 0:
        return 1
    if me <= 0:
        return 0

    num = 0

    if (smith, me) in memory:
        return memory[(smith, me)]

    for p in ['smith', 'me']:
        for d in [2, 5, 7]:

            cur_actions = copy(actions)
            cur_actions.insert(0, p)

            if p == 'smith':
                num += turn(smith, me - d, cur_actions)
            else:
                num += turn(smith - d, me, cur_actions)

    memory[(smith, me)] = num
    return num


print(turn() % 10**9)