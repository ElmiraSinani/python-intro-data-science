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
        if i + 1 < len(lines):
            next_line_len = len(format_line(lines[i + 1]))
        if line_len == 0 and next_line_len > 0:
            this_case[new_files[j]] = i + 1
            j += 1

        if line_len > 0:
            if 'orders' in this_case:
                with open("files/orders.csv", 'a') as fw:
                    fw.write(format_line(line)+"\n")
                    fw.close()
            else:
                with open("files/schools.csv", 'a') as fw:
                    fw.write(format_line(line) + "\n")
                    fw.close()


parsing_data('files/2-6-2-data.csv')
