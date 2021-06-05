#
import numpy as np
import pandas as pd


# 1. Write a Pandas program to display all the records of REGIONS file
def read_from_file(file):
    return pd.read_csv(file)


# 2. Write a Pandas program to display all the location id from locations file.
def get_location_column(file, col_name):
    locations = pd.read_csv(file)
    return locations[[col_name]]


# 3. Write a Pandas program to extract first 7 records from employees file.
def extract_sub_records(file, rows_number):
    return pd.read_csv(file, nrows=rows_number)


# 4. Write a Pandas program to select distinct department id from employees file.
def select_distinct_dep_ids(file):
    f = pd.read_csv(file)
    return f.DepartmentID.unique()


# 5. Write a Pandas program to display the first, last name, salary and department number for those employees
# whose first name starts with the letter 'S'.
def first_name_starts_with(file, start_with_letter, use_cols):
    df = pd.read_csv(file, usecols=use_cols)
    return df[df.FirstName.str.startswith(start_with_letter)]


def main():
    # 1
    print("#1: Show All Region Info \n", read_from_file("files/us_regions_and_divisions.csv"))

    # 2
    print("#2: Display location ids \n", get_location_column("files/locations.csv", 'ID'))

    # 3
    print("#3: extract sub records \n", extract_sub_records("files/employees.csv", 7))

    # 4
    print("#4. distinct department ids: \n", select_distinct_dep_ids("files/employees.csv"))

    # 5
    print("# 5 \n", first_name_starts_with("files/employees.csv", 'A', ['FirstName', 'LastName', 'Salary', 'DepartmentID']))


main()
