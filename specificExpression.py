from BooleanData import BooleanData
from Operator import Operator
from OpFunctions import *

def resolve_expression(input_expression,booleanData_vector):

    holding_stack = [];

    output = []; 

    solve_stack = [];

    for token in input_expression:

        operator=buscaOperator(token);
        
        if not operator:
            for item in booleanData_vector:
                if token == item.letter:
                    output.append(item.value);
        
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
                if len(holding_stack)==0:
                    break;
            
            holding_stack.append(operator);
        

    while len(holding_stack)>0:
        output.append(holding_stack.pop());

    for item in output:
        if isinstance(item,bool):
            solve_stack.append(item);
        
        elif isinstance(item,Operator):
            parameters=solve_stack[-(item.parameters):]
            uni_resul=item.function(*parameters);
            
            for i in range(0,item.parameters):
                solve_stack.pop();
            
            solve_stack.append(uni_resul);

    final_resul=solve_stack[0];
    
    return final_resul;

