from pathlib import Path


# path = Path('my_name.txt')
# contents = path.read_text()
# print(contents)

new_path = Path("new_file.txt")

file_text = "Today was a day that was being a day.\n"

file_text += "We learnt how to open .txt files in python"

new_path.write_text(file_text)
print(new_path.read_text())
