alphabets = 'abcdefghijklmnopqrstuvwxyz'
num_alphabet_mapping = {}
alphabet_num_mapping = {}
for i, alphabet in enumerate(alphabets):
    alphabet_num_mapping[i] = alphabet
    num_alphabet_mapping[alphabet] = i
from collections import Counter


def rollTheString(s, roll):
    # roll.sort(reversed=True)
    total_roll = [0] * len(s)
    counts = Counter(roll)
    nums = sorted(counts.keys(), reverse=True)
    nums.append(0)
    count = 0

    for i in range(len(nums)-1):
        count += counts[nums[i]]
        for j in range(nums[i]-1, nums[i+1]-1, -1):
            total_roll[j] += count
    count += counts[nums[-1]]
    for j in range(nums[-1]-1, -1, -1):
        total_roll[j] += count
    result = ''
    for i in range(len(s)):
        c = s[i]
        new_c = alphabet_num_mapping[(num_alphabet_mapping[c] + total_roll[i])%26]
        result += new_c
    return result