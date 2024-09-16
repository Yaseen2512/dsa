# team6
# Name : Mohameed Yaseen M (23110028)
# Write a python program to create class and objects for reversing a vowels without replacing the index position of vowels

class VowelReverser:
    def __init__(self, text):
        self.text = text

    def reverse_vowels(self):
        vowels = "aeiouAEIOU"
        text_list = list(self.text)
        i, j = 0, len(text_list) - 1

        while i < j:
            if text_list[i] not in vowels:
                i += 1
            elif text_list[j] not in vowels:
                j -= 1
            else:
                text_list[i], text_list[j] = text_list[j], text_list[i]
                i += 1
                j -= 1

        return ''.join(text_list)

while True:
    input_text = input("Enter a string (or type 'exit' to quit): ")
    if input_text.lower() == 'exit':
        break
    reverser = VowelReverser(input_text)
    output_text = reverser.reverse_vowels()
    print(f"Input: {input_text}")
    print(f"Output: {output_text}")
