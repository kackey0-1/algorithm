import os
import pathlib

print(os.path.exists('data/test.csv'))
print(os.path.isfile('data/test.csv'))
print(os.path.isdir('data/'))

# pathlib.Path('data/test.txt').touch()
# os.rename('data/test.txt','data/text.txt')

print(os.listdir('data'))
print(os.getcwd())

"""
tarfile
"""
import tarfile

with tarfile.open('data/test.tar.gz', 'w:gz') as tr:
    tr.add('data')

with tarfile.open('data/test.tar.gz', 'r:gz') as tr:
    tr.extractall(path='data')
    # with tr.extractfile('data')



"""
zipfile
"""
import zipfile
import glob
with zipfile.ZipFile('data/test.zip', 'w') as z:
    # z.write('data')
    # z.write('data/test.csv')
    for f in glob.glob('data/**', recursive=True):
        print(f)
        z.write(f)

with zipfile.ZipFile('data/test.zip', 'r') as z:
    z.extractall('hogehoge')
    with z.open('data/test.csv') as f:
        print(f.read())
