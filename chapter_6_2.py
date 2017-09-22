import re


def plural(noun):
    """
    A to make a enligh word plural using REGEX.
    It automatically make english words plural.
    """
    if re.search('[sxz]$', noun):
    # [ ] means "match exactly one of these characters"
    # $ matches the end of a string.
        return re.sub('$', 'es', noun) #re.sub performs REGEX string substituion.
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'
