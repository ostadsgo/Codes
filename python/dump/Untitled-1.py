test_string = "Some string." 
vowel_count = 0

for ch in test_string:
    if ch == 'a' or ch == 'A':
        vowel_count += 1
    if ch == 'e' or ch == 'E':
        vowel_count += 1
    if ch == 'i' or ch == 'I':
        vowel_count += 1
    if ch == 'o' or ch == 'O':
        vowel_count += 1
    if ch == 'u' or ch == 'U':
        vowel_count += 1

print(vowel_count)  # => 3

