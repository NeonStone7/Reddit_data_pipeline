import re
with open('requirements.txt', 'r') as file:
    lines = file.readlines()


clean_lines = [f"{x.split('=')[0]}=={x.split('=')[1]}\n" for x in lines]


with open('requirements.txt', 'w') as file:
    file.writelines(clean_lines)
