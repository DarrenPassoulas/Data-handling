# import the pandas module to be able to maniulate data. "as pd" is just calling pandas but calling it with the key letters "pd"
import pandas as pd 

# reading the data file you want to maniplate/ read data from 
df = pd.read_csv("Task4a_data.csv")

# Creating a empty file. I do this since when the user enter a certain product and supplier it stoes that information in a new data file
df2 = pd.read_csv("new.csv")



# creating inputs for products and supplier
# ex supplier = Natural Best
# ex product = Poratoes
Product_input = input("input product:")
Supplier_input = input("Supplier:")


# creating inputs for start date and end date.
# ex start date:01/01/2021
# ex end date:20/03/2021
print("print date in the format xx/xx/xxxx")
start_date = input("Start Date:")
end_date = input("End Date:")

# here i am accessing the product and supplier. It is accessed inputs above. this is all stored in the varible name new_df
new_df = df.loc[(df["Product"] == Product_input) & (df["Supplier"] == Supplier_input)]

# Once the user enter the product and supplier it is then store in a empty csv.
new_df.to_csv("new.csv")

# within the new file i would like to find if there were any profits made. So i create two extra colums amount purchased and amount sold i use these 2 colums to calculate the profit(3 colum)
new_df = df2["Amount Purchased"] = df2["KGs Purchased"] * df2["Purchase Price"]
new_df= df2["Amount sold"] = df2["KGs Sold"] * df2["Selling Price"]
new_df = df2["Profit"] = df2["Amount sold"] - df2["Amount Purchased"]


# start date and end date input will be accessed here to see the profit from a certain time range. 
second_file = (df2["Date"] >=start_date) & (df2["Date"] <= end_date) 
new_df = df2.loc[second_file] 

# show the information.
print(new_df)
