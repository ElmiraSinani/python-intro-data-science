#
import numpy as np
import pandas as pd


# 1. Write a Pandas program to add, subtract, multiple and divide two Pandas Series
def series_basic_actions(s1, s2):
    print("#1. Add two Series: \n", s1 + s2)
    print("#1. Subtract two Series: \n", s1 - s2)
    print("#1. Multiply two Series: \n", s1 * s2)
    print("#1. Divide Series1 by Series2: \n", s1 / s2)


# 2. Write a Pandas program to convert a dictionary to a Pandas series.
def convert_dic_to_series(d):
    print("#2 convert dict to series: \n", pd.Series(d))


# 3. Write a Pandas program to convert a NumPy array to a Pandas series
def convert_np_arr_to_series(s):
    print("#3 convert np array to series: \n", s)


# 4. Write a Pandas program to convert the first column of a DataFrame as a Series
def convert_df_column_to_series(df):
    print("#4 convert first column of a DataFrame as a Series: \n", pd.Series(df['A']))


# 5. Write a Pandas program to sort a given Series
def sort_series(s):
    print("# 5 Sort given Series: \n", s.sort_index())


# 6 Write a Pandas program to select the rows the score is between 15 and 20 (inclusive)
def select_rows_score(exam_data):
    df = pd.DataFrame(exam_data)
    print("# 6 Score between 15 and 20\n", df[df['score'].between(15, 20)])


# 7 Write a Pandas program to calculate the sum of the examination attempts by the students.
def sum_examination_attempts(exam_data):
    df = pd.DataFrame(exam_data)
    print("# 7 sum of the examination attempts\n", df['attempts'].sum())



def main():
    # 1
    s1 = pd.Series([2, 4, 6, 8, 10])
    s2 = pd.Series([1, 3, 5, 7, 9])
    series_basic_actions(s1, s2)

    # 2
    d = {"brand": "Ford", "model": "Mustang", "year": 1964}
    convert_dic_to_series(d)

    # 3
    obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
    convert_np_arr_to_series(obj)

    # 4
    df = pd.DataFrame({"A": pd.Categorical(["Apple", "Banana", "Blueberries", "Dewberry"]),
                       "B": pd.Timestamp("20130102"),
                       "C": pd.Series(1, index=list(range(4)), dtype="float32"),
                       "D": np.array([3] * 4, dtype="int32"),
                       })
    convert_df_column_to_series(df)

    # 5
    obj1 = pd.Series(range(4), index=['a', 'c', 'g', 'b'])
    sort_series(obj1)

    # 6
    exam_data = {
        'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
    select_rows_score(exam_data)

    # 7
    sum_examination_attempts(exam_data)


main()
