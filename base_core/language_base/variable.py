# 序列


# 映射
"""创建"""
d1 = {"name": "Alice", "age": 25, "city": "Beijing"}
d2 = dict(name="Alice", age=25, city="Beijing ")
d3 = dict([("name", "Alice"), ("age", 25), ("city", "Beiing")])

"""使用字典推导式"""
squares = {x: x**2 for x in range(5)}
print(squares)
