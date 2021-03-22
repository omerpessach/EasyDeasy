

def parse_image_name_from_path(path: str) -> str:
    """
    Parses the name of the image includes it's type (jpg, png etc..) from the given path
    """
    last_index = path.rfind('/')

    # found occurrence of '/'
    if last_index:
        name = path[last_index + 1:]
    else:
        name = ""

    return name

