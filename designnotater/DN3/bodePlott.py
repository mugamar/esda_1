import csv
import matplotlib.pyplot as plt

header = []
data = []

filename = "Data/Signal_in_to_out_bode.csv"
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)

    for datapoint in csvreader:

        values = [float(value) for value in datapoint]
        data.append(values)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

freq = [p[0] * 1000 for p in data]
ch1 = [p[1] for p in data]
phase = [p[3] for p in data]

plt.suptitle("Bode plot:")

ax1.grid()
ax2.grid()

plt.xlabel("Frequency [KHz]")
ax1.set_ylabel("Magnitude [dB]")
ax2.set_ylabel("Phase [Deg]")

ax1.plot(freq,ch1)
ax2.plot(freq,phase)

plt.show()