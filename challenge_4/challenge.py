#CHALLENGE 4
#PRINT FIRST AND LAST 3 CHARACTER OF A STRING

def first_and_last_three(s: str) -> str:
    """
    Visszaadja az első 3 és az utolsó 3 karaktert egy stringből összefűzve.
    Ha a string rövidebb, mint 3 karakter, akkor visszaadja a stringet.
    """
    if len(s) < 3:
        return s
    return s[:3] + s[-3:]
