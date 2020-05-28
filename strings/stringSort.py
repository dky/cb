def stringSort(s):
    sortedStr = sorted(s.replace(" ", ""))
    return "".join(sortedStr)


if __name__ == "__main__":
    s = "The quick brown jumps over the lazy dog"
    print(stringSort(s))
