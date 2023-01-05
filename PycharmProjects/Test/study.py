"""
# -*- conding: utf-8 -*-

import sympy
import numpy as np 
import matplotlib.pyplot as plt

# Juypter 노트북에서 수학식의 LaTeX 표현을 위해 필요함, 하지만 markdown에서 변환하는 것이 귀찮아서 나는 무시. 
# sympy.init_printing(use_latex='mathjax')

# basic
x, y, z, dx = sympy.symbols("x y z dx")
f = sympy.exp(x) + x*y
print(f)
# function에 2개 이상의 symbol이 있기 때문에, 편미분만 가능합니다. 
print("differentiation: {}, integration of diff: {}".format(
    sympy.diff(f, x), sympy.integrate(sympy.diff(f, x), x)
))

f = (x-2)*x*(x+2)
f_diff = sympy.diff(f, x)
f_diff_diff = sympy.diff(f_diff, x)
print('solution set')
print("-------")
print("solution set: {}".format(sympy.solve(f))) #단 필요에 따라, datatype을 바꾸어주는 것이 필요함 
print("solution set: {}".format(sympy.solve(f_diff)))
print("-------")
'''
- 방정식에 값을 넣어서 계산해줄 때는 subs와 evalf를 사용 
    - subs: 특정 symbol에 값을 넣어줌. 물론 값뿐만 아니라 다른 변수의 조합으로 넣어도 상관없음 
    - evalf: 그 값을 float 결과로 변환
'''
print()
print("diff value by limit")
print("-------")
for a in sympy.solve(f_diff):
    print("a: {}".format(a))
    print(f_diff.subs(x, a).evalf())
    # x를 x+dx로 바꿔주고, dx가 0으로 갈때의 diff 값을 limit를 사용해서 계산하려 한다. 
    diff_by_limit = sympy.limit((f.subs(x, x+dx) - f.subs(x, x))/ (x+dx - x), dx, 0.000001)
    print(diff_by_limit.subs(x, a).evalf())
    print("-------")
    
print("integration")
print(sympy.integrate(f))
print(sympy.integrate(sympy.diff(f)))
"""

"""
def is_factor(a, b):
    if b % a == 0:
        return True
    else:
        return False

print(is_factor(4, 1024))
"""

#for i in range(1, 10, 2):
#  print(i)


"""
def factors(b):
  for i in range(1, b+1):
  
    if b % i == 0:
      print(i)
      
if __name__ == '__main__':
  b = input('Your Number Please: ')
  b = float(b)
  
  if b > 0 and b.is_integer():
    factors(int(b))
  else:
    print('Please enter a positive integer')
"""

"""
def multi_table(a):
  for i in range(1, 11):
    print('{0} x {1} = {2}'.format(a, i, a*i))
    
if __name__ == '__main__':
  a = input('Enter a number: ')
  multi_table(float(a))
"""

#print("{0:.2f}".format(1.2345))
#print((25.5 * 2.54) / 100)
#print(650 * 1.609)


"""
'''
Fraction operations
'''
from fractions import Fraction

def add(a, b):
  print('Result of Addition: {0}'.format(a+b))
  
if __name__ == '__main__':
  a = Fraction(input('Enter first fraction: '))
  b = Fraction(input('Enter second fraction: '))
  op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
  if op == 'Add':
    add(a,b)
"""

"""
'''
Run until exit layout
'''
def fun():
  print('I am in an endless loop')
if __name__ == '__main__':
  while True:
    fun()
    answer = input('Do you want to exit? (y) for yes ')
    if answer == 'y':
      break
"""

"""
'''
Multiplication table printer with
exit power to the user
'''
def multi_table(a):
  for i in range(1, 11):
    print('{0} x {1} = {2}'.format(a, i, a*i))
    
if __name__ == '__main__':
  while True:
    a = input('Enter a number: ')
    multi_table(float(a))
    answer = input('Do you want to exit? (y) for yes ')
    if answer == 'y':
      break
"""

"""
l = [1, 2, 3]
for item in l:
  print(item)
"""

"""
l = [1, 2, 3]
for index, item in enumerate(l):
  print(index, item)
"""  
  
"""  
from mpl_toolkits import mplot3d
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');

plt.show()
"""

"""
'''
# plotting random walk by normal dist. 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d') # Axe3D object

sample_size = 50
x = np.cumsum(np.random.normal(0, 1, sample_size))
y = np.cumsum(np.random.normal(0, 1, sample_size))
z = np.cumsum(np.random.normal(0, 1, sample_size))
ax.plot(x, y, z, alpha=0.6, marker='o')
#plt.savefig('../../assets/images/markdown_img/180612_1225_3dplotting_plotting.svg')
plt.savefig('180612_1225_3dplotting_plotting.svg')
plt.title("ax.plot")
plt.show()
'''

# scattering 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 
'''
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d') # Axe3D object

sample_size = 500
x = np.cumsum(np.random.normal(0, 5, sample_size))
y = np.cumsum(np.random.normal(0, 5, sample_size))
z = np.cumsum(np.random.normal(0, 5, sample_size))
ax.scatter(x, y, z, c = z, s= 20, alpha=0.5, cmap=plt.cm.Greens)
#plt.savefig('../../assets/images/markdown_img/180612_1225_3dplotting_scattering.svg')
plt.savefig('180612_1225_3dplotting_scattering.svg')
plt.title("ax.scatter")
plt.show()
'''

# contour3d
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

fig = plt.figure(figsize=(12, 6))
ax = plt.axes(projection='3d')
ax.contour3D(x, y, z, 20, cmap=plt.cm.rainbow)
ax.view_init(45, 45) #방향 돌려서 보기. 
#plt.savefig('../../assets/images/markdown_img/180612_1225_3dplotting_contour.svg')
plt.savefig('180612_1225_3dplotting_contour.svg')
plt.title("ax.contour3D")
plt.show()  
"""

"""
from pylab import plot, show

x1_numbers = [1, 2, 3]
x2_numbers = [4, 5, 6]
y1_numbers = [2, 4, 6]
y2_numbers = [2, 4, 6]

nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
plot(nyc_temp, marker='o')

plot(x1_numbers, y1_numbers, x2_numbers, y2_numbers)
#plot(x_numbers, y_numbers, marker='o')
#plot(x_numbers, y_numbers, 'o')
show()
"""

"""
from pylab import plot, show, title, xlabel, ylabel, savefig, legend, axis

nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]

axis(xmin=2, xmax=10, ymin=0, ymax = 60)
plot(nyc_temp, marker='o')
print(axis())

title('Average monthly temperature in NYC')
xlabel('Month')
ylabel('Temperature')
legend([2000, 2006, 2012])
savefig('study.svg')
show()
"""

"""
'''
Simple plot using pyplot
'''
import matplotlib.pyplot as plt

def create_graph():
  x_numbers = [1, 2, 3]
  y_numbers = [2, 4, 6]
  plt.plot(x_numbers, y_numbers)
  plt.show()
  
if __name__ == '__main__':
  create_graph()
"""

"""
from pylab import plot, savefig
x = [1, 2, 3]
y = [2, 4, 6]
plot(x, y)
savefig('mygraph.png')
"""

"""
'''
The relationship between gravitational force and
distance between two bodies
'''
import matplotlib.pyplot as plt

# Draw the graph
def draw_graph(x, y):
  plt.plot(x, y, marker='o')
  plt.xlabel('Distance in meters')
  plt.ylabel('Gravitational force in newtons')
  plt.title('Gravitational force and distance')
  plt.show()
  
def generate_F_r():
  # Generate values for r
  r = range(100, 1001, 50)
  # Empty list to store the calculated values of F
  F = []
  # Constant, G
  G = 6.674*(10**-11)
  # Two masses
  m1 = 0.5
  m2 = 1.5
  # Calculate force and add it to the list, F
  for dist in r:
    force = G*(m1*m2)/(dist**2)
    F.append(force)
  # Call the draw_graph function
  draw_graph(r, F)
  
if __name__=='__main__':
  generate_F_r()
"""

"""
'''
Draw the trajectory of a body in projectile motion
'''
from matplotlib import pyplot as plt
import math

def draw_graph(x, y):
  plt.plot(x, y)
  plt.xlabel('x-coordinate')
  plt.ylabel('y-coordinate')
  plt.title('Projectile motion of a ball')
  
'''
Generate equally spaced floating point
numbers between two given values
'''
def frange(start, final, increment):
  numbers = []
  while start < final:
    numbers.append(start)
    start = start + increment
  return numbers  
  
def draw_trajectory(u, theta):
  theta = math.radians(theta)
  g = 9.8
  # Time of flight
  t_flight = 2*u*math.sin(theta)/g
  # Find time intervals
  intervals = frange(0, t_flight, 0.001)  
  # List of x and y coordinates
  x = []
  y = []
  for t in intervals:
    x.append(u*math.cos(theta)*t)
    y.append(u*math.sin(theta)*t - 0.5*g*t*t)
  draw_graph(x, y)

'''  
if __name__ == '__main__':
  try:
    u = float(input('Enter the initial velocity (m/s): '))
    theta = float(input('Enter the angle of projection (degrees): '))
  except ValueError:
    print('You entered an invalid input')
  else:
    draw_trajectory(u, theta)
    plt.show()  
'''

if __name__ == '__main__':
  # List of three different initial velocities
  u_list = [20, 40, 60]
  theta = 45
  for u in u_list:
    draw_trajectory(u, theta)
  # Add a legend and show the graph
  plt.legend(['20', '40', '60'])
  plt.show()  
"""

"""
'''
Quadratic function calculator
'''
# Assume values of x
x_values = [-1, 1, 2, 3, 4, 5]
for x in x_values:
  # Calculate the value of the quadratic function
  y = x**2 + 2*x + 1
  print('x={0} y={1}'.format(x, y))
"""

"""
'''
Example of drawing a horizontal bar chart
'''
import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
  # Number of bars
  num_bars = len(data)
  # This list is the point on the y-axis where each
  # Bar is centered. Here it will be [1, 2, 3...]
  positions = range(1, num_bars+1)
  plt.barh(positions, data, align='center')
  # Set the label of each bar
  plt.yticks(positions, labels)
  plt.xlabel('Steps')
  plt.ylabel('Day')
  plt.title('Number of steps walked')
  # Turns on the grid which may assist in visual estimation
  plt.grid()
  plt.show()
  
if __name__ == '__main__':
  # Number of steps I walked during the past week
  steps = [6534, 7000, 8900, 10786, 3467, 11045, 5095]
  # Corresponding days
  labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
  create_bar_chart(steps, labels)
"""

"""
import matplotlib.pyplot as plt

  
def fibo(n):
  if n == 1:
    return [1]
  if n == 2:
    return [1, 1]
  # n > 2
  a = 1
  b = 1
  # First two members of the series
  series = [a, b]
  for i in range(n):
    c = a + b
    series.append(c)
    a = b
    b = c
  return series

if __name__ == '__main__':
  #x = range(0, 100)
  #for i in x:
  #  plt.plot(fibo(i))
  plt.plot(fibo(100))
  plt.show()
"""

"""
shortlist = [1, 2, 3]
#print(sum(shortlist))
print(len(shortlist))
"""

"""
def calculate_mean(numbers):
  s = sum(numbers)
  N = len(numbers)
  # Calculate the mean
  mean = s/N
  return mean

if __name__ == '__main__':
  donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
  mean = calculate_mean(donations)
  N = len(donations)
  print('Mean donation over the last {0} days is {1}'.format(N, mean))
"""

"""  
samplelist = [4, 1, 3]
samplelist.sort()
print(samplelist)
"""

"""
'''
Calculating the median
'''
def calculate_median(numbers):
  N = len(numbers)
  numbers.sort()
  # Find the median
  if N % 2 == 0:
    # if N is even
    m1 = N/2
    m2 = (N/2) + 1
    # Convert to integer, match position
    m1 = int(m1) - 1
    m2 = int(m2) - 1
    median = (numbers[m1] + numbers[m2])/2
  else:
    m = (N+1)/2
    # Convert to integer, match position
    m = int(m) - 1
    median = numbers[m]
  return median
  
if __name__ == '__main__':
  donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
  median = calculate_median(donations)
  N = len(donations)
  print('Median donation over the last {0} days is {1}'.format(N, median))
"""

"""
#  Finding the Most Common Elements
from collections import Counter
simplelist = [4, 2, 1, 3, 4]
c = Counter(simplelist)
print(c.most_common())
print(c.most_common(1))
print(c.most_common(2))

mode = c.most_common(1)
print(mode)
print(mode[0])
print(mode[0][0])
print(mode[0][1])
"""

"""
'''
Calculating the mode
'''
from collections import Counter
def calculate_mode(numbers):
  c = Counter(numbers)
  mode = c.most_common(1)
  return mode[0][0]
  
if __name__=='__main__':
  scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
  mode = calculate_mode(scores)
  print('The mode of the list of numbers is: {0}'.format(mode))
"""

"""
'''
Calculating the mode when the list of numbers may
have multiple modes
'''
from collections import Counter
def calculate_mode(numbers):
  c = Counter(numbers)
  numbers_freq = c.most_common()
  max_count = numbers_freq[0][1]
  modes = []
  for num in numbers_freq:
    if num[1] == max_count:
      modes.append(num[0])
  return modes
  
if __name__ == '__main__':
  scores = [5, 5, 5, 4, 4, 4, 9, 1, 3]
  modes = calculate_mode(scores)
  print('The mode(s) of the list of numbers are:')
  for mode in modes:
    print(mode)
"""

"""
'''
Frequency table for a list of numbers
'''
from collections import Counter
def frequency_table(numbers):
  table = Counter(numbers)
  print('Number\tFrequency')
  for number in table.most_common():
    print('{0}\t{1}'.format(number[0], number[1]))
    
if __name__=='__main__':
  scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
  frequency_table(scores)
"""

"""
'''
Frequency table for a list of numbers
Enhanced to display the table sorted by the numbers
'''
from collections import Counter
def frequency_table(numbers):
  table = Counter(numbers)
  numbers_freq = table.most_common()
  numbers_freq.sort()
  print('Number\tFrequency')
  for number in numbers_freq:
    print('{0}\t{1}'.format(number[0], number[1]))

if __name__ == '__main__':
  scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
  frequency_table(scores)
"""

"""
'''
Find the range
'''
def find_range(numbers):
  lowest = min(numbers)
  highest = max(numbers)
  # Find the range
  r = highest-lowest
  return lowest, highest, r
  
if __name__ == '__main__':
  donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
  lowest, highest, r = find_range(donations)
  print('Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highest, r))  
"""

"""
'''
Find the variance and standard deviation of a list of numbers
from matplotlib import pyplot as plt
'''
import matplotlib.pyplot as plt

def calculate_mean(numbers):
  s = sum(numbers)
  N = len(numbers)
  # Calculate the mean
  mean = s/N
  return mean
  
def find_differences(numbers):
  # Find the mean
  mean = calculate_mean(numbers)
  # Find the differences from the mean
  diff = [] 
  for num in numbers:
    diff.append(num-mean)
  return diff
  
def calculate_variance(numbers):
  # Find the list of differences
  diff = find_differences(numbers)
  # Find the squared differences
  squared_diff = []
  for d in diff:
    squared_diff.append(d**2)
  # Find the variance
  sum_squared_diff = sum(squared_diff)
  variance = sum_squared_diff/len(numbers)
  return variance
  
if __name__ == '__main__':
  donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
  variance = calculate_variance(donations)
  print('The variance of the list of numbers is {0}'.format(variance))
  std = variance**0.5
  print('The standard deviation of the list of numbers is {0}'.format(std)) 
  plt.plot(donations, marker='x')
  plt.show()
"""

"""
simple_list1 = [1, 2, 3]
simple_list2 = [4, 5, 6]
for x, y in zip(simple_list1, simple_list2):
  print(x, y)
""" 

"""
def find_corr_x_y(x,y):
  n = len(x)
  # Find the sum of the products
  prod = []
  for xi,yi in zip(x,y):
    prod.append(xi*yi)
  sum_prod_x_y = sum(prod)
  sum_x = sum(x)
  sum_y = sum(y)
  squared_sum_x = sum_x**2
  squared_sum_y = sum_y**2
  x_square = []
  for xi in x:
    x_square.append(xi**2)
  # Find the sum
  x_square_sum = sum(x_square)
  y_square=[]
  for yi in y:
    y_square.append(yi**2)
  # Find the sum
  y_square_sum = sum(y_square)
  # Use formula to calculate correlation
  numerator = n*sum_prod_x_y - sum_x*sum_y
  denominator_term1 = n*x_square_sum - squared_sum_x
  denominator_term2 = n*y_square_sum - squared_sum_y
  denominator = (denominator_term1*denominator_term2)**0.5
  correlation = numerator/denominator
  return correlation 
  
# Find the sum of numbers stored in a file
def sum_data(filename):
  s = 0
  with open(filename) as f:
    for line in f:
      s = s + float(line)
  print('Sum of the numbers: {0}'.format(s))
  
if __name__ == '__main__':
  sum_data('mydata.txt')  
"""  

"""
'''
Calculating the mean of numbers stored in a file
'''
def read_data(filename):
  numbers = []
  with open(filename) as f:
    for line in f:
      numbers.append(float(line))
  return numbers
  
def calculate_mean(numbers):
  s = sum(numbers)
  N = len(numbers)
  mean = s/N
  return mean
  
if __name__ == '__main__':
  data = read_data('mydata.txt')
  mean = calculate_mean(data)
  print('Mean: {0}'.format(mean))  
"""  
  
""" 
import csv
import matplotlib.pyplot as plt

def scatter_plot(x, y):
  plt.scatter(x, y)
  plt.xlabel('Number')
  plt.ylabel('Square')
  plt.show()
  
def read_csv(filename):
  numbers = []
  squared = []
  with open(filename) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
      numbers.append(int(row[0]))
      squared.append(int(row[1]))
    return numbers, squared
    
if __name__ == '__main__':
  numbers, squared = read_csv('numbers.csv')
  scatter_plot(numbers, squared)  
"""

"""
import matplotlib.pyplot as plt
import csv

def read_csv(filename):
  with open(filename) as f:
    reader = csv.reader(f)
    next(reader)
    summer = []
    highest_correlated = []
    for row in reader:
      summer.append(float(row[1]))
      highest_correlated.append(float(row[2]))
  return summer, highest_correlated
  
if __name__ == '__main__':
  summer, highest_correlated = read_csv('correlate-summer.csv')
  corr = find_corr_x_y(summer, highest_correlated)
  print('Highest correlation: {0}'.format(corr))
  scatter_plot(summer, highest_correlated)
"""

#x = 1
#print(x + x + 1)

"""
from sympy import Symbol
a = Symbol('x')
print(a + a + 1)
print(a.name)
"""

"""
from sympy import symbols, expand
x,y,z = symbols('x,y,z')
s = x*y + x*y
p1 = x*(x + x)
p2 = (x + 2)*(x + 3)
print(s)
print(p1)
print(p2)
print(expand(p2))
"""

"""
from sympy import symbols, factor, expand, pprint, init_printing
init_printing(order='rev-lex')
x,y,z = symbols('x,y,z')
expr = x**2 - y**2
#expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
#expr = x + y + x*y
factors = factor(expr)
pprint(factors)
expands = expand(factors)
pprint(expands)
"""

"""
'''
Print the series:
x + x**2 + x**3 + ... + x**n
____ _____ _____
2 3 n
'''
from sympy import Symbol, pprint, init_printing
def print_series(n):
  # Initialize printing system with reverse order
  init_printing(order='rev-lex')
  #init_printing()
  x = Symbol('x')
  series = x
  for i in range(2, n+1):
    series = series + (x**i)/i
  pprint(series)
  
if __name__ == '__main__':
  n = input('Enter the number of terms you want in the series: ')
  print_series(int(n))
"""

"""
from sympy import symbols

x, y = symbols("x y")
expr = x*x + x*y + x*y + y*y
#res = expr.subs({x:1, y:2})
res = expr.subs({x:1-y})
print(res)
"""

"""
sampledict = {"key1": 5, "key2": 20}
print(sampledict["key1"])
"""

"""
from sympy import symbols, simplify
x, y = symbols("x y")
expr = x*x + x*y + x*y + y*y
expr_subs = expr.subs({x:1-y})
print(simplify(expr_subs))
"""

"""
'''
Print the series:
x + x**2 + x**3 + ... + x**n
____ _____ _____
2 3 n
'''
from sympy import Symbol, pprint, init_printing
def print_series(n, x_value):
  # Initialize printing system with reverse order
  init_printing(order='rev-lex')
  x = Symbol('x')
  series = x
  for i in range(2, n+1):
    series = series + (x**i)/i
  pprint(series)
  # Evaluate the series at x_value
  series_value = series.subs({x:x_value})
  print('Value of the series at {0}: {1}'.format(x_value, series_value))
  
if __name__ == '__main__':
  n = input('Enter the number of terms you want in the series: ')
  x_value = input('Enter the value of x at which you want to evaluate the series: ')
  print_series(int(n), float(x_value))
"""

"""
from sympy import sympify
expr = input('Enter a mathematical expression: ')
expr = sympify(expr)
#print(2*expr)
print(expr)
"""

"""
from sympy import sympify
from sympy.core.sympify import SympifyError
expr = input('Enter a mathematical expression: ')

try:
  expr = sympify(expr)
  print(expr)
except SympifyError:
  print('Invalid input')
"""

"""
'''
Product of two expressions
'''
from sympy import expand, sympify
from sympy.core.sympify import SympifyError
def product(expr1, expr2):
  prod = expand(expr1*expr2)
  print(prod)
  
if __name__=='__main__':
  expr1 = input('Enter the first expression: ')
  expr2 = input('Enter the second expression: ')
  try:
    expr1 = sympify(expr1)
    expr2 = sympify(expr2)
  except SympifyError:
    print('Invalid input')
  else:
    product(expr1, expr2)
"""

"""
from sympy import Symbol, solve
x = Symbol('x')
expr = x - 5 - 7
print(solve(expr))
"""

"""
from sympy import Symbol, solve
x = Symbol('x')
#expr = x**2 + 5*x + 4
expr = x**2 + x + 1
#print(solve(expr, dict=True))
print(solve(expr))
"""

"""
from sympy import symbols, solve

x, a, b, c = symbols("x a b c")
expr = a*x**2 + b*x + c
print(solve(expr, x, dict=True))
"""

"""
from sympy import Symbol, solve, pprint
s = Symbol('s')
u = Symbol('u')
t = Symbol('t')
a = Symbol('a')
expr = u*t + (1/2)*a*t*t - s
t_expr = solve(expr,t, dict=True)
#pprint(t_expr)
print(t_expr)
"""

"""
from sympy import Symbol, solve
x = Symbol('x')
y = Symbol('y')
expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y - 12
#expr3 = solve((expr1, expr2), dict=True)
#print(expr3)
#print(solve((expr1, expr2), dict=True))

soln = solve((expr1, expr2), dict=True)
soln = soln[0]
print(expr1.subs({x:soln[x], y:soln[y]}))
print(expr2.subs({x:soln[x], y:soln[y]}))
"""

"""
from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
#plot(2*x+3)
#plot((2*x + 3), (x, -5, 5))
#plot(2*x + 3, (x, -5, 5), title='A Line', xlabel='x', ylabel='2x+3')
#p = plot(2*x + 3, (x, -5, 5), title='A Line', xlabel='x', ylabel='2x+3', show=False)
#p.save('line.png')
"""

"""
from sympy import Symbol, simplify, solve
expr = input('Enter an expression: ')
expr1 = simplify(expr)
y = Symbol('y')
expr2 = solve(expr1, y)
print(expr2)
solutions = solve(expr1, 'y')
expr_y = solutions[0]
print(expr_y)
"""


"""
'''
Plot the graph of an input expression
'''
from sympy import Symbol, sympify, solve
from sympy.plotting import plot
def plot_expression(expr):
  y = Symbol('y')
  solutions = solve(expr, y)
  expr_y = solutions[0]
  plot(expr_y)
  
if __name__=='__main__':
  expr = input('Enter your expression in terms of x and y: ')
  try:
    expr = sympify(expr)
  except SympifyError:
    print('Invalid input')
  else:
    plot_expression(expr)
"""

"""
from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
plot(2*x+3, 3*x+1)    
"""

"""
from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
p = plot(2*x+3, 3*x+1, legend=True, show=False)
p[0].line_color = 'b'
p[1].line_color = 'r'
p.show()
"""


"""
from sympy import Poly, Symbol, solve_poly_inequality, plot
x = Symbol('x')
ineq_obj = -x**2 + 4 < 0
expr = -x**2 + 4
lhs = ineq_obj.lhs
p = Poly(lhs, x)
rel = ineq_obj.rel_op
print(solve_poly_inequality(p, rel))    
plot(expr)
"""

"""
from sympy import Symbol, solve, solve_univariate_inequality, sin, plot
x = Symbol('x')
ineq_obj = sin(x) - 0.6 > 0
expr = sin(x) - 0.6
print(solve_univariate_inequality(ineq_obj, x, relational=False))
plot(expr)
"""

"""
from sympy import Symbol, sin, sympify
x = Symbol('x')
#expr = x**2 - 4
#expr = 2*sin(x) + 3
#print(expr.is_polynomial())
#expr = (2+x)/(3+x)
#expr = 2+x
#expr = 2+sin(x)
#print(expr.is_rational_function())
expr = sympify('x+3>0')
print(expr)
"""

"""
from sympy import FiniteSet
s = FiniteSet(2, 4, 6)
print(s)
"""

"""
from sympy import FiniteSet
from fractions import Fraction
#s = FiniteSet(1, 1.5, Fraction(1, 5))
#s = FiniteSet(1, 1.5, 3)
#s = FiniteSet()
members = [1, 2, 3]
s = FiniteSet(*members)
for member in s:
  print(member)
#print(s)
#print(len(s))
#print(3 in s)
"""

"""
from sympy import FiniteSet
s = FiniteSet(3, 4, 5)
t = FiniteSet(5, 4, 3)
print(s == t)
"""

"""
from sympy import FiniteSet
s = FiniteSet(1)
t = FiniteSet(1,2)
print(s.is_subset(t))
"""

"""
from sympy import FiniteSet
s = FiniteSet(1, 2, 3)
ps = s.powerset()
print(ps)
print(len(ps))
"""

"""
from sympy import FiniteSet
s = FiniteSet(1, 2, 3)
#t = FiniteSet(1, 2, 3)
t = FiniteSet(1, 2, 3, 4)
#print(s.is_proper_subset(t))
#print(t.is_proper_subset(s))
#print(t.is_proper_superset(s))
#print(s.is_subset(t))
"""

"""
from sympy import FiniteSet
s = FiniteSet(1, 2, 3)
t = FiniteSet(2, 4, 6)
u = FiniteSet(3, 5, 7)
#print(s.union(t))
#print(s.intersect(t))
#print(s.union(t).union(u))
print(s.union(t).intersect(u))
"""

"""
from sympy import FiniteSet
s = FiniteSet(1, 2)
t = FiniteSet(3, 4)
p = s*t
print(p)
for elem in p:
  print(elem)
print(len(p) == len(s)*len(t))
"""

"""
from sympy import FiniteSet
s = FiniteSet(1, 2)
p = s**3
print(p)
for elem in p:
  print(elem)
"""

"""
from sympy import FiniteSet, pi
def time_period(length):
  g = 9.8
  T = 2*pi*(length/g)**0.5
  return T
  
if __name__ == '__main__':
  L = FiniteSet(15, 18, 21, 22.5, 25)
  for l in L:
    t = time_period(l/100)
    print('Length: {0} cm Time Period: {1:.3f} s'. format(float(l), float(t)))
"""


"""
from sympy import FiniteSet, pi
def time_period(length, g):
  T = 2*pi*(length/g)**0.5
  return T
  
if __name__ == '__main__':
  L = FiniteSet(15, 18, 21, 22.5, 25)
  g_values = FiniteSet(9.8, 9.78, 9.83)
  print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)', 'Gravity(m/s^2)', 'Time Period(s)'))
  for elem in L*g_values:
    l = elem[0]
    g = elem[1]
    t = time_period(l/100, g)
    print('{0:^15}{1:^15}{2:^15.3f}'.format(float(l), float(g), float(t)))
"""

"""
from sympy import FiniteSet
def probability(space, event):
  return len(event)/len(space)
  
def check_prime(number):
  if number != 1:
    for factor in range(2, number):
      if number % factor == 0:
        return False
  else:
    return False
  return True
  
if __name__ == '__main__':
  space = FiniteSet(*range(1, 21))
  primes = []
  for num in space:
    if check_prime(num):
      primes.append(num)
    event= FiniteSet(*primes)
  p = probability(space, event)
  print('Sample space: {0}'.format(space))
  print('Event: {0}'.format(event))
  print('Probability of rolling a prime: {0:.5f}'.format(p))
"""

"""
import random
print(random.randint(1, 6))
"""

"""
'''
Roll a die until the total score is 20
'''
import matplotlib.pyplot as plt
import random
target_score = 20
def roll():
  return random.randint(1, 6)
  
if __name__ == '__main__':
  score = 0
  num_rolls = 0
  while score < target_score:
    die_roll = roll()
    num_rolls += 1
    print('Rolled: {0}'.format(die_roll))
    score += die_roll
  print('Score of {0} reached in {1} rolls'.format(score, num_rolls))
"""

"""
from sympy import FiniteSet
import random
def find_prob(target_score, max_rolls):
  die_sides = FiniteSet(1, 2, 3, 4, 5, 6)
  # Sample space
  s = die_sides**max_rolls
  # Find the event set
  if max_rolls > 1:
    success_rolls = []
    for elem in s:
      if sum(elem) >= target_score:
        success_rolls.append(elem)
  else:
    if target_score > 6:
      success_rolls = []
    else:
      success_rolls = []
      for roll in die_sides:
        if roll >= target_score:
          success_rolls.append(roll)
  e = FiniteSet(*success_rolls)
  # Calculate the probability of reaching target score
  return len(e)/len(s)
  
if __name__ == '__main__':
  target_score = int(input('Enter the target score: '))
  max_rolls = int(input('Enter the maximum number of rolls allowed: '))
  p = find_prob(target_score, max_rolls)
  print('Probability: {0:.5f}'.format(p))
"""  
  
"""  
'''
Draw a Venn diagram for two sets
'''
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet

def draw_venn(sets):
  venn2(subsets=sets)
  #venn2(subsets=(a,b), set_labels=('S', 'T'))
  plt.show()

if __name__ == '__main__':
  s1 = FiniteSet(1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
  s2 = FiniteSet(2, 3, 5, 7, 11, 13, 17, 19)
  draw_venn([s1, s2])
"""

"""
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [1, 2, 3]
plt.plot(x, y)
plt.show()
"""

"""
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [1, 2, 3]
fig = plt.figure()
ax = plt.axes()
plt.plot(x, y)
plt.show()
"""    

"""
'''
Example of using matplotlib's Circle patch
'''
import matplotlib.pyplot as plt

def create_circle():
  circle = plt.Circle((0, 0), radius = 0.5)
  return circle
  
def show_shape(patch):
  ax = plt.gca()
  ax.add_patch(patch)
  plt.axis('scaled')
  plt.show()
  
if __name__ == '__main__':
  c = create_circle()
  show_shape(c)
"""

"""
'''
A growing circle
'''
from matplotlib import pyplot as plt
from matplotlib import animation

def create_circle():
  circle = plt.Circle((0, 0), 0.05)
  return circle
  
def update_radius(i, circle):
  circle.radius = i*0.5
  return circle,
  
def create_animation():
  fig = plt.gcf()
  ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
  ax.set_aspect('equal')
  circle = create_circle()
  ax.add_patch(circle)
  anim = animation.FuncAnimation(
    fig, update_radius, fargs = (circle,), frames=30, interval=50)
  plt.title('Simple Circle Animation')
  plt.show()

if __name__ == '__main__':
  create_animation()
"""

"""
'''
Animate the trajectory of an object in projectile motion
'''
from matplotlib import pyplot as plt
from matplotlib import animation
import math

g = 9.8

def get_intervals(u, theta):
  t_flight = 2*u*math.sin(theta)/g
  intervals = []
  start = 0
  interval = 0.005
  while start < t_flight:
    intervals.append(start)
    start = start + interval
  return intervals
  
def update_position(i, circle, intervals, u, theta):
  t = intervals[i]
  x = u*math.cos(theta)*t
  y = u*math.sin(theta)*t - 0.5*g*t*t
  circle.center = x, y
  return circle,
  
def create_animation(u, theta):
  intervals = get_intervals(u, theta)
  xmin = 0
  xmax = u*math.cos(theta)*intervals[-1]
  ymin = 0
  t_max = u*math.sin(theta)/g
  ymax = u*math.sin(theta)*t_max - 0.5*g*t_max**2
  fig = plt.gcf()
  ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
  circle = plt.Circle((xmin, ymin), 1.0)
  ax.add_patch(circle)
  anim = animation.FuncAnimation(fig, update_position,
    fargs=(circle, intervals, u, theta),
    frames=len(intervals), interval=1,
    repeat=False)
  plt.title('Projectile Motion')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.show()
  
if __name__ == '__main__':
  try:
    u = float(input('Enter the initial velocity (m/s): '))
    theta = float(input('Enter the angle of projection (degrees): '))
  except ValueError:
    print('You entered an invalid input')
  else:
    theta = math.radians(theta)
    create_animation(u, theta)
"""

"""
'''
Example of selecting a transformation from two equally probable
transformations
'''
import matplotlib.pyplot as plt
import random

def transformation_1(p):
  x = p[0]
  y = p[1]
  return x + 1, y - 1
  
def transformation_2(p):
  x = p[0]
  y = p[1]
  return x + 1, y + 1
  
def transform(p):
  # List of transformation functions
  transformations = [transformation_1, transformation_2]
  # Pick a random transformation function and call it
  t = random.choice(transformations)
  x, y = t(p)
  return x, y
  
def build_trajectory(p, n):
  x = [p[0]]
  y = [p[1]]
  for i in range(n):
    p = transform(p)
    x.append(p[0])
    y.append(p[1])
  return x, y
  
if __name__ == '__main__':
  # Initial point
  p = (1, 1)
  n = int(input('Enter the number of iterations: '))
  x, y = build_trajectory(p, n)
  # Plot
  plt.plot(x, y)
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.show()
"""

"""
'''
Draw a Barnsley Fern
'''
import random
import matplotlib.pyplot as plt

def transformation_1(p):
  x = p[0]
  y = p[1]
  x1 = 0.85*x + 0.04*y
  y1 = -0.04*x + 0.85*y + 1.6
  return x1, y1
  
def transformation_2(p):
  x = p[0]
  y = p[1]
  x1 = 0.2*x - 0.26*y
  y1 = 0.23*x + 0.22*y + 1.6
  return x1, y1
  
def transformation_3(p):
  x = p[0]
  y = p[1]
  x1 = -0.15*x + 0.28*y
  y1 = 0.26*x + 0.24*y + 0.44
  return x1, y1
  
def transformation_4(p):
  x = p[0]
  y = p[1]
  x1 = 0
  y1 = 0.16*y
  return x1, y1

def get_index(probability):
  r = random.random()
  c_probability = 0
  sum_probability = []
  for p in probability:
    c_probability += p
    sum_probability.append(c_probability)
  for item, sp in enumerate(sum_probability):
    if r <= sp:
      return item
  return len(probability)-1
  
def transform(p):
  # List of transformation functions
  transformations = [transformation_1, transformation_2,
  transformation_3, transformation_4]
  probability = [0.85, 0.07, 0.07, 0.01]
  # Pick a random transformation function and call it
  tindex = get_index(probability)
  t = transformations[tindex]
  x, y = t(p)
  return x, y
  
def draw_fern(n):
  # We start with (0, 0)
  x = [0]
  y = [0]
  x1, y1 = 0, 0
  for i in range(n):
    x1, y1 = transform((x1, y1))
    x.append(x1)
    y.append(y1)
  return x, y
  
if __name__ == '__main__':
  n = int(input('Enter the number of points in the Fern: '))
  x, y = draw_fern(n)
  # Plot the points
  plt.plot(x, y, 'o')
  plt.title('Fern with {0} points'.format(n))
  plt.show()
"""

"""
'''
Draw a square
'''
from matplotlib import pyplot as plt

def draw_square():
  ax = plt.axes(xlim = (0, 6), ylim = (0, 6))
  square = plt.Polygon([(1, 1), (5, 1), (5, 5), (1, 5)], closed = True)
  ax.add_patch(square)
  plt.show()
  
if __name__ == '__main__':
  draw_square()
"""

"""
from matplotlib import pyplot as plt

def create_circle(x, y):
  circle = plt.Circle((x, y), radius = 0.5)
  return circle
  
#def draw_circle(x, y):
#  ax = plt.gca()
#  create_circle(x, y)
  
if __name__ == '__main__':
  y = 1.5
  ax = plt.gca()
  while y < 5:
    x = 1.5
    while x < 5:
      c = create_circle(x, y)
      ax.add_patch(c)
      x += 1.0
    y += 1.0
    
  plt.axis('scaled')
  plt.show()
"""

"""
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

def initialize_image(x_p, y_p):
  image = []
  for i in range(y_p):
    x_colors = []
    for j in range(x_p):
      x_colors.append(0)
    image.append(x_colors)
  return image
  
def color_points():
  x_p = 6
  y_p = 6
  image = initialize_image(x_p, y_p)
  for i in range(y_p):
    for j in range(x_p):
      image[i][j] = random.randint(0, 10)
  plt.imshow(image, origin='lower', extent=(0, 5, 0, 5),
              cmap=cm.Greys_r, interpolation='nearest')
  plt.colorbar()
  plt.show()
  
if __name__ == '__main__':
  color_points()
"""

"""
import math
print(math.sin(math.pi/2))
"""

"""
import math
import sympy
print(sympy.sin(math.pi/2))
"""

"""
#import math
from sympy import Symbol, sin
theta = Symbol('theta')
#math.sin(theta) + math.sin(theta)
print(sin(theta) + sin(theta))
"""

"""
from sympy import sin, solve, Symbol
u = Symbol('u')
t = Symbol('t')
g = Symbol('g')
theta = Symbol('theta')
sol = solve(u*sin(theta)-g*t, t)
print(sol)
"""

"""
from sympy import Symbol
#x = Symbol('x')
x = Symbol('x', positive=True)
if (x+5) > 0:
  print('Do Something')
else:
  print('Do Something else')
"""

"""
from sympy import Limit, Symbol, S, sin
x = Symbol('x')
#L = Limit(1/x, x, S.Infinity)
#L = Limit(1/x, x, 0, dir='-')
#L = Limit(1/x, x, 0, dir='+')
L = Limit(sin(x)/x, x, 0)
print(L)
print(L.doit())
"""

"""
from sympy import Limit, Symbol, S
n = Symbol('n')
print(Limit((1+1/n)**n, n, S.Infinity).doit())
"""

"""
from sympy import Symbol, Limit, S
#p = Symbol('p', positive=True)
#r = Symbol('r', positive=True)
#t = Symbol('t', positive=True)
p = Symbol('p')
r = Symbol('r')
t = Symbol('t')
n = Symbol('n')
L = Limit(p*(1+r/n)**(n*t), n, S.Infinity)
print(L.doit())
"""

"""
from sympy import Symbol, Limit
t = Symbol('t')
St = 5*t**2 + 2*t + 8
t1 = Symbol('t1')
delta_t = Symbol('delta_t')
St1 = St.subs({t: t1})
St1_delta = St.subs({t: t1 + delta_t})
L = Limit((St1_delta-St1)/delta_t, delta_t, 0)
print(St1)
print(St1_delta)
print(L.doit())
"""

"""
from sympy import Symbol, Derivative
t = Symbol('t')
t1 = Symbol('t1')
St = 5*t**2 + 2*t + 8
expr = Derivative(St, t)
print(expr.doit().subs({t:1}))
"""

"""
from sympy import Derivative, Symbol
x = Symbol('x')
f = (x**3 + x**2 + x)*(x**2+x)
print(Derivative(f, x).doit())
"""

"""
'''
Derivative calculator
'''
from sympy import Symbol, Derivative, sympify, pprint
from sympy.core.sympify import SympifyError

def derivative(f, var):
  var = Symbol(var)
  d = Derivative(f, var).doit()
  #pprint(d)
  print(d)
  
if __name__=='__main__':
  f = input('Enter a function: ')
  var = input('Enter the variable to differentiate with respect to: ')
  try:
    f = sympify(f)
  except SympifyError:
    print('Invalid input')
  else:
    derivative(f, var)
"""

"""
from sympy import Symbol, solve, Derivative
x = Symbol('x')
x_min = -5
x_max = 5

f = x**5 - 30*x**3 + 50*x

d1 = Derivative(f, x).doit()
critical_points = solve(d1)
d2 = Derivative(f, x, 2).doit()
d3 = d1.subs({x:2})
d4 = d1.subs({x:x_min})
print(d1)
print(critical_points)
print(d2)
print(d3)
print(d4)
"""

"""
'''
Use gradient ascent to find the angle at which the projectile
has maximum range for a fixed velocity, 25 m/s
'''
import math
from sympy import Derivative, Symbol, sin

def grad_ascent(x0, f1x, x):
  epsilon = 1e-6
  step_size = 1e-4
  x_old = x0
  x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
  while abs(x_old - x_new) > epsilon:
    x_old = x_new
    x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
  return x_new

def find_max_theta(R, theta):
  # Calculate the first derivative
  R1theta = Derivative(R, theta).doit()
  theta0 = 1e-3
  theta_max = grad_ascent(theta0, R1theta, theta)
  return theta_max
  
if __name__ == '__main__':
  g = 9.8
  # Assume initial velocity
  u = 25
  # Expression for range
  theta = Symbol('theta')
  R = u**2*sin(2*theta)/g
  theta_max = find_max_theta(R, theta)
  print('Theta: {0}'.format(math.degrees(theta_max)))
  print('Maximum Range: {0}'.format(R.subs({theta:theta_max})))
"""

"""
'''
Use gradient ascent to find the maximum value of a
single-variable function
'''
from sympy import Derivative, Symbol, sympify

def grad_ascent(x0, f1x, x):
  epsilon = 1e-6
  step_size = 1e-4
  x_old = x0
  x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
  while abs(x_old - x_new) > epsilon:
    x_old = x_new
    x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
  return x_new
  
if __name__ == '__main__':
  f = input('Enter a function in one variable: ')
  var = input('Enter the variable to differentiate with respect to: ')
  var0 = float(input('Enter the initial value of the variable: '))
  try:
    f = sympify(f)
  except SympifyError:
    print('Invalid function entered')
  else:
    var = Symbol(var)
    d = Derivative(f, var).doit()
    var_max = grad_ascent(var0, d, var)
  print('{0}: {1}'.format(var.name, var_max))
  print('Maximum value: {0}'.format(f.subs({var:var_max})))
"""

"""
'''
Use gradient ascent to find the maximum value of a
single-variable function. This also checks for the existence
of a solution for the equation f'(x)=0.
'''
from sympy import Derivative, Symbol, sympify, solve

def grad_ascent(x0, f1x, x):
  # Check if f1x=0 has a solution
  if not solve(f1x):
    print('Cannot continue, solution for {0}=0 does not exist'.format(f1x))
    return
  epsilon = 1e-6
  step_size = 1e-4
  x_old = x0
  x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
  while abs(x_old - x_new) > epsilon:
    x_old = x_new
    x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
  return x_new

if __name__ == '__main__':
  f = input('Enter a function in one variable: ')
  var = input('Enter the variable to differentiate with respect to: ')
  var0 = float(input('Enter the initial value of the variable: '))
  try:
    f = sympify(f)
  except SympifyError:
    print('Invalid function entered')
  else:
    var = Symbol(var)
    d = Derivative(f, var).doit()
    var_max = grad_ascent(var0, d, var)
    if var_max:
      print('{0}: {1}'.format(var.name, var_max))
      print('Maximum value: {0}'.format(f.subs({var:var_max})))
"""

"""
from sympy import Integral, Symbol
x = Symbol('x')
k = Symbol('k')
#y = Integral(k*x, x)
y = Integral(k*x, (x,0,2))
print(y.doit())
"""

"""
from sympy import Symbol, exp, sqrt, pi, Integral
x = Symbol('x')
p = exp(-(x - 10)**2/2)/sqrt(2*pi)
y = Integral(p, (x, 11, 12)).doit().evalf()
print(y.doit())
"""


from sympy import Symbol, exp, sqrt, pi, Integral, S
x = Symbol('x')
p = exp(-(x - 10)**2/2)/sqrt(2*pi)
y = Integral(p, (x, S.NegativeInfinity, S.Infinity)).doit().evalf()
print(y)


