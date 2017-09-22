import re

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)


def plural(noun):
    for matches_rules, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)     
