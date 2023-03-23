import subprocess
import os
import shutil

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
            file.write('\n'.join(lines[:variable_line+1]) + '\n' + f'builder.RootComponents.RegisterCustomElement<{RazorWidgetName}>("{NewComponentName}");' + '\n' + '\n'.join(lines[variable_line+1:]))
            file.truncate()
        
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def PublishComponents(directory: str) -> bool:
    result = subprocess.run(["dotnet", "publish"], shell=True, cwd=directory, check=True, capture_output=True)
    if result.returncode == 0:
        return True
    else:
        return False

def CopyAndPasteFolders(source: str, destination: str) -> bool:
    folders_to_copy = ['_content','_framework']
    success = False
    try:
        for folder in folders_to_copy:
            source_folder = os.path.join(source, folder)
            destination_folder = os.path.join(destination, folder)
            if os.path.isdir(source_folder):
                if os.path.exists(destination_folder):
                    print(f"Folder '{folder}' already exists in '{destination}', skipping copy.")
                else:
                    shutil.copytree(source_folder, destination_folder)
                    print(f"Successfully copied folder '{folder}' from '{source}' to '{destination}'.")
                success = True
            else:
                print(f"Folder '{folder}' not found in '{source}'.")
        return success
    except Exception as e:
        print(f"Error copying folder(s) from '{source}' to '{destination}': {e}")
        return success

def ChangeHTML(path: str):
    variable_name = "</body>"
    variable_line = None
    line1 = f'<script src="_framework/blazor.webassembly.js"></script>'
    line2 = f'<script src="_content/Microsoft.AspNetCore.Components.CustomElements/Microsoft.AspNetCore.Components.CustomElements.lib.module.js"></script>'

    try:
        with open(path, "r") as file:
            contents = file.read()
            lines = contents.splitlines()
        
        for i, line in enumerate(lines):
            if line1 in line or line2 in line:
                print("Scripts are already in the HTML file")
                return True
            if variable_name in line:
                variable_line = i
                break

        with open(path, "r+") as file:
            file.seek(0)
            file.write('\n'.join(lines[:variable_line]) + '\n' + line1 + '\n' + line2 + '\n'.join(lines[variable_line:]))
            file.truncate()
        
        return True


    except Exception as e:
        print(f"Error: {e}")
        return False
    
