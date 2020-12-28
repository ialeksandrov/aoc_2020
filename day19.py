def rule_maker(raw_rules):
    rules = {}
    for rule in raw_rules:
        key, value = rule.split(': ')
        if value[0] == '"':
            rules[int(key)] = value[1:-1]
        else:
            values = value.split(' | ')
            temp_v = []
            for v in values:
                temp_v.append([int(vv) for vv in v.split(' ')])
            rules[int(key)] = temp_v
    return rules


def match_rule(expr, stack):
    if len(stack) > len(expr):
        return False
    elif len(stack) == 0 or len(expr) == 0:
        return len(stack) == 0 and len(expr) == 0

    c = stack.pop()
    if isinstance(c, str):
        if expr[0] == c:
            return match_rule(expr[1:], stack.copy())
    else:
        for rule in rules[c]:
            if match_rule(expr, stack + list(reversed(rule))):
                return True
    return False


def count_messages(rules, messages):
    total = 0
    for message in messages:
        if match_rule(message, list(reversed(rules[0][0]))):
            total += 1
    return total


with open("day19_input.txt") as fp:
    raw_rules, message = fp.read().split('\n\n')
    raw_rules = raw_rules.splitlines()
    message = message.splitlines()

rules = rule_maker(raw_rules)

print(f"Part 1: {count_messages(rules, message)}")
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
print(f"Part 2: {count_messages(rules, message)}")
