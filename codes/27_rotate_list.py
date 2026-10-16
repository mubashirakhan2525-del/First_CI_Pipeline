
def rotate_list(items, k):
    if not items:
        return []

    length = len(items)
    k = k % length

    if k == 0:
        return items.copy()

    return items[-k:] + items[:-k]


if __name__ == "__main__":
    items = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter rotation positions (negative for left): "))

    print("Rotated list:", rotate_list(items, k))
