import string


def rotate(text, rot):
    alphabet = string.ascii_lowercase
    alphabet_len = len(alphabet)

    def rotate_char(c: str, key: int):
        def rotate_letter(l: chr, rot: int):
            idx = alphabet.find(l.lower())
            rotated_idx = (idx + rot) % alphabet_len
            rotated_letter = alphabet[rotated_idx]

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
