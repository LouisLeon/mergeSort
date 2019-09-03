import os


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
        if numList[x] < (len(numList)/2):
            left.append(numList[x])
        else:
            right.append(numList[x])
    print(left);
    print(right);

def merge():
    pass


if __name__ == '__main__':
    main()
