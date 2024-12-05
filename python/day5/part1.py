in_date = ""

with open("input.txt") as f:
    in_date = f.read()


raw_rules, raw_updates = in_date.strip().split("\n\n")


def build_rule_sequence(rule):
    return [int(i) for i in rule.split("|")]


str_rules = raw_rules.split("\n")
rules = []
for r in str_rules:
    rules.append(build_rule_sequence(r))

rule_sequences = {}
# Key - Item
# Value - Numbers that the Item has to follow after
for r in rules:
    if r[0] not in rule_sequences:
        rule_sequences[r[0]] = set()
    rule_sequences[r[0]].add(r[1])


def check_s(array):
    # checks only broken rules
    for i in range(len(array)):
        pre_s = array[:i]
        cur = array[i]
        if not cur in rule_sequences:
            continue
        # checks if any previous items occur as an item that the current one has to follow after
        # means that a rule is obviously broken
        for p in pre_s:
            if p in rule_sequences[cur]:
                return False
    return True


bad_s = []
good_s = []
for raw_update in raw_updates.strip().split("\n"):
    update = [int(i) for i in raw_update.split(",")]
    if not check_s(update):
        bad_s.append(update)
    else:
        good_s.append(update)


total = 0
for s in good_s:
    total += s[len(s) // 2]

print(total)
