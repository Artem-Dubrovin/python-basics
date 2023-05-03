while True:
    x = int(input('введите число: '))
    count = 0
    fucktireal = 1
    while count < x: #120 = 5*4*3*2*1
        count += 1 
        fucktireal *= count
    print(fucktireal)