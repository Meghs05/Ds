import pandas as pd

# Example dataset: A DataFrame containing the lead statuses
data = {
    "lead_id": [1, 2, 3, 4, 5, 6],
    "status": ["Open", "Closed", "In Progress", "Open", "Closed", "Open"]
}

df = pd.DataFrame(data)

# Count the number of leads per status using the groupby function
status_count = df.groupby("status").size()

# Output the lead status distribution
print("Lead Status Distribution:")
print(status_count)
