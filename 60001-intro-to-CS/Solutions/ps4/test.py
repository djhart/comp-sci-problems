from ps4b import *
import string
from ps4a import get_permutations


test = Message("test")

print(test.get_message_text)



test_dick = {'d':3,'f':9}

test_dick['j']  = 10

print(test_dick)


shift = 25
shift_dict = {}

# for i in range(ord('a'),ord('z')+1):
#     shift_dict[chr(i)] = alphabet[alphabet.index(chr(i)) + shift]

# for i in range(ord('A'),ord('Z')+1):
#     shift_dict[chr(i)] = alphabet[alphabet.index(chr(i)) + shift]

# print(shift_dict)


print(len(shift_dict))    

orig_msg = "test message"
shift_msg = list(orig_msg)

for i, char in enumerate(shift_msg):
    if char in shift_dict:
        shift_msg[i] = shift_dict[char]

print(shift_msg)

for i in range(1,26):
    print(i)

test_dick['k'] = 100
a = max(test_dick, key=test_dick.get)

import random
VOWELS_LOWER = 'aeiou'
vowels_permutation = random.choice(get_permutations(VOWELS_LOWER))

dict = {}
perm_list = list(vowels_permutation)

for i, letter in enumerate(list(VOWELS_LOWER)):
    dict[letter] = perm_list[i]
    dict[letter.upper()] = perm_list[i].upper()
        









perm_list = get_permutations(VOWELS_LOWER)
scores = {}
for i, perm in enumerate(perm_list):
    trans_dict = dict
    test_message = self.apply_transpose(trans_dict)
    current_score = 0
    valid_words = self.get_valid_words()
    for word in test_message.split():
        if is_word(valid_words,word):
            current_score += 1
    scores[i] = current_score

real_perm = perm_list[max(scores, key=scores.get)]
if max(scores) == 0:
    return self.get_message_text()
else:
    return (real_perm , self.apply_transpose(real_perm))

print(dict)
