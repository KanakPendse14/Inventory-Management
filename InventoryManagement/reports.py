import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file
data = pd.read_excel("C:\\Users\\ACER\\IdeaProjects\\InventoryManagement\\exceldata.xlsx")
data = data.set_index("Product Name")

# Create a figure and axis objects
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

# Plot bar chart on the first axis
ax1.bar(data.index, data['Stock Value'])
ax1.set_title("Stock Statistic")
ax1.set_xlabel("Product Name")
ax1.set_ylabel("Stock Values")
ax1.tick_params(axis='x', rotation=90)  # Rotate x-axis labels for better readability

# Calculate total stock value
total_stock_value = data['Stock Value'].sum()

# Calculate percentage of each product's stock value
data['Stock Percentage'] = data['Stock Value'] / total_stock_value * 100

# Plot pie chart on the second axis
ax2.pie(data['Stock Percentage'], labels=data.index, autopct='%1.1f%%', startangle=140)
ax2.set_title("Stock Distribution")
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Plot histogram for sales per month on the third axis
ax3.hist(data['Sales per Month'])
ax3.set_xlabel("Product Name")
ax3.set_ylabel("Sales per Month")
ax3.set_title("Sales per Month Distribution")

# Plot histogram for sales per year on the fourth axis
ax4.hist(data['Sales per Year'])
ax4.set_xlabel("Year")
ax4.set_ylabel("Sales per Year")
ax4.set_title("Sales per Year Distribution")

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
