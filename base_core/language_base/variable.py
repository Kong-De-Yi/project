d1 = {"name": "Alice", "age": 30, "city": "New York"}
d2 = dict(name="Alice", age=30, city="New York")
d3 = dict([("name", "Alice"), ("age", 30), ("city", "New York")])

print(d1["name"])
print(d2.get("name"))
print(d3.get("email", "Not Found"))
