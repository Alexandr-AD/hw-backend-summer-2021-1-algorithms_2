__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    even = 0
    odd = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even += arr[i]
        else:
            odd += arr[i]
    if odd == 0 or even == 0:
        return 0
    else:
        res = even/odd
        return res
