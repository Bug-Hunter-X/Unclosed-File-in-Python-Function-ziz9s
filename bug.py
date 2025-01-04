def function_with_unclosed_file(filename):
    try:
        f = open(filename, 'r')
        # Process the file here...
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    # Missing f.close() or other resource management