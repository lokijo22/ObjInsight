class Table:
    def __init__(self, rows: list[list[object]] = [], row_names: list[str] = [], column_names: list[str] = [], name = 'Table') -> None:
        self.name = name
        self.table = rows
        # Headers
        self.row_names = row_names
        self.column_names = column_names
        # string size of columns
        self.column_sizes = []
    
    def append_row(self, row):
        """
        Append a row to the table.

        Args:
            row (list): The row to append.
        """
        self.table.append(row)

    def append_col(self, col, title):
        """
        Append a column to the table.

        Args:
            col (list): The column to append.
            title (str): The title of the column.
        """
        # Add the column to each row
        for i, row in enumerate(self.table):
            row.append(col[i])
        
        # Add the title to the titles list
        self.column_names.append(title)

    def sort_by_column(self, col_idx):
        """
        Sort the rows of the table based on a certain column.

        Args:
            col_idx (int): The index of the column to sort by.
        """
        self.table.sort(key = lambda x: x[col_idx])

    def get_column(self, col_idx):
        # use list comprehension to get column
        column = [self.table[i][col_idx] for i in range(len(self.table))]

        return column

    def col_stat(self, col_widths, function, name:str):
        # Calculate the total values for each column
        row = [function(self.get_column(i+1)) for i in range(len(col_widths) - 1)]
        row.insert(0, f"{name.upper()}:")

        # Generate the stats row string
        out = self.list_to_row_string(row) + '\n'

        return out
    
    def get_types(self, columns = True) -> list[set]:
        """
        Gets a list of sets for each column or row 
        """
        
        types = []

        # lambda that returns either the column or row of a given index based on a boolean
        list_to_parse = lambda index : self.get_column(index) if columns else self.table[index]

        # get sets of the unique types of each column
        for index in range(len(self.column_sizes)):
            print(f"DEBUG: index: {index}")    
            item_types = [item.__class__.__name__ for item in list_to_parse(index)]
            types.append(set(item_types))
        
        return types

    def list_to_row_string(self, items:list, length = 0) -> str:
        length = len(items)
        print(f"DEBUG: items: {items}")
        # TEMPORARY: should work fine if the item strings are not longer than the column widths and the number of items are not greater than the number of columns
        return ' | '.join(str(items[i]).ljust(self.column_sizes[i]) for i in range(length))


    def get_column_sizes(self, items:list = None) -> list[int]:
        print(f"DEBUG: items: {items}")
        # WARNING! SPICY! complex list comprehension shenanigans
        if items is not None:
            return [len(str(i)) for i in range(len(items))]
        else:
            return [max(len(str(row[i])) for row in self.table) for i in range(len(self.table[0]))]

    def __str__(self):
        """
        Return a string representation of the table.
        """


        # Calculate the maximum width of each column
        self.column_sizes = self.get_column_sizes()

        # create horizontal seperator
        seperator = '-' * (sum(self.column_sizes) + len(self.column_sizes)) + '\n'

        # compare calculated maximim width with the length of the title
        for i, name in enumerate(self.column_names):
            self.column_sizes[i] = max(self.column_sizes[i], len(name))


        # Create the string representation of the table
        table_str = f"{self.name}\n"

        if self.column_names:
            table_str += self.list_to_row_string(self.column_names) + '\n'
            table_str += seperator
        
        for row in self.table:
            table_str += self.list_to_row_string(row) + '\n'
        
        table_str += seperator

        # Types Section
        table_str += "Types\n"

        table_str += self.list_to_row_string(self.get_types()) + '\n'

        table_str += seperator

        # Stats Section
        table_str += "Statistics\n"

        table_str += self.col_stat(self.column_sizes, sum, "Total")
        table_str += self.col_stat(self.column_sizes, lambda x: round(sum(x) / len(x)), "Average")
        table_str += self.col_stat(self.column_sizes, max, "Max")
        table_str += self.col_stat(self.column_sizes, min, "min")

        return table_str