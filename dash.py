import matplotlib
from matplotlib import pyplot as plt
import pandas as pd

# Sample data
data = {
    "Country": ["China", "Japan", "India", "France", "Australia", "Sweden"],
    "Profit": [100, 159, 129, 58, 149, 49],
    "Forecast": [200, 140, 120, 60, 120, 60],
    "Target": [20, 150, 100, 80, 150, 55],
    "Revenue": [20, 30, 200, 116, 249, 1449],
    "Revenue2": [20, 100, 222, 152, 292, 242],
    "Revenue3": [512, 303, 263, 113, 443, 243]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot setup
fig, ax = plt.subplots(figsize=(10, 6))
width = 0.15  # width of each bar

# Set positions
positions = range(len(df["Country"]))

# Plot each metric
ax.bar([p - 2*width for p in positions], df["Profit"], width=width, label='Profit')
ax.bar([p - width for p in positions], df["Forecast"], width=width, label='Forecast')
ax.bar(positions, df["Target"], width=width, label='Target')
ax.bar([p + width for p in positions], df["Revenue"], width=width, label='Revenue')
ax.bar([p + 2*width for p in positions], df["Revenue2"], width=width, label='Revenue2')
ax.bar([p + 3*width for p in positions], df["Revenue3"], width=width, label='Revenue3')

# Label and style
ax.set_xlabel("Country")
ax.set_ylabel("Value")
ax.set_title("Country-wise Metrics")
ax.set_xticks(positions)
ax.set_xticklabels(df["Country"])
ax.legend()

# Show plot
plt.tight_layout()
plt.show()
