def people():
    unsorted_list = []
    sorted_list = []

    for _ range(5):
        info = []
        info.append(input('Give me a name:'))
        info.append(input('Give me an age: '))
        info.append(input('Give me a score:'))
        unordered_list = tuple(people)

        sorted_list.append(unordered_list)

    sorted_list.sort(key=lambda x:(x[0], x[1], x[2]))
    print(sorted_list)

    print(people())