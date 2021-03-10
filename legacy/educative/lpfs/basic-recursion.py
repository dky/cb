def rec_count(number):
    print("This is the:", number)
    # Base case
    if number == 0:
        return 0
    rec_count(number - 1)  # A recursive call with a different argument
    print("Call to rec_count to decrement:", number)


rec_count(5)
