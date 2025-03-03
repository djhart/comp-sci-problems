# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def insert_char(string, char, position):
    new_string = string[:position] + char + string[position:]
    return new_string

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return sequence
    else:
        sublist = get_permutations(sequence[1:])
        shift_letter = sequence[0]
        permutation_list = []
        i = 0
        for perm in sublist:
            for j in range(len(perm)+1):
                permutation_list.append(insert_char(perm,shift_letter,j))
                i += 1

        return permutation_list





if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)


    print(get_permutations("cat"))
    print(get_permutations("abc"))
    print(get_permutations("zoo"))


