def reverse_vowels(text):
    vowels = "aeiouAEIOU"
    text_list = list(text)
    vowel_positions = [i for i, char in enumerate(text_list) if char in vowels]
    vowel_chars = [text_list[i] for i in vowel_positions]
    vowel_chars.reverse()

    for i, pos in enumerate(vowel_positions):
        text_list[pos] = vowel_chars[i]

    return ''.join(text_list)

# Get user input
input_text = input("Enter a string: ")
output_text = reverse_vowels(input_text)
print(f"Input: {input_text}")
print(f"Output: {output_text}")
