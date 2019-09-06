import os

debug = False


def main():
    with open("input.txt", "r") as file:
        line = [int(x) for x in file.readline().split()]
    print(mergeSort(line))


def mergeSort(numList):
    left = []
    right = []

    if len(numList) <= 1:
        return numList

    for x in range(len(numList)):
        if x < (len(numList) / 2):
            left.append(numList[x])
        else:
            right.append(numList[x])

    if debug:
        print(left)
        print(right)

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while left:
        result.append(left[0])
        left = left[1:]
    while right:
        result.append(right[0])
        right = right[1:]

    return result


if __name__ == '__main__':
    main()
