import pandas as pd

employees = {
    "Кузін":         "м. Суми, вул. Заливна, 5",
    "Куравльов":     "м. Суми, вул. Збройних Сил України, 63",
    "Іващенко":      "м. Суми, вул. Харківська, 10",
    "Пасішніченко":  "м. Суми, вул. Героїв Сумщини, 7",
    "Шевченко":      "м. Суми, вул. В'ячеслава Чорновола, 51",
    "Кудін":         "м. Суми, вул. Івана Сірка, 9",
    "Статівка":      "м. Суми, вул. Михайла Лушпи, 3",
    "Кубиків":       "м. Суми, вул. Козацький Вал, 1",
    "Кульков":       "м. Суми, вул. Білопільський шлях, 11",
    "Лозовська":     "м. Суми, вул. Петропавлівська, 16"
}

df = pd.DataFrame(list(employees.items()), columns=["Surname", "Address"])

df["Salary"] = [18000, 22000, 19500, 25000, 27000, 21000, 20000, 19000, 30000, 23000]
df["Bonus"]  = [3000,  2500,  1500,  4000,  5000,  2000,  1800,  1000,  4500,  3000]

df["Profit"] = df["Salary"] + df["Bonus"]

print("Повний DataFrame:")
print(df)
print()

print("Перші 3 рядки DataFrame:")
print(df.head(3))
print()

print("Типи даних у стовпцях:")
print(df.dtypes)
print()

print("Кількість рядків і стовпців (df.shape):")
print(df.shape)
print()

print("Описова статистика (df.describe()):")
print(df.describe())
print()

high_salary = df[df["Salary"] > 10000]
print("Працівники із зарплатою понад 10 000 грн:")
print(high_salary[["Surname", "Salary", "Bonus", "Profit"]])
print()

sorted_df = df.sort_values(by="Salary", ascending=False)
print("Сортування за зарплатою (спадання):")
print(sorted_df[["Surname", "Salary", "Bonus", "Profit"]])
print()

df["Salary_Group"] = pd.cut(
    df["Salary"],
    bins=[0, 20000, 25000, 30000, 40000],
    labels=["до 20 тис", "20–25 тис", "25–30 тис", "понад 30 тис"]
)

grouped_mean = df.groupby("Salary_Group", observed=False)["Profit"].mean()
print("Середній прибуток (TotalPay) по групах зарплат:")
print(grouped_mean)
print()

max_profit = df["Profit"].max()
max_emp = df.loc[df["Profit"].idxmax(), "Surname"]
print(f"Максимальний прибуток: {max_profit} грн (у працівника {max_emp})")

unique_bonus_sum = df["Bonus"].drop_duplicates().sum()
print("Сума унікальних бонусів:", unique_bonus_sum)