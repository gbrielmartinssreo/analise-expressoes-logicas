from src.classes.BooleanData import BooleanData
import re

def typeExpression(needValue):
    
    input_expression = input("Digite a expressao: "); 

    letters = sorted(list(set(re.findall("[a-zA-Z]",input_expression))))

    booleanData_vector = []

      
    if needValue == True:
        
        booleanData_qnt = len(letters) 

        for i in range(0,booleanData_qnt):

            value = input(f"Digite o valor (V/F) de {letters[i]}: ")[0];
        
            if value == "V":
                value=True;
            elif value == "F":
                value=False;

            booleanData_vector.append(BooleanData(letters[i],value));    
    
    else:
        booleanData_vector = letters[:]

    return input_expression,booleanData_vector;

