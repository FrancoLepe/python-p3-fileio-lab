# def write_file(file_name, file_content):
#     write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )

# with open('log_file.txt', mode='w', encoding='utf-8') as log_file:
#     log_file.write('Log 1')

def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt') as f:
        return f.read()