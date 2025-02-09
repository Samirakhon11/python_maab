txt = 'LMaasleitbtui'
car_names = ['', '']

for i in range(len(txt)):
    index = i % 2
    car_names[index] += txt[i].lower()

for name in car_names:
    if 6 <= len(name) <= 7:
        print(name)