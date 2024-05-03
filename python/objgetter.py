

def session_modules():
    #short script for listing modules currently imported into this session
    import sys

    #use sys library to get a dictionary of all imports in the current session
    modules = sys.modules

    return modules

def get_all_modules():
    # dynamic importing
    import importlib
    # files and folders
    import os

    # path to python library
    path = "C:\\Users\\" + input("Enter name of User: ") + "\\AppData\\Local\\Programs\\Python\\Python312\\Lib"

    #modules that are already in the session
    active_modules = session_modules()

    # modules that should not be imported regardless
    # antigravity and this are joke modules
    # tty and pty require termios and curses requires _curses
    # typing.re is depreciated
    ignore = ['antigravity', 'crypt', "this", "tty","pty", "curses","re"]
    
    directory = os.listdir(path)

    for item in directory:
        # remove .py suffix
        if item.endswith(".py"):
            item = item.removesuffix(".py")

        # test if the current item is already in the current session
        already_imported = active_modules.__contains__(item)

        # check if this import needs to be ignored
        do_ignore = ignore.__contains__(item)

        # import the module if it is not already in the session
        if (not already_imported) and (not do_ignore):
            try:
                importlib.import_module(item)
            except Exception as e:
                print(f"Failed to Import {item}: {e}")

        

def main():
    from ObjInsight import ObjInsight
    import table #type: ignore
    import warnings

    #stop showing those pesky warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # import all modules that are not already imported
    get_all_modules()

    # get and store modules in the current session
    modules = session_modules()

    #create a table object to be able to nicely print and handle the data
    data = table.Table(row_names = list(modules.keys()), column_names = ["Module Name", "Methods", "Variables", "Publics", "Privates", "Total Attributes"])
    

    # add data entries
    for key, object in list(modules.items()):
        # initialize Object Insight Instance for element in the dictionary
        item = ObjInsight(object)
        columns = [item.methods, item.variables, item.publics, item.privates, item.all]
        
        # create row list
        row = []

        # get data from object and append it to the list
        for function in columns:
            row.append(len(function()))

        # add retrieved data to the table
        data.append_row(row)
    
    # sort data samllest to greatest in decending order
    data.sort_by_column(3)

    # show results
    print(data)

import time

# time program execution
start = time.time()
main()
end = time.time()

# return 
print(f"Program executed in {round(end-start, 2)} seconds")