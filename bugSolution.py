def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # Process the file here...
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
#Alternative solution with explicit close
def function_with_explicit_close(filename):
    try:
        f = open(filename, 'r')
        # Process the file here...
        for line in f:
            print(line.strip())
        f.close() #Close the file explicitly
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}") 