"""LintCode No.415 Valid Palindrome

Functions will be tested under LintCode test environment
"""


def is_valid_palindrome(input_str):
    left, right = 0, len(input_str) - 1

    while left < right and not input_str[left].isalpha() and not input_str[left].isdigit():
        left += 1
    while left < right and not input_str[right].isalpha() and not input_str[right].isdigit():
        right += 1

    while left < right:
        if input_str[left].lower() == input_str[right].lower():
            continue
        else:
            return False

    return True


a_str = 'A man, a plan, a canal: Panama'
valid = is_valid_palindrome(a_str)
print(valid)

