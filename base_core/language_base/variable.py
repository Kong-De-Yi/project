try:
    with open("D:\\Hello.txt") as f:
        for line in f:
            print(line, end="")
except Exception as e:
    print(e)
