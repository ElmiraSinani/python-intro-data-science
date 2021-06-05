#
import numpy as np
import pandas as pd


# 1. Write a Pandas program to display all the records of REGIONS file
def read_from_file(file):
    print("#1: Show All Region Info \n", pd.read_csv(file))


# 2. Write a Pandas program to display all the location id from locations file.
def get_location_column(file, column_name):
    locations = pd.read_csv(file)
    print("#2: Display location ids \n", locations[['ID']])


# 3. Write a Pandas program to extract first 7 records from employees file.
def extract_sub_records(file, rows_number):
    print("#3: extract sub records \n", pd.read_csv(file, nrows=rows_number))


# 4. Write a Pandas program to select distinct department id from employees file.
def select_distinct_dep_ids(file):
    f = pd.read_csv(file)
    print("#4. distinct department ids: \n", f.DepartmentID.unique())


# 5. Write a Pandas program to display the first, last name, salary and department number for those employees
# whose first name starts with the letter 'S'.
def filter_emp_data(file, start_with_letter):
    df = pd.read_csv(file, usecols=['FirstName', 'LastName', 'Salary', 'DepartmentID'])
    print("# 5 \n", df[df.FirstName.str.startswith(start_with_letter)])


def main():
    # 1
    read_from_file("files/us_regions_and_divisions.csv")

    # 2
    get_location_column("files/locations.csv", 'ID')

    # 3
    extract_sub_records("files/employees.csv", 7)

    # 4
    select_distinct_dep_ids("files/employees.csv")

    # 5
    filter_emp_data("files/employees.csv", 'A')


main()
