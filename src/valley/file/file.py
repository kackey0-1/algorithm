import os
import pathlib

print(os.path.exists('data/test.csv'))
print(os.path.isfile('data/test.csv'))
print(os.path.isdir('file/'))

# pathlib.Path('file/test.txt').touch()
# os.rename('file/test.txt','file/text.txt')

print(os.listdir(''))
print(os.getcwd())

"""
tarfile
"""
import tarfile

with tarfile.open('data/test.tar.gz', 'w:gz') as tr:
    tr.add('file')

with tarfile.open('data/test.tar.gz', 'r:gz') as tr:
    tr.extractall(path='')
    # with tr.extractfile('file')


"""
zipfile
"""
import zipfile
import glob
with zipfile.ZipFile('data/test.zip', 'w') as z:
    # z.write('file')
    # z.write('file/test.csv')
    for f in glob.glob('data/**', recursive=True):
        print(f)
        z.write(f)

with zipfile.ZipFile('data/test.zip', 'r') as z:
    z.extractall('hogehoge')
    with z.open('data/test.csv') as f:
        print(f.read())

