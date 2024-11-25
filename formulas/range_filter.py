#function to filtrate data per rango of dates
def filter_by_range(data, key, start, end):
    return [item for item in data if start <= item [key] <= end]

#filter a list of dictionaries per range of dates
