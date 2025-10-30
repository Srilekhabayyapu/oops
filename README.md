

 Project Documentation – Name Matching System

 Project Overview

The Name Matching System is a Python-based application designed to find the most similar names from a predefined dataset based on a given user input.
It uses fuzzy string matching to calculate similarity scores and ranks names according to how closely they match the input.


---

 Objective:

To build a name-matching engine that identifies names similar to a given input.

To return:

Best Match — the closest name with the highest similarity score.

List of Matches — other names ranked by similarity.




---

Concept Used: Fuzzy String Matching

Fuzzy matching helps compare two text strings and find how “close” they are, even if they aren’t identical (for example, “Geeta” vs. “Geetha”).
It works using Levenshtein Distance, which counts the number of edits (insertions, deletions, substitutions) needed to make one string identical to another.

Example:

String 1	String 2	Score (%)	Meaning

Geeta	Geetha	95	Very similar
Geeta	Gita	90	Close
Geeta	Sunita	40	Unrelated



---

 Libraries Used:

Library	Purpose

fuzzywuzzy	Provides fuzzy string matching algorithms
pandas	Displays ranked results in tabular format



---

🏗 Code Explanation

1️⃣ Importing Libraries

from fuzzywuzzy import process
import pandas as pd

process.extract() — compares an input string against a list and returns best matches.

pandas — used for creating a readable table of results.



---

2️⃣ Data Preparation

names_dataset = [
    "Geetha", "Gita", "Gitu", "Geetanjali", "Geetika", "Geet",
    "Sita", "Seetha", "Sheetal", "Sunita", "Sneha", "Soniya",
    "Priya", "Preeti", "Pooja", "Pari", "Payal", "Pavani",
    "Lavanya", "Latha", "Lakshmi", "Lalitha", "Leela", "Laya",
    "Rani", "Rithika", "Renu", "Rashmi", "Rohini", "Rajeshwari",
    "Meena", "Manisha", "Mounika", "Madhuri", "Mahalakshmi"
]

The dataset contains 30+ sample names for comparison.

You can replace or extend this list with any name dataset.



---

3️⃣ Taking User Input

user_input = input("🔍 Enter a name to find similar names: ").strip()

Prompts the user for a name.

.strip() removes unwanted spaces for clean input.



---

4️⃣ Performing Similarity Matching

matches = process.extract(user_input, names_dataset, limit=10)

Compares the user input with each name in the dataset.

Returns the top 10 closest matches as a list of tuples:

[('Geetha', 95), ('Gita', 90), ('Gitu', 84), ...]



---

5️⃣ Extracting Best Match

best_match = matches[0]
best_name, best_score = best_match

Takes the first item (highest score) as the best match.



---

6️⃣ Displaying the Results

print("\n Best Match:")
print(f"Name: {best_name}  |  Similarity Score: {best_score}")

print("\n Top 10 Similar Names:")
df = pd.DataFrame(matches, columns=["Name", "Similarity Score"])
print(df.to_string(index=False))

Shows the best matching name and similarity score.

Converts the full result list into a table using Pandas.



---
 Example Run

Input:

Geeta

Output:

 Best Match:
Name: Geetha  |  Similarity Score: 95

 Top 10 Similar Names:
        Name  Similarity Score
       Geetha                95
          Gita                90
          Gitu                84
     Geetika                81
   Geetanjali                77
         Geet                74
        Sita                65
      Seetha                63
       Sneha                58
       Rani                54


---

Functional Flow Diagram

┌────────────────────────┐
          │  Start Program          │
          └────────────┬───────────┘
                       │
             ┌─────────▼──────────┐
             │  Load Dataset       │
             └─────────┬──────────┘
                       │
             ┌─────────▼──────────┐
             │  Get User Input     │
             └─────────┬──────────┘
                       │
             ┌─────────▼──────────┐
             │  Compute Similarity │
             └─────────┬──────────┘
                       │
             ┌─────────▼──────────┐
             │  Show Results       │
             └─────────┬──────────┘
                       │
             ┌─────────▼──────────┐
             │  End Program        │
             └────────────────────┘


---

How to Test Locally

1. Ensure Python is Installed

python --version


2. Install Required Libraries

pip install fuzzywuzzy[speedup] pandas


3. Run the Program

python name_matcher.py


4. Verify Output

Enter test names like:

Geeta

Sita

Rani


Confirm the results match expected similarity rankings.





---
 Deliverables

File	Description

name_matcher.py	Main project code
README.md	Setup and usage instructions
DOCUMENTATION.md	Detailed explanation of logic and workflow



---

 Key Learnings

Fuzzy string matching helps match similar words with minor differences.

Useful in name-matching, duplicate detection, and text search.

Can be extended to work with large databases or ML vector models.



---
Author

Srilekha Bayyapu
Project: Name Matching System
