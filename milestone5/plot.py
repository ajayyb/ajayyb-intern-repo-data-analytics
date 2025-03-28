from matplotlib import pyplot as plt
import seaborn as sns

sns.set_theme(style='darkgrid')

x_values = [1,2,3,4]
y_values = [5,2,7,1]

plt.plot(x_values, y_values)
plt.scatter(x_values, y_values)

plt.plot(x_values, y_values, color = 'black')

plt.title("Practicing Plotting")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()