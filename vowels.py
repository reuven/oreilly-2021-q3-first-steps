def count_vowels(filename):
    count = 0

    for one_line in open(filename):
        for one_character in one_line.lower():
            if one_character in 'aeiou':
                count += 1

    return count


if __name__ == '__main__':
    s = input('Enter a string: ').strip()
    print(count_vowels(s))


# This is the file vowels.py
# In Python, I can load it with
#    import vowels

# Inside of the file, I defined a function called "count_vowels" When
# I "import vowels" in Python, this function is available as
# "vowels.count_vowels".  Because we're accessing a module's function
# via the module object.

# We could also have said "from vowels import count_vowels".  And then
# we would have had to run "count_vowels()"
