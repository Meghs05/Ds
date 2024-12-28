import matplotlib.pyplot as plt

# Example data
regions = ['North', 'South', 'East', 'West', 'Central']
number_of_leads = [120, 150, 100, 130, 90]

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(regions, number_of_leads, color='yellow')
plt.xlabel('Region')
plt.ylabel('Number of Leads')
plt.title('Leads by Region')
plt.show()
