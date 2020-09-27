import random
from math import sqrt


def OneD():
    #  randomlist = random.sample(range(10, 30), 5)
    #  print(randomlist)

    w = random.sample(range(181, 240), 20)
    print(w, "\n")

    length = int(len(w) / 2)

    a = w[0:length]
    b = w[length:length * 2]

    for i in range(0, 10):
        print("\nIteration:", i + 1)

        print(a, b)

        l_a = sum(a) / len(a)
        l_b = sum(b) / len(b)
        l_a = round(l_a, 2)
        l_b = round(l_b, 2)
        print(f'Median A:{l_a}, Median B:{l_b}')  # Prints median values

        a = []
        b = []

        for values in w:
            if abs(values - l_a) < abs(values - l_b):
                a.append(values)
            else:
                b.append(values)

        print("New lists:")
        print(a, b)
        print(f'Median A:{round(sum(a) / len(a), 2)}, Median B:{round(sum(b) / len(b), 2)}')  # Prints median values

        if l_a == round(sum(a) / len(a), 2):
            print(f'A:(old){l_a},(new){round(sum(a) / len(a), 2)}\nB:(old){l_b},(new){round(sum(b) / len(b), 2)}')
            print(f"\nMean of last two iterations are the same\nTotal iterations: {i + 1}")
            break


def twoD():
    rows, cols = (2, 10)

    w = []
    lis = []

    # getting random heights
    h = random.sample(range(130, 205), 20)
    print(f'Height:{h}')

    # getting reg numbers
    for i in range(181, 201):
        lis.append(i)
    print(f'Reg numbers:{lis}')
    w = zip(lis, h)
    w = list(w)  # converting into list

    print(f'Reg with height:{w}')

    '''
    dist formula = sqrt((x2-x)**2 + (y2-y)**2))
    '''
    c1_x = w[0][0]  # getting const x value for c1
    c1_y = w[0][1]  # getting const y value for c1
    c2_x = w[1][0]  # getting const x value for c2
    c2_y = w[1][1]  # getting const y value for c2

    # mean values
    mx_c1 = 0
    my_c1 = 0
    mx_c2 = 0
    my_c2 = 0

    for iterations in range(1, 10):
        # empty lists to append new values
        c_1 = []
        c_2 = []
        #  getting answers from dist formula
        c1 = 0
        c2 = 0
        #  the variable values
        x2 = 0
        y2 = 0
        #  saving sum of x and y values in x &y
        sx = 0
        sy = 0
        print(f"\n\nIteration:{iterations}")
        for i in w:
            #  getting variable values
            x2 = i[0]
            y2 = i[1]
            #  applying dist formula
            c1 = sqrt((x2 - c1_x) ** 2 + (y2 - c1_y) ** 2)
            c2 = sqrt((x2 - c2_x) ** 2 + (y2 - c2_y) ** 2)
            # sorting in c1 and c2
            if abs(c1) < abs(c2):
                c_1.append(i)
            else:
                c_2.append(i)
        #  shows values in c1 and c2
        print(f'C1:{c_1},\nC2:{c_2}')
        #  gets sum of x and y for c1
        for sum_c1 in c_1:
            sx += sum_c1[0]
            sy += sum_c1[1]
        #  compares with previous mean sum, if same, exits loop
        if mx_c1 == sx:
            print(f"Iteration {iterations}, Mean values are the same")
            break
        # if not same, applies new mean to compare for next iteration
        mx_c1 = sx
        my_c1 = sy
        for sum_c2 in c_2:
            sx += sum_c2[0]
            sy += sum_c2[1]
        mx_c2 = sx
        my_c2 = sy
