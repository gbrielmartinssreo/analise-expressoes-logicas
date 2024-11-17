class Operator:
    def __init__(self,symbol,function,precedence):
        self.symbol=symbol;
        self.function=function;
        self.precedence=precedence;

    def __str__(self):
        return f"{self.symbol}, {self.function}, {self.precedence}";


def func_and(*values):
    resultado = True  
    for value in values:  
        resultado = resultado and value  
        if not resultado:  
            break
    return resultado


def func_or(*values):
    resultado = False  
    for value in values:  
        resultado = resultado or value  
        if resultado:  
            break
    return resultado


def func_neg(value):
    return not value;


def func_cond(value1,value2):
    if(value1==True and value2==False):
        return False;
    else:
        return True;

def func_bicond(value1,value2):
    if(value1==value2):
        return True;
    else:
        return False;



list_operators = [
        Operator("(",None,0),
        Operator(")",None,0),
        
        Operator("~",func_neg,5),
        Operator("^",func_and,4),
        Operator("v",func_or,3),
        Operator(">",func_cond,2),
        Operator("-",func_bicond,1), 
]

def buscaOperator(token):
    for operator in list_operators:
        if operator.symbol == token:
            return operator;


input_expression = input(str("Digite a expressao: ")); 

holding_stack = [];

output = []; 

solve_stack = [];

for token in input_expression:

    operator=buscaOperator(token);
    
    if not operator:
        if(token=='A'):
            output.append(True);
        elif(token=='B'):
            output.append(False);
        elif(token=='C'):
            output.append(False);
    elif ((operator.symbol != "(") and (operator.symbol != ")")):
        while holding_stack[-1].precedence > operator.precedence:
            output.append(holding_stack.pop());

        holding_stack.append(operator);
    elif (operator.symbol == "("):
        holding_stack.append(operator);
    elif (operator.symbol == ")"):
        while holding_stack[-1].symbol != "(":
            output.append(holding_stack.pop());

        holding_stack.pop();
        continue;

while len(holding_stack)>0:
    output.append(holding_stack.pop());








