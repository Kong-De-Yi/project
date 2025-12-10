name = "Jim"
first_name = "Halpert"
last_name = "Halpert"
full_name = first_name + " " + last_name
greeting = "Hello, " + name + "!"
age = 30
height_cm = 183.0
is_employee = True
skills = ["Sales", "Management", "Customer Service"]
address = {"street": "123 Paper St.", "city": "Scranton", "state": "PA", "zip": "18503"}
salary = None  # Salary is not yet defined
performance_score = 4.5  # Out of 5.0
work_hours = (9, 17)  # From 9 AM to 5 PM
project_codes = {"PRJ001", "PRJ002", "PRJ003"}
department = b"Sales"  # Byte string for department name
employee_id = 1001
bio = (
    f"{full_name} is {age} years old and works in the {department.decode()} department."
)
nickname = name.lower()
