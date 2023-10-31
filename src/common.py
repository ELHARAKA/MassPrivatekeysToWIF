"""
Common function used in both compressed and uncompressed files.
"""

def process_file(file_path, conversion_function):
    """
    Process a file with a specified conversion function.
    """
    with open(file_path, encoding='utf-8') as file_handle:
        for line in file_handle:
            print(str.strip(line))
            conversion_function(str.strip(line))
