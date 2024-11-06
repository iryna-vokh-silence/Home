
def is_within_1_to_10(a: int) -> bool:
    a = int(input("Введіть число: "))
    if 1 <= a <= 10:
        print("True")
        return True
    else:
        print("False")
        return False