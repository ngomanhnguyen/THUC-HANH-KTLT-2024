def bubbleSort(nlist):
    loop = len(nlist)
    for i in range(loop):
        swapped = False
        for j in range(loop - 1):
            if nlist[j] > nlist[j + 1]:
                # Trao đổi hai phần tử
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True
        # Nếu không cần trao đổi nữa thì thoát khỏi vòng lặp
        if not swapped:
            break
    return nlist