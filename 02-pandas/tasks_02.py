import pandas as pd


# Task 1. Series
#
# Given a dictionary with students and their grades.
# 1. Create a Series named 'grades'.
# 2. Select only Max and Dima.
# 3. Change Alex's grade to 4.

students = pd.Series({
    'Ilya': 5,
    'Max': 4,
    'Alex': 3,
    'Dima': 5
}, name='grades')

selected_students = students.loc[['Max', 'Dima']]
students.loc['Alex'] = 4

print('Task 1:')
print(selected_students)
print(students, '\n')


# Task 2. DataFrame
#
# Given information about three students:
# name: Ilya, Max, Alex
# age: 19, 20, 21
# score: 85, 92, 78
#
# 1. Create a DataFrame with three columns.
# 2. Set row indexes: student_1, student_2, student_3.
# 3. Display only the 'name' and 'score' columns.

table = {
    'name': ['Ilya', 'Max', 'Alex'],
    'age': [19, 20, 21],
    'score': [85, 92, 78]
}

df = pd.DataFrame(
    table,
    index=['student_1', 'student_2', 'student_3']
)

print('Task 2:')
print(df[['name', 'score']], '\n')


# Task 3. Index alignment
#
# Given two Series:
# a = [10, 20, 30], indexes: A, B, C
# b = [100, 200, 300], indexes: B, C, D
#
# 1. Create a DataFrame from both Series.
# 2. Predict the values for rows A, B, C, D.
# 3. Determine where NaN values will appear.
# 4. Run the code and check your prediction.

a = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
b = pd.Series([100, 200, 300], index=['B', 'C', 'D'])

aligned_df = pd.DataFrame({'a': a, 'b': b})

print('Task 3:')
print(aligned_df)
