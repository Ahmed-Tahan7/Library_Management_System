import string

class Encryption:
    def encode(self, password):
        alphabet_lower = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
        alphabet_upper = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        shift = 5
        end_text = ""

        for char in password:
            if char in alphabet_lower:
                position = alphabet_lower.index(char)
                new_position = (position + shift) % 26  # Wrap around using modulo for lowercase letters
                end_text += alphabet_lower[new_position]
            elif char in alphabet_upper:
                position = alphabet_upper.index(char)
                new_position = (position + shift) % 26  # Wrap around for uppercase letters
                end_text += alphabet_upper[new_position]
            else:
                end_text += char  # Leave symbols, numbers, and other non-alphabetic characters unchanged

        return end_text