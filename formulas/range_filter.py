
def filter_by_range(data, key, start, end):
    return [item for item in data if start <= item [key] <= end]

