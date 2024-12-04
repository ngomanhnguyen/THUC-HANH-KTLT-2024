def bubbleSort(nlist):
    """
    Hàm sắp xếp nổi bọt (Bubble Sort)
    :param nlist: Danh sách các phần tử cần sắp xếp
    :return: Danh sách sau khi đã được sắp xếp
    """
    loop = len(nlist)
    for i in range(loop - 1):
        swapped = False
        for j in range(loop - 1 - i):  # Giảm dần phạm vi so sánh
            if nlist[j] > nlist[j + 1]:
                # Tráo đổi hai phần tử
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True
        # Nếu không có sự hoán đổi nào, danh sách đã được sắp xếp
        if not swapped:
            break
    return nlist