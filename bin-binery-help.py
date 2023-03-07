import matplotlib.pyplot as plt
x_vals = [0, 2, 5, 32, 64, 127, 255]
y_vals = [488, 489, 488, 503, 827, 1630, 3260]
plt.figure(figsize=(10, 5))
plt.ylabel('U, мВ')
plt.xlabel('число')
plt.xlim(0, 260)
plt.ylim(450, 3500)
plt.plot(x_vals, y_vals)
plt.show()