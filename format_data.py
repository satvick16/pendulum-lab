import math

file = open("tracker_data.txt", "r")
Lines = file.readlines()

with open("formatted_data.txt", "w") as f:
    for line in Lines:
        thing = list(line.split())
        x_over_len = float((float(thing[1])) / 624.0)
        theta = (math.asin(x_over_len) * 180 / math.pi) - 0.65

        f.write(str(thing[0]) + " " +
                str(theta) + " " + str(1/60/2) + " " + str(0.0997 * theta))
        f.write("\n")
