from cProfile import label
import csv
import matplotlib.pyplot as plt

header = []
data = []


filename = "Data/Signal_in_to_out_spectrum.csv"
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)

    for datapoint in csvreader:

        values = [float(value) for value in datapoint]
        data.append(values)

print(header)
print(data[0])
print(data[2])





time = [p[0]/1000 for p in data]
ch1 = [p[1] for p in data]
#ch2 = [p[2] for p in data]

plt.suptitle("Network analyser:")






plt.xlabel("Frequency [KHz]")
plt.ylabel("CH1 [dBV]")
plt.figtext(0.5, -1, "one text and next text", ha="center", fontsize=18, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
plt.grid()


plt.plot(time,ch1)
#plt.plot(time,ch2)

plt.show()



