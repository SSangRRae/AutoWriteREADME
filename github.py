# pip install gitpython
import git

# write your information
userName = 'SSangRRae'
repository = 'ProblemSolving'

# config remote repo
branch = 'tree/main'
addr = f'https://github.com/{userName}/{repository}'
link = f'{addr}/{branch}'

# config local repo
localDir = 'C:/git/' + repository
repo = git.Repo(localDir)

def pull():
    # Pull repo
    print('...pull')
    repo.remotes.origin.pull()

def push():
    print('...push')
    repo.index.add('README.md')
    repo.index.commit('Update README.md')
    repo.remotes.origin.push()