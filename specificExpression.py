from BooleanData import BooleanData
from Operator import Operator
from OpFunctions import *

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


def resolve_expression():
    booleanData_qnt=int(input("Quantas letras tem a expressao: "));

    booleanData_vector = []

    for i in range(0,booleanData_qnt):
        letter = input("Digite a letra: ")[0];
        value = input("Digite o valor (V/F): ")[0];
        if value == "V":
            value=True;
        elif value == "F":
            value=False;

        booleanData_vector.append(BooleanData(letter,value));    
        


    input_expression = input("Digite a expressao: "); 

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

    print(f"\nResultado: {final_resul}");

