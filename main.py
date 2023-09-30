import os
from datetime import datetime
import github

now = datetime.now()
categories = ['SWEA', '백준', '프로그래머스']
numbers = ['1️⃣', '2️⃣', '3️⃣']
content = f"""# {github.repository}\n<p align="right"> 최종업로드: {now.strftime('%Y-%m-%d %H:%M:%S')} </p>\n\n"""
count = 0

def write(category):
    global content, count

    addr = github.localDir + f'/{category}/'

    if os.path.isdir(addr):
        content += """\n<br/>\n\n"""
        content += f"""### {numbers[count]} {category}\n"""
        count += 1

        content += """| Level | Number |\n| :------: | ------ |\n"""
        levels = os.listdir(addr)

        for level in levels:
            files = os.listdir(addr + level)
            content += f"""| {level} | """
            for file in files:
                num = file.find('.')
                content += f"""[{file[0:num]}]({github.link}/{category}/{level}/{file}), """
            content += """ |\n"""

def main():
    github.pull()
    
    for category in categories: write(category)
   
    # Write README.md
    with open(github.localDir + '/README.md', 'w', encoding='UTF8') as readme:
        readme.write(content)
    
    github.push()

if __name__ == '__main__':
    main()