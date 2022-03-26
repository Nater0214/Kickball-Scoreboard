# inputloop.py
# Prompts the user for an input until criteria are met


# Methods
def inputloop(prompt: str, end: str, checkfor_type: str, checkfor: tuple = None):
    """Prompt the user for an input until criteria are met"""
    
    if checkfor_type == 'options':
        return _options(prompt, end, checkfor)
    elif checkfor_type == 'len':
        return _len(prompt, end, checkfor)
    elif checkfor_type == 'int':
        return _int(prompt, end, checkfor)
    elif checkfor_type == 'range':
        return _range(prompt, end, checkfor)
    else:
        raise ValueError("Expected a valid type of item to check for")


def _options(prompt, end, options):
    """Input that checks for options"""
    
    inp = ''
    while inp not in options: # Loop
        inp = input(f"{prompt} ({', '.join(options)}){end} ")
    
    return inp


def _len(prompt, end, lengths):
    """Input that checks until a input string is a certain length"""

    inp = ''
    while len(inp) not in lengths: # Loop
        inp = input(f"{prompt} (Len of {', '.join(str(i) for i in lengths)}){end} ")
    
    return inp


def _int(prompt, end, requirements = None):
    """Input that checks for an integer"""

    if 'requirements' in locals():
        # Error checking
        requirements_check = requirements[0]
        if requirements_check not in ('>', '<', '>=', '<='):
            raise ValueError("Expected reqiremets check to be a valid operator")
        
        requirements_value = requirements[1]
        if not(isinstance(requirements_value, int)):
            raise ValueError("Expected requrements value to be an integer")

        inp = ''
        while not(inp.isdigit() and eval(f"{inp} {requirements_check} {requirements_value}")): # Loop
            inp = input(f"{prompt} ({requirements_check} {str(requirements_value)}){end} ")
        
        return int(inp)
    else:
        inp = ''
        while not(inp.isdigit()):
            inp = input(f"{prompt} (int){end}")


def _range(prompt, end, range_):
    """Input that checks for a value in a range"""

    range_low = range_[0]
    range_high = range_[1]

    inp = ''
    while not(inp in range(range_low, range_high + 1)):
        try:
            inp = int(input(f"{prompt} ({range_low} - {range_high}){end} "))
        except:
            pass
    
    return inp