import string

def rotate(text, rot):
    letters = string.ascii_lowercase
    alphabet_len = len(letters)
    idx_to_letter = dict(enumerate(letters))
    letter_to_idx = dict([(v, k) for (k, v) in enumerate(letters)])

    def rotate_char(c: str, key: int):
        def rotate_letter(l: chr, rot: int):
            idx = letter_to_idx[l.lower()]
            rotated_letter = idx_to_letter[(idx + rot) % alphabet_len]

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

if __name__ == '__main__':
    print(rotate('a', 1))
