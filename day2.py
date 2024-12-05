count = 0

with open('day2-input.txt', 'r+') as f:
    for line in f:
        digits = [int(x) for x in line.split(' ')]

        if len(digits) == 1:
            continue
        i = 0
        sign = 0 # 1: decrease, 2: increase
        inv = 1
        for i in range(len(digits) - 1):
            if digits[i] < digits[i+1]:
                if sign == 0:
                    sign = 1
                elif sign != 1:
                    inv = 0
                    break
            elif digits[i] > digits[i+1]:
                if sign == 0:
                    sign = 2
                elif sign != 2:
                    inv = 0
                    break
            else:
                inv = 0
                break

            if abs(digits[i] - digits[i+1]) > 3:
                inv = 0
                break
        if inv:
            count += 1
    print(count)