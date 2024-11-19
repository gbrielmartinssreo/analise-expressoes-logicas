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


