import math
import re

def calculate(expression: str):
    # Replace symbols 
    expression = expression.replace("÷", "/").replace("✖", "*")

    # persentage
    expression = re.sub(r'(\d+(\.\d+)?)%', r'(\1/100)', expression)

    # Replace cos and tan 
    expression = expression.replace("cos", "math.cos(math.radians")
    expression = expression.replace("tan", "math.tan(math.radians")
 # numbers after cos/tan
    expression = re.sub(r'math\.cos\(math\.radians(\d+(\.\d+)?)', r'math.cos(math.radians(\1))', expression)
    expression = re.sub(r'math\.tan\(math\.radians(\d+(\.\d+)?)', r'math.tan(math.radians(\1))', expression)

    return eval(expression)