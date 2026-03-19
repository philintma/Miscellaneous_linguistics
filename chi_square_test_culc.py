import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

import pandas as pd

# --- 1. Load Google Sheets data ---
# Replace with your actual sheet ID
sheet_id = "1UVo7wPeu2HXRQ1Zm8VTa4v2Bui2shyrRskHduYHttCw"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

df = pd.read_csv(url)

# --- 2. Keep only first 18 rows ---
df = df.iloc[:18]

# --- 3. Rename columns (shorter names) ---
df.columns = [
    "verb", "miguel_ok", "knapp_ok", "miguel_res", "knapp_res",
    "freq_constr", "freq_total", "freq_ratio",
    "es_constr", "es_total", "es_ratio",
    "am_constr", "am_total", "am_ratio",
    "mx_constr", "mx_total", "mx_ratio"
]

# --- 4. Convert column types ---

# First 6 columns → strings
df.iloc[:, :6] = df.iloc[:, :6].astype(str)

# Remaining columns → integers
df.iloc[:, 6:] = df.iloc[:, 6:].astype(int)

# --- 5. Check result ---
print(df.dtypes)
print(df.head())

# Example data:
# rows = verbs
# columns = [in construction, not in construction]

#SPAIN 20-21
# Data
verbs = [
     "llegar", "rodar", "caer", "entrar", "avanzar",
     "salir", "subir", "bajar", "partir", "volver", "venir", "ir"
      ]
in_constr = np.array([76, 1, 5, 6, 2, 6, 2, 2, 1, 1, 3, 2])
total = np.array([174444, 5801, 43759, 65307, 16158, 106266, 
                   30965, 27684, 12544, 121678, 94908, 693371])

# # Compute frequencies
# freq = in_constr / total

# sorted_idx = np.argsort(freq)[::-1]

# freq = freq[sorted_idx]
# verbs = np.array(verbs)[sorted_idx]

# to_test = []

# for i in range(len(in_constr)):
#     to_test.append([in_constr[i], total[i] - in_constr[i]])

# to_test = np.array(to_test)
#chi2, p, dof, expected = chi2_contingency(to_test)

# print("Chi-square:", chi2)
# print("p-value:", p)
# print("Degrees of freedom:", dof)
# print("Expected frequencies:\n", expected)

# residuals = (to_test - expected) / np.sqrt(expected)
# print("Residuals", residuals)
# for i, r in enumerate(residuals[:, 0]):
#         if abs(r) > 2:
#             print(f"Verb {i} is unusual: residual = {r:.2f}")

# # Plot
plt.figure(figsize=(12, 6))

bars = plt.bar(verbs, freq, color="#7b2cbf")  # purple

# Styling
plt.title("Frequency of Verbs in Absolute Participle Clause", fontsize=16)
plt.xlabel("Verb", fontsize=12)
plt.ylabel("Frequency (k/n)", fontsize=12)

plt.xticks(rotation=45, ha="right")

# Grid for readability
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Remove top/right spines for cleaner look
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()