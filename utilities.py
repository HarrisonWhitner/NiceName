def file_to_array(string):
    with open(string, 'r') as openFile:
        return openFile.read().splitlines()

def print_name_data(label, name):
    return label + "\t" + name + "\n"