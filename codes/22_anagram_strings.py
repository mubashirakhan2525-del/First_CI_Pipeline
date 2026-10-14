def is_anagram(first, second):
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()

    return sorted(first) == sorted(second)


if __name__ == "__main__":
    first = input("Enter the first string: ")
    second = input("Enter the second string: ")

    print(is_anagram(first, second))