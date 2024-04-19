
def sum(numbers: list[int]):
    """
    
    Args:
      numbers: a list of integers
    
    Returns:

    """
    
    total = 0
    
    #iterates through all items and adds them together
    for number in numbers:
        total += number
    
    #returns the sum of all items in the list
    return total


def format_list(list):
  output = '\n'

  for index in range(len(list)):
    item = list[index]
    output += f'{str(item)}\n'

  return output


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


def format(object):
   objecttype = object.__class__.__name__

   match objecttype:
    case 'dict':
        return format_dict(object)

    case 'list':
        return format_list(object)
    
    case 'int','str', 'boolean', 'float':
        return str(object)

    case _:
         print(f"unrecognized object - {objecttype} object - {object}")


"""
This function is intended to display the available information 
about a given list of objects. 

for now it simply shows iformation on the types of the objects in
the class.
"""
def analyze_list(list: list):


    #ititialize lists for data storage
    types = []
    type_count = []

    index = 0
    for item in list:
        #get information from the item
        item_type = item.__class__

        #save type if it is does not have the same type as another item in the list
        if types != []:
            for i in range(len(types)):
                test = types[i]
                if test != item_type and index != i:
                    types.append(item_type)
                    type_count.append(0)
                elif index != i:
                    pass
                else:
                    type_count[i] += 1
        else:
            types.append(item_type)
            type_count.append(0)
    
    out = ''

    out += format(types)
    
    out += format(type_count)

    return out


def analyze_function(function):
    #get a list of the attributes of the function
    attributes = function.__dir__()

    #Title
    print(f"\nFunction - ", end = '')

    #function name
    print(function.__name__)

    #attribute list details
    print(analyze_list(attributes))

    #attributes
    print(format(attributes))

def main():

    analyze_function(sum)

main()