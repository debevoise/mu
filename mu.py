M, U, I = 'M', 'U', 'I'
MI = M+I
UU = U+U
III = I*3


def indices(string, pattern):
    idx = 0
    while True:
        try:
            yield (idx := string.index(pattern, idx))
            idx += 1
        except ValueError:
            break


def rule1(theorem):
    if theorem[-1] == I: 
        yield theorem + U

def rule2(theorem):
    return (
        theorem + theorem[i+1:] 
        for i in indices(theorem, M)
        )

def rule3(theorem):
    return (
        theorem[:idx] + U + theorem[idx+3:] 
        for idx in indices(theorem, III)
        )

def rule4(theorem):
    return (
        theorem[:idx] + theorem[idx+2:]   
        for idx in indices(theorem, UU)
        )

def rule_gen(theorem, rules):
    for rule in rules:
        for thm in rule(theorem):
            yield thm


AXIOM = [rule1,rule2,rule3,rule4]

q = [rule_gen(MI, AXIOM)]

while q:
    g = q.shift()
    
for i in g:
    print(g)