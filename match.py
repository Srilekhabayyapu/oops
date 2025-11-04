# ======================================
# Project: Name Matching System
# Author: Srilekha Bayyapu
# ======================================

from fuzzywuzzy import process
import pandas as pd

# ------------------------------
# Step 1: Data Preparation
# ------------------------------
names_dataset = [
    "Geetha", "Gita", "Gitu", "Geetanjali", "Geetika", "Geet",
    "Sita", "Seetha", "Sheetal", "Sunita", "Sneha", "Soniya",
    "Priya", "Preeti", "Pooja", "Pari", "Payal", "Pavani",
    "Lavanya", "Latha", "Lakshmi", "Lalitha", "Leela", "Laya",
    "Rani", "Rithika", "Renu", "Rashmi", "Rohini", "Rajeshwari",
    "Meena", "Manisha", "Mounika", "Madhuri", "Mahalakshmi"
]

# ------------------------------
# Step 2: Take user input
# ------------------------------
user_input = input("Enter a name to find similar names: ").strip()

# ------------------------------
# Step 3: Similarity Matching
# ------------------------------
matches = process.extract(user_input, names_dataset, limit=10)

# ------------------------------
# Step 4: Best Match and Ranked List
# ------------------------------
best_match = matches[0]
best_name, best_score = best_match

# Display Results
print("\n Best Match:")
print(f"Name: {best_name}  |  Similarity Score: {best_score}")

print("\n Top 10 Similar Names:")
df = pd.DataFrame(matches, columns=["Name", "Similarity Score"])
print(df.to_string(index=False))