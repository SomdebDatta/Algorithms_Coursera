def max_pair_product(my_list: list) -> None:
    n = len(my_list)
    max1, max2 = 0, 0

    for i in range(1, n):
        if my_list[i] > my_list[max1]:
            max1 = i

    if max1 == max2:
        max2 = 1

    for i in range(n):
        if my_list[i] > my_list[max2] and i != max1:
            max2 = i

    print(my_list[max1] * my_list[max2])


if __name__ == "__main__":
    _ = input()
    my_list = list(map(int, input().split()))
    max_pair_product(my_list)
