import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('flights.csv')

avg_delays_monthly = df.groupby('Month').agg({
    'DepDelay': 'mean',
    'ArrDelay': 'mean'
}).reset_index()

print("\nAverage Delays by Month:")
print(avg_delays_monthly)

plt.figure(figsize=(12, 6))

plt.plot(avg_delays_monthly['Month'], avg_delays_monthly['DepDelay'], marker='o', color='blue', label='Departure Delay')

plt.plot(avg_delays_monthly['Month'], avg_delays_monthly['ArrDelay'], marker='o', color='green', label='Arrival Delay')

plt.title('Average Departure and Arrival Delays by Month')
plt.xlabel('Month')
plt.ylabel('Delay (minutes)')
plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
