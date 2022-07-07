from pathlib import Path
import shutil
import requests
from tqdm import tqdm
import zipfile
from zipfile import ZIP_DEFLATED, ZIP_LZMA
import argparse

root_url = "https://kpolyakov.spb.ru/download/"
archives_names = ['24data.zip', '26data.zip', '27data.zip']
file_names = ['answers.csv'] + archives_names

if __name__ == '__main__':
    print('\n Welcome to kpolyakov.spb.ru files downloader by Dmitry Kochetkov!\n')

    parser = argparse.ArgumentParser(description='Downloads problem files and answers from https://kpolyakov.spb.ru')
    parser.add_argument('-f', metavar='force', action=argparse.BooleanOptionalAction, help='Force removal of data directory.')
    args = parser.parse_args()

    dirpath = Path('./data')
    if dirpath.exists() and dirpath.is_dir():
        if args.f != True:
            print('Directory ./data already exists. Use -f key to remove it.')
            exit()
        
        shutil.rmtree(dirpath)
        print('Erased ./data directory.')

    if not dirpath.exists():
        dirpath.mkdir()
        print('Created empty ./data directory')
        print()

    print('Downloading files...')
    for i, name in enumerate(file_names):
        print('[{} / {}] Downloading {}'.format(i+1, len(file_names), name))
        response = requests.get(root_url + name, stream=True)

        with open("./data/" + name, "wb+") as handle:
            for data in tqdm(response.iter_content()):
                handle.write(data)

    print('Download complete.')
    print()
    print('Extracting ZIP archives...')

    for i, archive_name in enumerate(archives_names):
        print('[{} / {}] Extracting {}'.format(i+1, len(file_names), archive_name))
        
        folder_name = archive_name.split('.')[0]
        Path('./data/' + folder_name).mkdir()
        with zipfile.ZipFile("./data/" + archive_name, "r", ZIP_DEFLATED) as f:
            for name in tqdm(f.namelist()):
                try:
                    f.extract(name, path="./data/" + folder_name + "/")
                    if name.split('.')[-1] == 'zip':
                        with zipfile.ZipFile('./data/' + folder_name + "/" + name, "r") as f2:
                            f2.extractall('./data/' + folder_name + "/" + name.split('.')[0])
                except zipfile.BadZipfile:
                    print('\nUnable to extract file', name)

    print('Done')