# Function to tranform JSON to CSV row
def json_to_csv_row(element):
    row_csv = [str(value) for value in element.values()]
    return ",".join(row_csv)