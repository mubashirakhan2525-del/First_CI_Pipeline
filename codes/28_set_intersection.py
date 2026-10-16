
def set_intersection(first, second):
    result = set()

    for item in first:
        if item in second:
            result.add(item)

    return result


if __name__ == "__main__":
    first = set(map(int, input("Enter the first set of numbers: ").split()))
    second = set(map(int, input("Enter the second set of numbers: ").split()))

    print("Intersection:", set_intersection(first, second))
