#
import pandas as pd

f = open('files/data.csv', 'r')

count = 0

while True:
    count += 1
    line = f.readline()
    line = line.replace('"', '')
    line = line.replace(',', '')
    line = line.replace('\t', '')
    # line = line.strip()
    s1 = '+---------------+-----------------------+'
    s2 = '+-------------+------------------------------------------+-------------+---------------------+-------------------+------------+'
    s3 = '+-------------+-------------+-------------+----------+--------------------+------------+------------+----------+----------------+------------+---------------+'
    if line.strip() == '' or line.strip() == s1 or line.strip() == s2 or line.strip() == s3:
        continue

    if line.strip() == 'Region':
        file_name = "files/converted_regions.csv"
        this_case = count
        continue
    elif line.strip() == 'Location':
        file_name = "files/converted_location.csv"
        this_case = count
        continue
    elif line.strip() == 'employees.csv':
        file_name = "files/converted_employees.csv"
        this_case = count
        continue

    if this_case == 1:
        lst = line.split('|')
        dic = {'REGION_ID': [lst[1].strip()], 'REGION_NAME': [lst[2].strip()]}
    elif this_case == 11:
        lst = line.split('|')
        dic = {'LOCATION_ID': [lst[1].strip()], 'STREET_ADDRESS': [lst[2].strip()], 'POSTAL_CODE': [lst[3].strip()], 'CITY': [lst[4].strip()], 'STATE_PROVINCE': [lst[5].strip()], 'COUNTRY_ID': [lst[6].strip()] }
    elif this_case == 39:
        lst = line.split('|')
        dic = {'EMPLOYEE_ID': [lst[1].strip()], 'FIRST_NAME': [lst[2].strip()], 'LAST_NAME': [lst[3].strip()], 'EMAIL': [lst[4].strip()], 'PHONE_NUMBER': [lst[5].strip()], 'HIRE_DATE': [lst[6].strip()], 'JOB_ID': [lst[7].strip()], 'SALARY': [lst[8].strip()], 'COMMISSION_PCT': [lst[9].strip()], 'MANAGER_ID': [lst[10].strip()], 'DEPARTMENT_ID': [lst[11].strip()] }

    df = pd.DataFrame(dic)
    df.to_csv(file_name, mode='a', header=False)

    if not line:
        break

f.close()


