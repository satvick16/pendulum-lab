import math

file = open("formatted_data.txt", "r")
Lines = file.readlines()

with open("maxes_formatted_data.txt", "w") as f:
    for i in range(len(Lines)-1):
        thing = list(Lines[i].split())

        if abs(float(thing[1])) > abs(float(list(Lines[i-1].split())[1])) and abs(float(thing[1])) > abs(float(list(Lines[i+1].split())[1])):
            f.write(thing[0] + " " + str(abs(float(thing[1]))))
            f.write("\n")

    f.close()

initial_amplitude = 4.7
target_amplitude = 4.7 * (math.e ** (-1 * math.pi / 4))

maxes_file = open("maxes_formatted_data.txt", "r")
maxes = maxes_file.readlines()

for line in maxes:
    thing = line.split()

    if float(thing[1]) <= target_amplitude:
        print(thing[0], thing[1])
        index = maxes.index(line) + 1
        periods = float(index / 3)
        print("number of periods elapsed = ", periods)
        q = periods * 4
        print("Q = ", q)
        break
