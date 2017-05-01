# Python Bridge Week 1 Assignment 3
# Felipe Campos

a = input("Type number a: ")
b = input("Type number b: ")
artmean = (float(a) + float(b))/2.0
geomean = (float(a)*float(b)) ** 0.5
rmsq = ((float(a) ** 2) * (float(b) ** 2))**0.5

print("Arithmetic Mean: " + str(artmean))
print("Geometric Mean: " + str(geomean))
print("Root-mean-square: " + str(rmsq))
