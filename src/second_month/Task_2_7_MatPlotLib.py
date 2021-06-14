#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 1 Write a Python program to draw a line with suitable label in the x axis, y axis and a title.
def draw_line(data):
    plt.plot(data)
    plt.title('Draw a line using matplotlib')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.show()


# 2 Write a Python program to draw line charts of the financial data of Alphabet Inc.
#   between October 3, 2016 to October 7, 2016
def draw_line_charts_of_fin_data(data_file):
    df = pd.read_csv(data_file, index_col=0)
    df.columns =['a','b', 'c', 'd']
    df.plot(kind='line')
    plt.legend(loc='upper left')
    plt.title("Financial Data of Alphabet Inc")
    plt.xlabel("Date Ranges for financial data")
    plt.show()


#  3. Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc.
# between October 3, 2016 to October 7, 2016. Customized the grid lines with linestyle -, width .5. and color blue.
def draw_line_charts_with_grid(data_file):
    df = pd.read_csv(data_file, index_col=0)
    df.columns = ['a', 'b', 'c', 'd']
    df1 = df.drop(['a','b', 'c'], axis=1)

    fig = plt.figure()
    pl = fig.add_subplot(1, 1, 1)
    pl.plot(df1, 'ro--', linewidth=1, markersize=8)
    pl.set_title("Financial Data of Alphabet Inc")
    pl.set_xlabel("Date Ranges for financial data")
    pl.set_ylabel("Values of data records")

    plt.grid(linestyle='-', linewidth='.5', color='blue')
    plt.show()


# 4. Write a Python programming to display a bar chart of the popularity of programming Languages
def bar_chart_languages_by_popularity(languages, popularity):
    plt.bar(languages, popularity)
    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("Languages Bar Chart By Popularity")
    plt.show()


# 5 Write a Python programming to create a pie chart of the popularity of programming Languages
def pie_chart_languages_by_popularity(languages_str, popularity_lst):
    plt.pie(popularity_lst, labels=languages_str)
    plt.title("Languages Pie Chart By Popularity")
    plt.show()


# 6. Write a Python program to draw a scatter graph taking a random distribution in X and Y
#    and plotted against each other.
def draw_scatter_graph(x, y):
    plt.scatter(x, y, color='b')
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()


def main():
    # 1
    data = np.arange(10)
    draw_line(data)

    # 2
    data_file = "files/AlphabetIncfinancialData.csv"
    draw_line_charts_of_fin_data(data_file)

    # 3
    draw_line_charts_with_grid(data_file)

    # 4
    languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    bar_chart_languages_by_popularity(languages, popularity)

    # 5
    languages_str = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
    pie_chart_languages_by_popularity(languages_str, popularity)

    # 5
    x = np.random.random(50)
    y = np.random.random(50)
    draw_scatter_graph(x, y)


main()
