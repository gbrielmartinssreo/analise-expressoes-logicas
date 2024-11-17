class Operator:
    def __init__(self,symbol,function,precedence,parameters):
        self.symbol=symbol;
        self.function=function;
        self.precedence=precedence;
        self.parameters=parameters;

    def __str__(self):
        return f"{self.symbol}, {self.function}, {self.precedence}, {self.parameters}";



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

def func_neg(*values):
    return not values[0];

def func_cond(*values):
    if(values[0]==True and values[1]==False):
        return False;
    else:
        return True;

def func_bicond(*values):
    if(values[0]==values[1]):
        return True;
    else:
        return False;



list_operators = [
        Operator("(",None,0,0),
        Operator(")",None,0,0),
        
        Operator("~",func_neg,5,1),
        Operator("^",func_and,4,2),
        Operator("v",func_or,3,2),
        Operator(">",func_cond,2,2),
        Operator("-",func_bicond,1,2), 
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
            output.append(True);
    
    elif (operator.symbol == "("):
        holding_stack.append(operator);
    elif (operator.symbol == ")"):
        while holding_stack[-1].symbol != "(":
            output.append(holding_stack.pop());

        holding_stack.pop();
        continue;

    
    elif (operator.symbol == "("):
        holding_stack.append(operator);
    
    elif (operator.symbol == ")"):
        while holding_stack[-1].symbol != "(":
            output.append(holding_stack.pop());

        holding_stack.pop();
        continue;

    elif(len(holding_stack)==0):
        holding_stack.append(operator);

    elif ((operator.symbol != "(") and (operator.symbol != ")")):
        while holding_stack[-1].precedence > operator.precedence:
            output.append(holding_stack.pop());

        holding_stack.append(operator);
    

while len(holding_stack)>0:
    output.append(holding_stack.pop());

for item in output:
    if isinstance(item,bool):
        solve_stack.append(item);
    elif isinstance(item,Operator):
        uni_resul=item.function(solve_stack[(-item.parameters):]);
        for i in range(-1,-(item.parameters)):
            solve_stack.pop();

        solve_stack.append(uni_resul);

final_resul=solve_stack[0];

print(f"{final_resul}");







