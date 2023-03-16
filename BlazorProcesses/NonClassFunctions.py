def WriteToProgramFile(code, path) -> bool:
    variable_name = "var builder"
    variable_line = None

    try:
        with open(path, 'r') as file:
            contents = file.read()
            lines = contents.splitlines()

        for i, line in enumerate(lines):
            if variable_name in line:
                variable_line = i
                break

        if variable_line is None:
            raise ValueError(f"Variable {variable_name} not found in file.")

        with open(path, 'r+') as file:
            file.seek(0)
            file.write('\n'.join(lines[:variable_line+1]) + '\n' + code + '\n' + '\n'.join(lines[variable_line+1:]))
            file.truncate()
        
        print("here")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

