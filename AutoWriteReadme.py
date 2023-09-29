# pip install gitpython
import git
import os

# write your information
userName = 'SSangRRae'
repo = 'ProblemSolving'

# config remote repo
branch = 'tree/main'
addr = f'https://github.com/{userName}/{repo}'
link = f'{addr}/{branch}'

# config local repo
localDir = 'C:/git/' + repo

HEADER = """# ProblemSolving\n"""
repo = git.Repo(localDir)

def pullRepo():
    # Pull repo
    print('...pull')
    repo.remotes.origin.pull()

def make():
    content = ""
    content += HEADER

    # 1. SWEA
    content += """### 1️⃣ SWEA\n"""

    if os.path.isdir(localDir + '/SWEA'):
        content += """| Level | Number |\n| :------: | :------: |\n"""
        levels = os.listdir(localDir + '/SWEA')

        for level in levels:
            files = os.listdir(localDir + '/SWEA/' + level)
            content += f"""| {level} | """
            for file in files:
                num = file.find('.')
                content += f"""[{file[0:num]}]({link}/SWEA/{level}/{file}), """
            content += """ |\n\n"""
    
    # 2. BOJ
    content += """### 2️⃣ BOJ\n"""

    if os.path.isdir(localDir + '/백준'):
        content += """| Level | Number |\n| :------: | :------: |\n"""
        levels = os.listdir(localDir + '/백준')

        for level in levels:
            files = os.listdir(localDir + '/백준/' + level)
            content += f"""| {level} | """
            for file in files:
                num = file.find('.')
                content += f"""[{file[0:num]}]({link}/백준/{level}/{file}), """
            content += """ |\n\n"""

    # Write README.md
    with open(localDir + '/README.md', 'w', encoding='UTF8') as readme:
        readme.write(content)

def pushRepo():
    print('...push')
    repo.index.add('**')
    repo.index.commit('Update README.md')
    repo.remotes.origin.push()

def main():
    pullRepo()
    make()
    pushRepo()

if __name__ == '__main__':
    main()