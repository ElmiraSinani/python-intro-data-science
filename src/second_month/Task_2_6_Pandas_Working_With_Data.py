#
import pandas as pd


def format_line(line):
    line = line.replace(",", "")
    line = line.replace("Ex12 3 2004", "")
    line = line.replace("Ex5.", "")
    for i in range(60, 1, -1):
        space = i * ' '
        line = line.replace(space, ",")
    return line.strip()


def parsing_data(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    this_case = {}
    new_files = ['school', 'orders']
    j = 0
    for i in range(0, len(lines)):
        line = lines[i]
        line_len = len(format_line(line))
        formatted_line = format_line(line)
        if i + 1 < len(lines):
            next_line_len = len(format_line(lines[i + 1]))
        if line_len == 0 and next_line_len > 0:
            this_case[new_files[j]] = i + 1
            j += 1

        if formatted_line.startswith('school') or formatted_line.startswith('ord_no'):
            formatted_line = 'id,'+formatted_line

        if line_len > 0:
            if 'orders' in this_case:
                with open("files/orders.csv", 'a') as fw:
                    fw.write(formatted_line+"\n")
                    fw.close()
            else:
                with open("files/schools.csv", 'a') as fw:
                    fw.write(formatted_line + "\n")
                    fw.close()


# 1. Write a Pandas program to split the following dataframe into groups based on school code
def group_df_by_column(file, column):
    df = pd.read_csv(file)
    return df.groupby([column])


# 2 Write a Pandas program to split the following given dataframe by school code and get mean, min, and max value of
# age for each school
def group_df_by_col_and_agg(file, column):
    df = pd.read_csv(file)
    return df.groupby([column]).agg({'age': ['mean', 'min', 'max']})


# 3 Write a Pandas program to split the following given dataframe into groups based on school code and class
def group_df_by_columns(file, columns_list):
    df = pd.read_csv(file)
    return df.groupby(columns_list)


# 4 Write a Pandas program to split the following given dataframe into groups based on school code and cast grouping
# as a list
def group_by_col_and_cast_to_list(file, column):
    df = pd.read_csv(file)
    group_by_col = df.groupby([column])
    return list(group_by_col)


# 5 Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group.
# Using the following dataset find the mean, min, and max values of purchase amount (purch_amt)
# group by customer id (customer_id)
def split_df_group_and_agg(file, group_by_col, agg_column):
    df = pd.read_csv(file)
    return df.groupby([group_by_col]).agg({agg_column: ['mean', 'min', 'max']})


def main():
    # parsing data: one time action
    # parsing_data('files/2-6-2-data.csv')

    # 1
    file = 'files/schools.csv';
    df_by_column = group_df_by_column(file, 'school')
    for col, frame in df_by_column:
        print(f"DataFrame records for group {col!r}")
        print("------------------------")
        print(frame, end="\n\n")

    # 2
    print(group_df_by_col_and_agg(file, 'school'), end="\n\n")

    # 3
    df_by_columns = group_df_by_columns(file, ['school', 'class'])
    for col, frame in df_by_columns:
        print(f"DataFrame records for group {col!r}")
        print("------------------------")
        print(frame, end="\n\n")

    # 4
    print(group_by_col_and_cast_to_list(file, 'school'), end="\n\n")

    # 5
    orders_file = "files/orders.csv"
    print(split_df_group_and_agg(orders_file, 'customer_id', 'purch_amt'));

main()