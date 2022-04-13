"""Prepared by:
20CS065 KISHAN PRAJAPATI
20CS066 DHRITIMAN SENPRAMANIC
20CS071 MANSI RAVAL"""

# Draw a line in a diagram from position (0,0) to position (6,250):
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()


# Draw a line in a diagram from position (1, 3) to position (8, 10):
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()


# Markers - Mark each point with a circle
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker= 'o')
plt.show()


# Linestyle - dotted line
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle='dotted')
plt.show()


# Scatter plot
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

plt.scatter(x, y)
plt.show()


# 4bar graph
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.show()


#Horizontal bar graph
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

#Pie chart
import matplotlib.pyplot as plt
cars = ['AUDI', 'BMW', 'NISSAN','TESLA', 'HYUNDAI', 'HONDA']
data = [20, 15, 15, 14, 16, 20]
plt.pie(data, labels =
cars,colors = ['#F0F8FF','#E6E6FA','#B0E0E6','#7B68EE','#483D8B'])
plt.title('Chart title')
plt.show()


#Grouped bar chart
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(5)
y1 = [34, 56, 12, 89, 67]
y2 = [12, 56, 78, 45, 90]
width = 0.40
# plot data in grouped manner of bar type
plt.bar(x-0.2, y1, width)
plt.bar(x+0.2, y2, width)
plt.show()


#Mini project: Stock market Analysis Using Matplotlib and Yfinance
import matplotlib.pyplot as plt
import yfinance as yf
start = "2012-01-01"
end = "2021-12-01"
amazon = yf.download('AMZN',start,end)
apple = yf.download('AAPL',start,end)
reliance = yf.download('RELIANCE.NS',start,end)
tesla = yf.download('TSLA',start,end)
amazon['Open'].plot(label = "Amazon")
apple['Open'].plot(label = "Apple")
reliance['Open'].plot(label = "Reliance")
tesla['Open'].plot(label = 'Tesla')
plt.legend(loc='best')
plt.title('Stock Prices of Amazon, Apple , Reliance and Tesla')
plt.show()