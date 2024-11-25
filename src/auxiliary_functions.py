from src.classes.Operator import Operator 

def buscaOperator(token):
    for operator in list_operators:
        if operator.symbol == token:
            return operator;



def func_and(*values):
    if values[0]==True and values[1]==True:
        return True;
    else:
        return False;

def func_or(*values):
    if values[0]==False and values[1]==False:
        return False;
    else:
        return True;


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
