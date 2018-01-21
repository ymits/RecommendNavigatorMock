import random

def execute(all_accounts, params):
    groupNum = int(params.get("groupNum", 1))
    targets = all_accounts[:]

    chunk_size = int(len(targets) / groupNum)
    rest = len(targets) % groupNum

    random.shuffle(targets)
    groups = []
    x = 0
    while x < len(targets):
        if rest > 0:
            chunked = chunk_size + 1
            rest = rest - 1
        else:
            chunked = chunk_size
        groups.append(targets[x:x + chunked])

        x = x + chunked

    return groups
