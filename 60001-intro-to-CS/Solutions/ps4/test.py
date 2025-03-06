from ps4b import *

test = Message("test")

print(test.get_message_text)



test_dick = {'d':3,'f':9}

test_dick['j']  = 10

print(test_dick)


shift = 25
shift_dict = {}

for i in range(ord('a'),ord('z')+1):
    shift_dict[chr(i)] = alphabet[alphabet.index(chr(i)) + shift]

for i in range(ord('A'),ord('Z')+1):
    shift_dict[chr(i)] = alphabet[alphabet.index(chr(i)) + shift]

print(shift_dict)


print(len(shift_dict))    

orig_msg = "test message"
shift_msg = list(orig_msg)

for i, char in enumerate(shift_msg):
    if char in shift_dict:
        shift_msg[i] = shift_dict[char]

print(shift_msg)

for i in range(1,26):
    print(i)

test_dick['k'] = 10
a = max(test_dick, key=test_dick.get)


a
