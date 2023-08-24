   
list = ["january", "febuary", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

for month in list :
    print( month)
month = input("Enter Month ") 
for month in list :

  if (month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december"):
    num_of_days = 31
  else:
    num_of_days = 30     
print("number of days are " + str(num_of_days))       