import pandas
pandas.set_option('display.max_colwidth', None)

def main():
    df1 = pandas.read_excel("data.xlsx")
    df2 = df1.set_index('Input').transpose().to_dict(orient='list')

    exp = input("Please enter an expression: ")
    print (f'{df2[exp]}')

if __name__ == '__main__':
    main()

'''
print(df2.at["Chipotl Postmates",'Output'])
print(df2.loc["Chipotl Postmates", : ])
data_dict = df1.to_dict()
print(f'{data_dict}')
V1
    df2 = df1.set_index("Input")
    exp = input("Please enter an expression: ")
    print (f'{df2.at[exp,"Output"]}')

'''
