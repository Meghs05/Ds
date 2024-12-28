import matplotlib.pyplot as plt

# Example data
lead_sources = ['Website', 'Referral', 'Social Media', 'Email', 'Ads', 'Events']
number_of_leads = [150, 100, 50, 80, 120, 30]

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(lead_sources, number_of_leads, color='skyblue')
plt.xlabel('Lead Source')
plt.ylabel('Number of Leads')
plt.title('Leads by Source')
plt.show()