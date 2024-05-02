class ObjInsight:
    def __init__(self, object) -> None:
        #create object dictionary
        self.object_dict = self.create_object_dict(object)

    def create_object_dict(self, obj):
        obj_dict = {}

        #create a dictionary entry for each attribute
        for attr in dir(obj):
            #get attribute from string
            value = getattr(obj, attr)
            
            #create dictionary entry of "name of attribute" : attribute
            obj_dict[attr] = value

        return obj_dict

    def variables(self):
        """
        Returns a dictionary of all the non-callble attributes
        """
        # create a filter method for variables
        filter = lambda item: not callable(item)

        # store filtered dictionary
        variable_dict = self.filter(filter)
        
        return variable_dict
    
    def methods(self):
        """
        Returns a dictionary of all the callble attributes
        """
        # create a filter method for methods
        filter = callable

        # store filtered dictionary
        variable_dict = self.filter(filter)
        
        return variable_dict

    def all(self):
        return self.object_dict
    
    def privates(self):
        # create filter for privates
        filter = lambda x : str(x).startswith("__")

        # store filtered dictionary
        variable_dict = self.filter(filter)
        
        return variable_dict

    def publics(self):
        # create filter method for publics
        filter = lambda x : not str(x).startswith("__")

        # store filtered dictionary
        variable_dict = self.filter(filter)
        
        return variable_dict


    def filter(self, filter):
        """
        Passes all attributes in the dictionary through the method given.
        if the result of an attribute passing through the method is true,
        add it to a new dictionary. this dictionary is returned when
        it finsihed filtering all the attributes.

        Args:
            filter: a function that acts as a filter for the attributes

        Returns:
            dict: a dictionary of all the passing attributes
        """
        # Initialize new dictionary to store filtered results
        items = {}

        # Repeat the filter method for every item in the dictionary
        for name, item in self.object_dict.items():  # Use .items() to iterate over key-value pairs
            # Test if passing item through the filter results in True
            if filter(item):
                # If it does pass the filter, store it in the new dictionary
                items[name] = item

        return items