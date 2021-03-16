patterns = {
    "111": "0",
    "110": "1",
    "101": "1",
    "100": "0",
    "011": "1",
    "010": "1",
    "001": "1",
    "000": "0"
}


def step(state):
    next_state = ["0"] * len(state)
    for i in range(0, len(state)):
        curr = ["0"] * 3
        for j in range(-1, 2):
            curr[j + 1] = str(state[(i + j) % len(state)])
        if "".join(curr) in patterns:
            next_state[i] = patterns["".join(curr)]
    return "".join(next_state)


curr_step = "10000101010000100100001001111001011010100101101100"
stop = False

while True:
    if "000000000000000" in curr_step:
        break
    curr_step = step(curr_step)

print(curr_step)