import string


def rotate(text, rot):
    letters = string.ascii_lowercase
    alphabet_len = len(letters)

    def rotate_char(c: str, key: int):
        def rotate_letter(l: chr, rot: int):
            idx = ord(l.lower()) - 97
            rotated_idx = (idx + rot) % alphabet_len
            rotated_letter = chr(rotated_idx + 97)

            if l.islower():
                return rotated_letter
            else:
                return rotated_letter.upper()

        if c.isalpha():
            return rotate_letter(c, key)
        else:
            return c

    rotated_text = ''.join([rotate_char(c, rot) for c in text])

    return rotated_text
