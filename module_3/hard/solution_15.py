# Write a function draw_shape(shape, size, char="*") that draws a given shape (like a square or triangle) using an optional character. The shape type can be "square" or "triangle".

def draw_shape(shape, size, char="*"):
    """
    Draws a given shape (square or triangle) using an optional character.
    
    Parameters:
    shape (str): The type of shape to draw ("square" or "triangle").
    size (int): The size of the shape (e.g., side length for square, height for triangle).
    char (str): The character to use for drawing the shape. Default is "*".
    
    Raises:
    ValueError: If the shape is not "square" or "triangle".
    """
    if shape == "square":
        for i in range(size):
            print(char * size)
    elif shape == "triangle":
        for i in range(1, size + 1):
            print(char * i)
    else:
        raise ValueError("Shape must be 'square' or 'triangle'")

print("Square:")
draw_shape("square", 5, "#")

print ("Triangle:\n")
draw_shape("triangle",5, "*")


