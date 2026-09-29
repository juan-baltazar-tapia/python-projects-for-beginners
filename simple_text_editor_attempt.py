from pathlib import Path


def valid_file_name(user_input):
    return not (user_input.find('/') and user_input[-4:] != '.txt')
    
def get_user_content(file_name):
    print("Enter your text (type SAVE on a new line to save and exit):")
    content = ''
    while True:
        line = input().strip()
        if line == "SAVE":
            break
        content += line + '\n'
    print(f"File {file_name} saved")
    return content
        
def display_content(file_name):
    return Path(file_name).read_text()

def get_user_input():
    while True:
        user_input = input("Enter the filename to open or create: ").strip()
        if valid_file_name(user_input):
            break
        print("Invalid txt file")
    return user_input  

def write_or_edit_file(file_name, txt_files):
    if Path(file_name) in txt_files:
        print(display_content(file_name))
    content = get_user_content(file_name)
    Path(file_name).write_text(content)
     
def main():
    file_name = get_user_input()
    txt_files = list(Path('.').glob('*.txt'))
    write_or_edit_file(file_name, txt_files)


if __name__ == '__main__':
    main()
