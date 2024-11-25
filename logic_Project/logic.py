import json

from formulas.range_filter import add, filter_by_range, calculate_totals_each_category

#function to read the data on json file
def read_data(path):
    try:
        with open (f"databases/{path}", "r") as file: #open the file just on read mode
            return json.load(file) #load and return the data on json file
    except FileNotFoundError:# if the file doesnt exist, just return the list empty
        return[]
 
 
#function to write data on json file
def write_data(dat, path):
    with open(f"databases/{path}", "wd+") as file:#open the file just on read mode
        json.dumps(dat, file, indent=4) # wrote data on json format with 4 indentation

 
 
#function to registrate a new spend amount       
def register_bills (amount, category, description, date): 
    data = read_data("database.json")#load the data into the file
    new_spent = {  #create anew dictionary with the details of the spent

        "amount": amount,
        "category":category,
        "description":description,
        "date":date

    }

    data.append(new_spent) #add the new spent into the data list 
    write_data( data, "database.json") # save the update data into the json file

def call_bills(): # call every spent amount
    return read_data("database.json") #return all the data loaded from the file

def calculate_total():
    data = read_data("database.json") #load existing  data from the file
    if not data:
        return{}
    
    return calculate_totals_each_category(data, "category", "amount")# calculate and returns the total
 
#function to report the spent amount 
def generate_reports():
    data = read_data ("database.json")
    if not data:
        return  {"total_bills": 0, "totals_each_category": totals,}
    totals = calculate_total()
    report = {
        "total_bill": add( [spent["amount"] for spent in data if "amount" in spent]),
        "totals_each_category": totals

    }
    return report

