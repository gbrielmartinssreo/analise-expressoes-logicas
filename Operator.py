class Operator:
    def __init__(self,symbol,function,precedence,parameters):
        self.symbol=symbol;
        self.function=function;
        self.precedence=precedence;
        self.parameters=parameters;

    def __str__(self):
        return f"{self.symbol}, {self.function}, {self.precedence}, {self.parameters}";


