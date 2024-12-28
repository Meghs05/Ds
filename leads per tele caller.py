import pandas as pd

# Example dataset: A DataFrame containing the lead information
data = {
    "lead_id": [1, 2, 3, 4, 5, 6],
    "agent": ["John", "Mary", "John", "Mary", "Alex", "John"]
}

df = pd.DataFrame(data)

# Count the number of leads per agent using the groupby function
leads_count = df.groupby("agent").size()

# Output the number of leads handled by each agent
print("Total Leads per Tele-caller:")
print(leads_count)
