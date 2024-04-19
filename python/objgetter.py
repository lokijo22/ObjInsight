import pefile

def create_object_dict(obj):
    obj_dict = {}
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    for attr in attributes:
        value = getattr(obj, attr)
        obj_dict[attr] = value

    return obj_dict

def process_entries(dictionary):
    try:
        for key, item in dictionary.items():
            item = create_object_dict(item)

    except Exception as e:
        print(e)

def format_dict(dict, flag = False):
    """
    Format dictionaries or dictionary-like objects into a string.

    Parameters:
        data: dict or dict-like object - The data to format.
        flag: Boolean - a flag which indicates whether the 

    Returns:
        str: The formatted string.
    """
    result = ""

    #generate string from data
    for category, item in dict.items():
        result +=  f"\n\n {category}\n  class: {str(type(item).__name__)}"
    
    return result

path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Noita\\noita.exe"
pe = pefile.PE(path)

# Get a list of variable names and their contents
variables_with_contents = {var: getattr(pe, var) for var in dir(pe) if not callable(getattr(pe, var)) and not var.startswith("__")}

# Get a list of method names
methods = [method for method in dir(pe) if callable(getattr(pe, method)) and not method.startswith("__")]


print(path)

dictionary = create_object_dict(pe)
process_entries(dictionary)

print(format_dict(dictionary))