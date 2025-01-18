import matplotlib.pyplot as plt
import numpy as np

xpoints = []
ypoints = []

#opening the file
# altertalively use /data/Datav1
with open( "/home/alex/CLionProjects/untitled/Data/outPut.txt" , 'r' ) as file:
    #read by lines
    for line in file:
        # print(line)
        # split by whitespace
        lineArray = line.split()
        # add to array
        xpoints.append(float( lineArray[0]))
        ypoints.append(float (lineArray[1]))

# /home/alex/CLionProjects/untitled/Data/Datav4.txt
coeffs = []
inter = 0
# altertalively use data/Polyv1
with open( "/home/alex/CLionProjects/untitled/Data/Datav4.txt" , 'r' ) as file:
    #read by lines
    for line in file:
        print(line)
        # split by whitespace
        coeffs = line.split()
        #print()
print(coeffs)
xpoints = np.array(xpoints)
ypoints = np.array(ypoints)

# plt.scatter(xpoints, ypoints)
# plt.show()

plt.figure(figsize=(10, 10))  # Set the figure size
#plt.scatter(xpoints, ypoints)
plt.xlabel('X-axis')  # Add x-axis label
plt.ylabel('Y-axis')  # Add y-axis label
plt.title('Data Plot')  # Add a title
#plt.grid(True)  # Add a grid for better readability

# Create a smooth x array for the polynomial
# x_smooth = np.linspace(min(xpoints), max(xpoints), 200)


# Create a smooth x array for the polynomial
num_of_x = 200
x_smooth = np.linspace(min(xpoints), max(xpoints), num_of_x)
# Calculate the y values for the polynomial
y_poly = []
coeffs = [2.81620753e-08, -3.66257507e-05,  3.98234042e-01,  1.53898013e+02]
for x in x_smooth:
    y  = 0;
    pow = 3
    for i in coeffs:
        # print(i)
        y += i * (x ** (pow))
        pow -= 1
    #y_poly.append(y)
y_poly = np.polyval(coeffs, x_smooth)

# Plot original data
plt.scatter(xpoints, ypoints, color='blue', label='Original Data')
# Plot the polynomial
plt.plot(x_smooth, y_poly, color='red', label='3rd Degree Polynomial')

# Save the plot as a PNG file
plt.savefig('images/data_plot.png')
print("Plot saved as 'images/data_plot.png'")
