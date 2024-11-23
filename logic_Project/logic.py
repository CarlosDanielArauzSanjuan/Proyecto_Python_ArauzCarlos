import json

from formulas.operations import add, filter_by_range, calculate_totals_each_category


def read_data(path):
    with open (f"databases/{path}", "r") as file:
        return json.load(file)
    

def write_data(data, path):
    with open(f"databases/{path}", "wd+") as file:
        json.dumps(data, file, indent=4)

def register_bills (amount, category, description, date):
    data = read_data("database.json")
    new_data = { 

        "amount": amount,
        "category":category,
        "description":description,
        "date":date

    }

    data.append(new_data)
    write_data( data, "database.json")

def call_bills():
    return read_data("database.json")

def calculate_total():
    data = read_data("database.json")
    return calculate_totals_each_category(data, "category", "amount")
 

def generate_reports():
    data = read_data ("database.json")
    totals = calculate_total()
    report = {
        "total_bill": add([spent["amount"] for ------ in data]),
        "totals_each_category": totals

    }
    return report

