# inputloop.py
# Prompts the user for an input until criteria are met


# Methods
from click import option


def inputloop(prompt, checkfor_type, checkfor):
    """Prompt the user for an input until criteria are met"""

    if checkfor_type not in ["options"]: # Check if checkfor_type is a valid type
        raise ValueError("Expected a valid type of item to check for")
    
    if checkfor_type == "options":
        __optioninput(prompt, checkfor)


def __optioninput(prompt, options):
    """Input that checks for options"""

    if isinstance(options, list): # Check if options is a list
        raise ValueError("Expected list of options for checkfor_type options")
    
    while inp not in options:
        inp = input(f"{prompt} ({','.join(options)}) ")
    
    return inp