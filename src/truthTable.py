from src.specificExpression import *
from src.classes.BooleanData import BooleanData

def truthTable_generator(expression, variables):
    num_variables = len(variables)
    num_rows = 2**num_variables
    min_width = 7 

    header = " | ".join(var.center(min_width) for var in variables)
    header = header + " | " + expression.center(min_width)
    header_len = len(header)
    print("-" * header_len)
    print(header)
    print("-" * header_len)

    for i in range(num_rows):
        row_binary = bin(i)[2:].zfill(num_variables)
        values = [True if bit == '1' else False for bit in row_binary]
        boolean_data_vector = [BooleanData(var, val) for var, val in zip(variables, values)]

        try:
            result = resolve_expression(expression, boolean_data_vector)
            result_str = str(result)
        except Exception as e:
            result_str = f"Error: {type(e).__name__} - {e}"

        row_elements = [str(val) for val in values] + [result_str]
        formatted_row = " | ".join(elem.center(min_width) for elem in row_elements)
        print(formatted_row)
        print("-" * header_len)

