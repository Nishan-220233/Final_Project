import pandas as pd
import matplotlib.pyplot as plt

# i. Load the dataset
data = pd.read_csv("Final_Exam.csv")
print(data)


# ii. Remove rows with null values and save
data_Removed = data.dropna()
data_Removed.to_csv('removed_data.csv', index=False)
print(data_Removed)


# iii. Replace null values with column mean and save
data_filled = data.copy()
for column in ['Age', 'Salary']:
    data_filled[column].fillna(data_filled[column].mean(), inplace=True)
data_filled.to_csv('filled_data.csv', index=False)
print(data_filled)

# iv. Plot bar graph for bonus
plt.figure(figsize=(10, 5))
plt.bar(data['Name'], data['Bonus'], color='skyblue', label='Bonus')

# v. Title and label
plt.title('Bonus Drawn by Employees')
plt.xlabel('Employee Name')
plt.ylabel('Bonus Amount')
plt.legend()
plt.grid(axis='y')
plt.show()