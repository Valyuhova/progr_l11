import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("comptagevelo2010.csv")

df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
df = df.set_index("Date")

if "Unnamed: 1" in df.columns:
    df = df.drop(columns=["Unnamed: 1"])

print("Перші рядки датафрейму:")
print(df.head(), "\n")

print("Інформація про датафрейм:")
print(df.info(), "\n")

print("Описова статистика:")
print(df.describe(), "\n")

total_all_paths = df.sum().sum()
print("Загальна кількість велосипедистів за рік на всіх велодоріжках:", int(total_all_paths), "\n")

total_by_path = df.sum()
print("Загальна кількість велосипедистів за рік на кожній велодоріжці:")
print(total_by_path, "\n")

df["Month"] = df.index.month

paths = ["Berri1", "Maisonneuve_1", "Rachel / Papineau"]

for path in paths:
    if path in df.columns:
        monthly_sum = df.groupby("Month")[path].sum()
        best_month = monthly_sum.idxmax()
        print(f"Найпопулярніший місяць для доріжки {path}: {best_month} (сума = {int(monthly_sum.max())})")
    else:
        print(f"Стовпця {path} немає у файлі.")
print()

path_for_plot = "Berri1"

monthly_berri = df.groupby("Month")[path_for_plot].sum()

plt.figure(figsize=(8, 5))
plt.plot(monthly_berri.index, monthly_berri.values, marker="o", linewidth=2)

plt.title(f"Завантаженість велодоріжки {path_for_plot} по місяцях (2010)")
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.grid(True)
plt.xticks(range(1, 13))

plt.show()