subscript_string = "9" + chr(0x2088) + "7"  # Using Unicode character for superscript 8
print(subscript_string)  # Output: 9⁸7

formatted_string = f"9{chr(0x2088)}7"  # Using f-string interpolation
print(formatted_string)  # Output: 9⁸7