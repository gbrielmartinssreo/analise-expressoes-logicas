import re

def close_parentheses(term):
    open_count = 0

    for char in term:
        if char == '(':
            open_count += 1  
        elif char == ')':
            open_count -= 1  

    if open_count > 0:
        term += ')' * open_count  

    return term

def resolve_logic_prop(expression):
    expression = expression.replace("^", "&")

    pattern_negation = r"(?<![~A-Z()])(~[A-Z])(?![~A-Z])"
    expression = re.sub(pattern_negation, r"(\1)", expression)

    pattern_binary = r"(?<!\()([~A-Z]+\s*[>v&|]\s*[~A-Z]+)(?!\))"
    expression = re.sub(pattern_binary, r"(\1)", expression)

    pattern_isolated = r"(?<![~A-Z()])([A-Z])(?![~A-Z])"
    expression = re.sub(pattern_isolated, r"(\1)", expression)

    pattern_conclusion = r"\([^\(\)]*\)"
    matches = list(re.finditer(pattern_conclusion, expression))

    conclusion = ""
    if matches:
        conclusion = matches[-1].group()
        print(f"Achou a conclusão: {conclusion}")
    else:
        print("Nenhuma conclusão encontrada!")

    expression = expression.replace(conclusion, "")

    hypothesis = re.findall(r"\([^\)]+\)", expression)

    for i in range(0,len(hypothesis)):
        hypothesis[i] = close_parentheses(hypothesis[i])

    print(hypothesis)
