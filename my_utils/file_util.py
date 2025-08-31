def print_file(file_name):
    f = None
    try:
        f = open(file_name, 'r', encoding='utf-8')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if f:
            f.close()
        else:
            print(f"File {file_name} not found.")
def append_to_file(file_name, data):
    f = open(file_name, 'a', encoding='utf-8')
    f.write(data)
    f.write('\n')
    f.close()