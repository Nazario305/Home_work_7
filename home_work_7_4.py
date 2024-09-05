def common_elements():
    numbers1 = []
    numbers2 = []

    for i in range(0, 100):
        if i % 3 == 0:
            numbers1.append(i)

    numbers1_set = set(numbers1)
    # print(numbers1)
    for i in range(0, 100):
        if i % 5 == 0:
            numbers2.append(i)
    # print(numbers2)
    numbers2_set = set(numbers2)
    intersection_set = numbers1_set.intersection(numbers2_set)
    # print(intersection_set)
    return intersection_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')
