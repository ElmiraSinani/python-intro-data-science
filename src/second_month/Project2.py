#
import googletrans as googletrans
from googletrans import Translator
import numpy as np
import pandas as pd
import tabula
import matplotlib.pyplot as plt


def read_pdf(pdf_file):
    df = tabula.read_pdf(pdf_file, pages='all')[1]
    return df


def convert_pdf_to_csv(from_pdf_file, to_csv_file):
    tabula.convert_into(from_pdf_file, to_csv_file, output_format="csv", pages='all')


def df_describe(df):
    return df.describe()


def translate_months(df):
    # translator = Translator()
    # df['month'] = df['month'].map(lambda x: translator.translate(x, dest="en").text)
    # translator is not working as expected. so working with manual translation
    months_dict = {'Janeiro': 'January', 'Fevereiro': 'February', 'Março': 'March', 'Abril': 'April', 'Maio': 'May', 'Junho': 'June', 'Julho': 'July', 'Agosto': 'August', 'Setembro': 'September', 'Outubro': 'October', 'Novembro': 'November', 'Dezembro': 'December'}
    df['month'] = df['month'].map(months_dict)
    return True


def remove_dots_from_column(df, column):
    df[column] = df[column].replace('.', '', regex=True)


def drop_na(df):
    df['number'] = df['number'].replace(0, np.nan)
    return df.dropna()


def get_grouped_col_sum(df, group_by, sum_col):
    return df.groupby([group_by])[sum_col].sum()


def fires_by_year(df):
    data = pd.pivot_table(df, values="number", index=["year"], aggfunc=np.sum)
    data.plot.bar(color='g', alpha=1)
    plt.xlabel("Year")
    plt.ylabel("Number")
    plt.title("Fires by Year")
    plt.show()


def fires_by_month(df):
    data = pd.pivot_table(df, values="number", index=["month"], aggfunc=np.sum)
    data.plot.bar(color='g', alpha=1)
    plt.xlabel("Year")
    plt.ylabel("Number")
    plt.title("Fires by Month")
    plt.show()


def fires_by_year1(df):
    data = get_grouped_col_sum(df, 'year', 'number')
    plt.title("Fire numbers By Years")
    data.plot.bar(color='k', alpha=0.7)
    plt.show()


def reindex_month_names(data):
    new_index = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']
    return data.reindex(new_index)


def fires_by_month1(df):
    data = get_grouped_col_sum(df, 'month', 'number')
    data = reindex_month_names(data)
    plt.title("Fire numbers By Months\n")
    data.plot.bar(color='k', alpha=0.7)
    plt.show()


def fires_by_year_and_month(df):
    plt.figure(figsize=(300, 6))
    plt.rc('xtick', labelsize=5)
    df['year-month'] = df.apply(lambda x: str(x['year']) + ' ' + str(x['month']), axis=1)
    grouped_by_y_m = get_grouped_col_sum(df, 'year-month', 'number')
    plt.title("Fire numbers By Years Month")
    plt.legend(loc='upper left')
    grouped_by_y_m.plot.bar(color='k', alpha=0.7)
    plt.show()


def main():
    # convert pdf to csv
    # convert_pdf_to_csv("files/project2.pdf", "files/project2.csv")

    df = pd.read_csv("files/project2.csv")
    translate_months(df)
    remove_dots_from_column(df, 'number')
    df = drop_na(df)

    fires_by_year_and_month(df)
    fires_by_year(df)
    fires_by_year1(df)
    fires_by_month(df)
    fires_by_month1(df)


main()

