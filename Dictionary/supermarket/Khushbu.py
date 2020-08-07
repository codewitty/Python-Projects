import pandas
pandas.set_option('display.max_colwidth', None)


def main():
    df1 = pandas.read_excel("data.xlsx")
    df2 = df1.set_index("Input")

    exp = input("Please enter an expression: ")
    print (f'{df2.at["Chipotl Postmates","Output"]}')

if __name__ == '__main__':
    main()

'''
print(df1)
print(df2.at["Chipotl Postmates",'Output'])
print(df1['Output'])
print(df2.loc["Chipotl Postmates", : ])
'''
