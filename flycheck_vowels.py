def count_vowels(filename):
    count = 0

    for one_line in open(filename):
        for one_character in one_line.lower():
            if one_character in 'aeiou':
                count += 1

    return count


# This is the file vowels.py
# In Python, I can load it with


#    import vowels

# 