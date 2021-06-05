#
import numpy as np
import pandas as pd


# 1. Write a Pandas program to add, subtract, multiple and divide two Pandas Series
def series_basic_actions(s1, s2):
    return "\n Add two Series: \n {} \n Subtract two Series: \n {} \nMultiply  two Series\n {} \n Divide Series1 by " \
           "Series2 \n {}".format(s1 + s2, s1 - s2, s1 * s2, s1 / s2)


# 2. Write a Pandas program to convert a dictionary to a Pandas series.
def convert_dic_to_series(d):
    return pd.Series(d)


# 3. Write a Pandas program to convert a NumPy array to a Pandas series
def convert_np_arr_to_series(np_arr):
    return pd.Series(np_arr)


# 4. Write a Pandas program to convert the first column of a DataFrame as a Series
def convert_df_column_to_series(df):
    return pd.Series(df.iloc[0])


# 5. Write a Pandas program to sort a given Series
def sort_series(s):
    return s.sort_index()


# 6 Write a Pandas program to select the rows the score is between 15 and 20 (inclusive)
def select_rows_between(exam_data, position, between_from, between_to):
    df = pd.DataFrame(exam_data)
    return df[df.iloc[:, position].between(between_from, between_to)]


# 7 Write a Pandas program to calculate the sum of the examination attempts by the students.
def sum_examination_attempts(exam_data, position):
    df = pd.DataFrame(exam_data)
    return df.iloc[:, position].sum()


def main():
    # 1
    s1 = pd.Series([2, 4, 6, 8, 10])
    s2 = pd.Series([1, 3, 5, 7, 9])
    print("#1 Series basic actions", series_basic_actions(s1, s2))

    # 2
    d = {"brand": "Ford", "model": "Mustang", "year": 1964}
    print("#2 convert dict to series: \n", convert_dic_to_series(d))

    # 3
    np_arr = np.arange(4.)
    print("#3 convert np array to series: \n", convert_np_arr_to_series(np_arr))

    # 4
    df = pd.DataFrame({"A": pd.Categorical(["Apple", "Banana", "Blueberries", "Dewberry"]),
                       "B": pd.Timestamp("20130102"),
                       "C": pd.Series(1, index=list(range(4)), dtype="float32"),
                       "D": np.array([3] * 4, dtype="int32"),
                       })
    print("#4 convert first column of a DataFrame as a Series: \n", convert_df_column_to_series(df))

    # 5
    obj1 = pd.Series(range(4), index=['a', 'c', 'g', 'b'])
    print("# 5 Sort given Series: \n",  sort_series(obj1))

    # 6
    exam_data = {
        'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
    print("# 6 Score between 15 and 20\n", select_rows_between(exam_data, 1, 15, 20))

    # 7
    print("# 7 sum of the examination attempts\n", sum_examination_attempts(exam_data, 2))


main()
