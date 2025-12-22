import math
import re
import json
import os

# esm elfile elly haytsgl feh elhistory
HISTORY_FILE = "history.json"

def calculate(expression: str):
    original_expression = expression # n7fzo abl el-replace
    
    # replace symbols 
    expression = expression.replace("÷", "/").replace("✖", "*")

    # persentage
    expression = re.sub(r'(\d+(\.\d+)?)%', r'(\1/100)', expression)

    # Replace cos and tan 
    expression = expression.replace("cos", "math.cos(math.radians")
    expression = expression.replace("tan", "math.tan(math.radians")
    
    # numbers after cos/tan
    expression = re.sub(r'math\.cos\(math\.radians(\d+(\.\d+)?)', r'math.cos(math.radians(\1))', expression)
    expression = re.sub(r'math\.tan\(math\.radians(\d+(\.\d+)?)', r'math.tan(math.radians(\1))', expression)

    result = eval(expression)
    
    # n7fz el3amlya fe eljson
    save_to_json(original_expression, result)
    
    return result

def save_to_json(op, res):
    data = []
    # nshof elfile mawgod wala la2
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []
    
    # n-insert eloperation elgdida fl awel
    data.insert(0, {"op": op, "res": res})
    
    # n5aly a5er 10 operations bs
    with open(HISTORY_FILE, "w") as f:
        json.dump(data[:10], f, indent=4)

def get_history_data():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                return json.load(f)
            except:
                return []
    return []