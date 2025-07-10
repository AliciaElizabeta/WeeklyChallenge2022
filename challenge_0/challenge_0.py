
for index in range(1,101):
    div3 = index % 3 == 0
    div5 = index % 5 == 0
    if div3 and div5:
        print ("fizzbuzz")
        continue
    if div3:
        print ("fizz")
        continue
    if div5:
        print ("buzz")
        continue
    print(index)
