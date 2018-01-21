idCounter = 0

def generate(prefix):
    global idCounter
    idCounter = idCounter + 1
    id = str(idCounter)
    return prefix + id
