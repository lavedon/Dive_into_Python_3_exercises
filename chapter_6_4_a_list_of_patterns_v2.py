import re


def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

patterns = \
         (
             ('[sxz]$',       '$', 'es'),
             ('[^aeioudgkprt]h$',   '$', 'es'),
             ('(qu|[^aeiou])y$',    'y$','ies'),
             ('$',              '$',    's')
        )

print("Here are the patterns we have to build functions with")
print(patterns)
print("now using rules to build all these functions")
rules = [build_match_and_apply_functions(pattern, search, replace)
         for (pattern, search, replace) in patterns]

print(rules)
print("\n \n \n")
print("Go ahead and use the super duper function 'plural(your_word)' now")
