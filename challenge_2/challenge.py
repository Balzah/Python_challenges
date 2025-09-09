#CHALLENGE 2
#FIND THE CHARACTER AT A SPECIFIC INDEX


def char_at_index(s: str, i: int) -> str:

    if len(s) == 0:
        return "String is empty."
    elif i < len(s):
        return s[i]
    else:
        return "Out of range."