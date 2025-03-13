import csv
import json
from datetime import datetime

#exception

class ValidationError(Exception):
    """Exception raised for validatoin errors."""
    def __init__(self, field, message = "Invalid value"):
        self.field = field
        self.message = message

try:
    raise ValidationError("username", "Must not be empty")
except ValidationError as e:
    print(e) 


#CSV - Comma Separated Values

#EXAMPLE

#   a1         a2      a3
#Username,Identifier,First name,Last name,Description -> Header
#booker12,9012,Rachel,Booker,"I know python, sql and js" -> no space allowed

with open('username.csv', 'rt') as f:
    print(f.read())

with open('username.csv', 'rt') as f:
    lines = f.read().splitlines()
    usernames = [row.split(', ')[0] for row in lines[1:]]
    print(lines)  # -> returns list of all lines
    print(usernames) # -> prints only usernames

columns =     ['Name', 'Age', 'City']
data = [
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles']
]

with open('output.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerow(data)

with open('username.csv', 'rt') as file:
    reader = csv.reader(file, delimiter=';')
    columns = next(reader)
    for row in reader:
        print(row) 


#DictReader
        
with open('username.csv', 'rt') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        print(row) 
#output:
# {'Username': 'booker12', 'Identifier': '9012', 'First name': 'Rachel', 'Last name': 'Booker'}
        
        
data = [
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'}
]

with open('output.csv', mode='w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictReader(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)


#JSON - JavaScript Object Notation
    
#EXAMPLE:
{    # it means a new object, in js
    "employees":[
        {"firstName":"John", "lastName":"Doe"},
        {"firstName":"Anna", "lastName":"Smith"}
    ]
}

with open('users.json', 'r') as file:
    data = json.load(file)
    print(data) 

json_str = """
{
"id": 1,
"name": "Alice Johnson",
"isActive": true,
}
"""
#use loads to convert

json_obj = json.load(json.str)
type(json_obj) 

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)  # indend 4 -> each of them in a new line, with 4 spaces, like a tab

# dump -> writing to a file
    
json_string = '{"name": "Bob", "age": 25, "city": "Los Angeles"}'
data = json.loads(json_string)
print(data)  # print as a dict


# dict to string -> dumps

print(datetime.now())

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
    