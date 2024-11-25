import json

from formulas.range_filter import add, filter_by_range, calculate_totals_each_category


def read_data(path):
    try:
        with open (f"databases/{path}", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
        
def write_data(dat, path):
    with open(f"databases/{path}", "wd+") as file:
        json.dumps(dat, file, indent=4)

def register_bills (amount, category, description, date):
    data = read_data("database.json")
    new_spent = { 

        "amount": amount,
        "category":category,
        "description":description,
        "date":date

    }

    data.append(new_spent)
    write_data( data, "database.json")

def call_bills():
    return read_data("database.json")

def calculate_total():
    data = read_data("database.json")
    if not data:
        return{}
    
    return calculate_totals_each_category(data, "category", "amount")
 

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

