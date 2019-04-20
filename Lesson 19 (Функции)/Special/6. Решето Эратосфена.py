def eratosthenes(num):
    if num < 4:
        return

    exam = []
    ret = []

    for i in range(2, num + 1):
        exam.append(i)

    while exam:
        for i in exam[1:]:
            if i % exam[0] == 0:
                ret.append(i)
                exam.remove(i)
        exam = exam[1:]

    print(*ret)