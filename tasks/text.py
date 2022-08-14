from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    if len(text) == 0:
        return (None, None)
    else:
        if re.fullmatch("\s{1,}", text):
            return (None, None)
        else:
            testtxt = re.split("\s{1,}", text)
            ans = (min(testtxt, key=len), max(testtxt, key=len))
        return ans

