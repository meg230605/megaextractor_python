# TABLE READER
import pandas as pd
print()
print('''              This is a simple program
              for extracting tables or data in
              tabular format from any website   ''')
print()
website=input("Enter the url of the website you want to extract the tables from: ")
data= pd.read_html(website)
for table in data:
    print(table)
    ask = input("Want to extract more Tables ? Enter yes or no : ")
    if ask.lower()=="yes":
            continue
    else:
        print("----- THANK YOU -----")
        break
