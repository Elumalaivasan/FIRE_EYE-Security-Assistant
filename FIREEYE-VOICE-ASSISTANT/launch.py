def launcher(command):
    import os
    words = command.split(" ")
    program = words[-1]
    if "terminal" in program:
        os.system("gnome-terminal &")
    return