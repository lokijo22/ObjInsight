def create_object_dict(obj):
    obj_dict = {}
    attributes = [attr for attr in dir(obj)]

    for attr in attributes:
        value = getattr(obj, attr)
        obj_dict[attr] = value

    return obj_dict


def format_dictionary(dictionary, indent=2):
    """Formats a dictionary for easy reading."""
    
    formatted_string = "{\n"
    
    for key in dictionary._order:
        value = dictionary.get_by_index(dictionary._order.index(key))
        formatted_string += f"{' ' * indent}'{key}': {value},\n"
    
    formatted_string += "\n}"
    
    return formatted_string


def generate_object_summary(obj):
    """Generate a summary of object attributes and methods."""
    directory = dir(obj)

    #if it exists add variable name to the string
    try:
        directory_summary = f"{obj.__name__}\n\n"
    except Exception:
        pass
    #if not then if the variable's class exists add that to the string
    try:
        directory_summary = f"{obj.__class__.__name__} object\n\n"
    except Exception:
        pass

    variables = "Variables -\n"
    methods = "Methods -\n"

    description = obj.__doc__
    directory_summary += f"{description}\n\n"

    for item_name in directory:
        # Detect whether the directory item is a method or a variable
        is_method = callable(getattr(obj, item_name, None))
        
        # Build the summary string with information about each item
        if is_method:
            if item_name != "__class__":
                methods += f"  {item_name}\n  {getattr(obj, item_name).__doc__}\n\n"
        else:
            if item_name != "__doc__":
                value = getattr(obj, item_name)
                variables += f"  {item_name}\t: {value.__class__.__name__}\n" 
    
    directory_summary += f"{variables} \n{methods} \n"
    return directory_summary


# Example usage:
number = 5

# Create an IndexedDict of the object attributes
obj_dict = create_object_dict(number)

# process entries
for key, item in obj_dict.items():
    item = create_object_dict(item)

directory_info = generate_object_summary(number)

print("OBJECT SUMMARY:\n\n" + directory_info)
