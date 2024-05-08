import ast 
def get_function_name(code):
    # Parse the code
    tree = ast.parse(code)

    # Initialize a variable to store the function name
    function_name = None

    # Iterate through the parsed AST (Abstract Syntax Tree)
    for node in ast.walk(tree):
        # Check if the node is a function definition
        if isinstance(node, ast.FunctionDef):
            # Assign the name of the function to the variable
            function_name = node.name
            # Break out of the loop since we found the function
            break

    return function_name


def extract_function(code):
    # Parse the code into an AST
    tree = ast.parse(code)

    # Initialize a visitor that will find function definitions
    class FunctionVisitor(ast.NodeVisitor):
        def __init__(self):
            self.function_code = None
        
        def visit_FunctionDef(self, node):
            # Store the source code of the first function and stop further traversal
            if self.function_code is None:
                self.function_code = ast.unparse(node)
                raise StopIteration

    # Create a visitor instance and visit the nodes
    visitor = FunctionVisitor()
    try:
        visitor.visit(tree)
    except StopIteration:
        pass

    return visitor.function_code


