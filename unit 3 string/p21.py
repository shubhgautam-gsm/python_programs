# Printable characters
str1 = "Hello, this is a normal string."
print("Original string:", str1)
is_printable = str1.isprintable()
print("All characters are printable:", is_printable)  # Output: True

# Non-printable characters
str2 = "This string has\tabs \nand a\x07bell character."
print("\nOriginal string:", str2)
is_printable = str2.isprintable()
print("All characters are printable:", is_printable)  # Output: False

# Explanation of non-printable characters:
# - \t: Tab character (not visible but takes up space)
# - \n: Newline character (moves cursor to the next line)
# - \x07: Bell character (triggers a beep)
