import json

from formulas.operations import add, filter_by_range, calculate_totals_each_category


def read_data(path):
    with open (f"databases/{path}", "r") as file:
        return json.load(file)
    

def write_data(data, path):
    with open(f"databases/{path}", "wd+") as file:
        json.dumps(data, file, indent=4)

def register_bills (amount, category, description, date):
    data= read_data("database.json")
    new_data = { 

        "amount":
        "category":
        "description":
        "date":




    }


