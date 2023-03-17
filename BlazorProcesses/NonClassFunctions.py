import subprocess

def WriteToProgramFile(RazorWidgetName: str, NewComponentName: str, path: str) -> bool:
    variable_name = "WebAssemblyHostBuilder.CreateDefault"
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
            file.write('\n'.join(lines[:variable_line+1]) + '\n' + f'builder.RootComponents.RegisterCustomElement<{RazorWidgetName}>("{NewComponentName}")' + '\n' + '\n'.join(lines[variable_line+1:]))
            file.truncate()
        
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def PublishComponents(directory: str) -> bool:
    result = subprocess.run(['dotnet publish'], shell=True, cwd=directory, check=True, capture_output=True)
    if result.returncode == 0:
        return True
    else:
        return False


