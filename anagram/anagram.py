from collections import Counter


def detect_anagrams(word, candidates):
    def is_anagram_of(word, candidate):
        is_anagram = Counter(word.lower()) == Counter(candidate.lower())
        is_all_caps_version = word.lower() == candidate.lower()

        return (is_anagram
                and not is_all_caps_version)

    return [candidate
            for candidate
            in candidates
            if is_anagram_of(word, candidate)]
