def WriteToProgramFile(code, path) -> None:
    with open(path, 'a') as file:
       file.write(code + '\n')