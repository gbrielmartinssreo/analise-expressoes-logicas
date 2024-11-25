from src.classes.BooleanData import BooleanData

def typeExpression(needValue):
    
    booleanData_qnt=int(input("Quantas letras tem a expressao: "));

    input_expression = input("Digite a expressao: "); 

    booleanData_vector = []

    for i in range(0,booleanData_qnt):
        letter = input(f"Digite a {i+1}º letra: ")[0];
        
        if needValue == False:
            booleanData_vector.append(letter);
            continue;

        value = input("Digite o valor (V/F): ")[0];
        
        if value == "V":
            value=True;
        elif value == "F":
            value=False;

        booleanData_vector.append(BooleanData(letter,value));    
    
    return input_expression,booleanData_vector;

