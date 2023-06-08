def can_type_in_one_row(word):
    rows = [
        set("qwertyuiop"),
        set("asdfghjkl"),
        set("zxcvbnm")
    ]

    word_lower = word.lower()
    row = None

    # Check which row the first character belongs to
    for i in range(len(rows)):
        if word_lower[0] in rows[i]:
            row = i
            break

    # Check if all characters belong to the same row
    for char in word_lower:
        if char not in rows[row]:
            return False

    return True

# Test the function
word1 = "Hello"
word2 = "Python"
word3 = "asdf"
word4 = "OpenAI"

print(can_type_in_one_row(word1))  # Output: True
print(can_type_in_one_row(word2))  # Output: False
print(can_type_in_one_row(word3))  # Output: True
print(can_type_in_one_row(word4))  # Output: False
