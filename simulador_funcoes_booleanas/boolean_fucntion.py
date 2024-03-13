RESERVED_CHARS = ["+","*","(",")","'",]
class boolean_function:
    @staticmethod
    def variables(function: str) -> list:
        variables = []
        for char in function:
            if char not in RESERVED_CHARS:
                if char is not " ":
                    char.upper()
                    variables.append(char)
        return variables

    @staticmethod
    def get_value_variables(variables: list) -> dict:
        variables_values = {}
        for var in variables:
            value = int(input(f"Digite o valor da variavel {var}, 0 ou 1: "))
            variables_values[var] = value
        return variables_values

    @staticmethod
    def build_function(function: str, variables_values: dict) -> str:
        new_fucntion = ""
        for char in function:
            if char is not " ":
                if char not in RESERVED_CHARS:
                    char.upper()
                    value = variables_values[char]
                    new_fucntion += str(value)
                    new_fucntion += " "
                if char == "'":
                    if new_fucntion[-2] == ")":
                        i = 0
                        position = 100
                        for char in new_fucntion:
                            if char == "(":
                                position = i
                            i += 1
                        if(position is not 100):
                            tp = new_fucntion[position:]
                            new_fucntion = new_fucntion[:position]
                            new_fucntion += 'not '
                            new_fucntion += tp
                    else:
                        temp = new_fucntion[-2]
                        new_fucntion = new_fucntion[:-2]
                        char = 'not '
                        new_fucntion += char
                        new_fucntion += temp
                        new_fucntion += " "
                if char == "+":
                    new_fucntion += "or "
                if char == "*":
                    new_fucntion += "and "
                if char == "(":
                    new_fucntion += "( "
                if char == ")":
                    new_fucntion += ") "
        return new_fucntion

    @staticmethod
    def eval_function(function: str) -> int:
        evaluado =  eval(function)
        if evaluado == True:
            return 1
        elif evaluado == False:
            return 0
        else:
            return evaluado
# (A AND B OR (C)')