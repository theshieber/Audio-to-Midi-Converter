import math
import csv

innerRadius = .00975/2
outerRadius = .01275/2

K = (1./2.) * math.sqrt(innerRadius ** 2 + outerRadius ** 2)
print K
v = 3700
m = 3.0112

with open('es25_notes_frequency.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:

		noteName = row[0]
		f = float(row[1])

		L = math.sqrt((math.pi * v * K * m ** 2) / (8*f))

		LRound = round(L, 3)

		paddingLen = len(noteName)
		padding = " "
		for i in range(10 - paddingLen):
			padding += " "

		print  padding + row[0] + " : " + str(LRound)