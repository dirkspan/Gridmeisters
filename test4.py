import matplotlib.pyplot as plt

#breedte en lengte
w = 50
h = 50

#pixels
d = 70
plt.figure(figsize=(w, h), dpi=d)

x = [25, 25, 35]
y = [18, 44, 44]

plt.plot(x, y)
plt.savefig("testlines.png")