from datetime import date

d1 = date(2025, 12, 13)
print(d1)
d2 = date.today()
print(d2)
import time

timestamp = time.time()
d3 = date.fromtimestamp(timestamp)
print(d3)
print(
    f"{d3.year},{d3.month},{d3.day},{d3.weekday()},{d3.isoweekday()},{d3.isoformat()},{d3.strftime('%Y年%m月%d日')}"
)
