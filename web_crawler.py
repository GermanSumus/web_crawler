import os


# each website crawled will get a new project folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

create_project_dir('testfile')
