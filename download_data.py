from pathlib import Path
import shutil
import requests
from tqdm import tqdm
import zipfile
from zipfile import ZIP_DEFLATED, ZIP_LZMA

root_url = "https://kpolyakov.spb.ru/download/"
archive_names = ['24data.zip', '26data.zip', '27data.zip']

dirpath = Path('./data')
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)
    print('Deleted old data files')

if not dirpath.exists():
    dirpath.mkdir()

for i, name in enumerate(archive_names):
    print('[{} / {}] Downloading {}'.format(i+1, len(archive_names), name))
    response = requests.get(root_url + name, stream=True)

    with open("./data/" + name, "wb+") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)

    # with zipfile.ZipFile("./data/" + name, "r", ZIP_LZMA) as zip_ref:
    #     unzip_directory_name = name.split('.')[0]
    #     Path('./data/' + unzip_directory_name).mkdir()
    #     zip_ref.extractall('./data/' + unzip_directory_name)

print('Done')