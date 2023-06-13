def max_pair_product(my_list: list) -> None:
    my_list.sort()

    print(my_list[-1] * my_list[-2])


if __name__ == "__main__":
    _ = input()
    my_list = list(map(int, input().split()))
    max_pair_product(my_list)
