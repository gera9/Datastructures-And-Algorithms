def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hash_map = {}
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        if hash_map.get(char_s, 0) != 0:
            hash_map[char_s] += 1
        else:
            hash_map[char_s] = 1

        if hash_map.get(char_t, 0) != 0:
            hash_map[char_t] -= 1
        else:
            hash_map[char_t] = -1

    for v in hash_map:
        if hash_map[v] != 0:
            return False

    return True


def main() -> None:
    s = "anagram"
    t = "nagaram"

    print(is_anagram(s, t))


if __name__ == "__main__":
    main()
