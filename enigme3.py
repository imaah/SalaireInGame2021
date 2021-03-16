import fileinput

drugs = []

for line in fileinput.input("enigme3.txt"):
    drugs.append(line.replace("\n", ""))

occur = {}
searched = []

for i in range(12):
    for drug in drugs:
        if i > len(drug) - 1:
            continue
        if drug[i] in occur.keys():
            occur[drug[i]] += 1
        else:
            occur[drug[i]] = 1

    most_present = None

    for letter in occur.keys():
        if most_present is None or occur[letter] > occur[most_present]:
            most_present = letter

    searched.append(most_present)
    occur = {}

print("".join(searched))
