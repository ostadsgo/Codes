def generate_hashtag(s):
    # Capitalize each word's first letter
    r = "#" + "".join(word.capitalize() for word in s.strip().split())
    if len(r) > 140 or len(r) == 0:
        return False
    return r

assert generate_hashtag('Codewars') == '#Codewars'
assert generate_hashtag('codewars  is  nice'), '#CodewarsIsNice'
assert generate_hashtag('Codewars') == '#Codewars', 'Should handle a single word.'
assert generate_hashtag('Codewars      ') == '#Codewars', 'Should handle trailing whitespace.'
assert generate_hashtag('      Codewars') == '#Codewars', 'Should handle leading whitespace.'
assert generate_hashtag('Codewars Is Nice')== '#CodewarsIsNice', 'Should remove spaces.'
assert generate_hashtag('codewars is nice')== '#CodewarsIsNice', 'Should capitalize first letters of words.'
assert generate_hashtag('CoDeWaRs is niCe')== '#CodewarsIsNice', 'Only the first letter of each word should be capitalized in the final hashtag, all other letters must be lower case.'
assert generate_hashtag('c i n')== '#CIN', 'A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1.'
assert generate_hashtag('codewars  is  nice')== '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.'
assert generate_hashtag(''), False== 'Expected an empty string to return False'
assert generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') == False, 'Should return False if the final string is longer than 140 chars.'
