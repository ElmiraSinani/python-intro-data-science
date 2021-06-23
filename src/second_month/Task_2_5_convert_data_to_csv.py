#
import pandas as pd

f = open('files/data.csv', 'r')
lines = f.readlines()

for i in range(0, len(lines)):
    line = lines[i]
    line = line.replace('"', '')
    line = line.replace(',', '')
    line = line.replace('\t', '')
    if line.strip() == '' or line.strip()[0] == '+':
        continue

    if line.strip() == 'Region':
        file_name = "files/converted_regions.csv"
        this_case = 'reg'
        continue
    elif line.strip() == 'Location':
        file_name = "files/converted_location.csv"
        this_case = 'loc'
        continue
    elif line.strip() == 'employees.csv':
        file_name = "files/converted_employees.csv"
        this_case = 'emp'
        continue

    if this_case == 'reg':
        lst = line.split('|')
        dic = {'REGION_ID': [lst[1].strip()], 'REGION_NAME': [lst[2].strip()]}
    elif this_case == 'loc':
        lst = line.split('|')
        dic = {'LOCATION_ID': [lst[1].strip()], 'STREET_ADDRESS': [lst[2].strip()], 'POSTAL_CODE': [lst[3].strip()], 'CITY': [lst[4].strip()], 'STATE_PROVINCE': [lst[5].strip()], 'COUNTRY_ID': [lst[6].strip()] }
    elif this_case == 'emp':
        lst = line.split('|')
        dic = {'EMPLOYEE_ID': [lst[1].strip()], 'FIRST_NAME': [lst[2].strip()], 'LAST_NAME': [lst[3].strip()], 'EMAIL': [lst[4].strip()], 'PHONE_NUMBER': [lst[5].strip()], 'HIRE_DATE': [lst[6].strip()], 'JOB_ID': [lst[7].strip()], 'SALARY': [lst[8].strip()], 'COMMISSION_PCT': [lst[9].strip()], 'MANAGER_ID': [lst[10].strip()], 'DEPARTMENT_ID': [lst[11].strip()] }

    df = pd.DataFrame(dic)
    df.to_csv(file_name, mode='a', header=False)

f.close()


