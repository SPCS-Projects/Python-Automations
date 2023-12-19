import os
import urllib.request
import pathlib
from threading import Thread


def download_link(link, file_path):
    urllib.request.urlretrieve(link, file_path)


def get_names(links, path):
    paths = []
    names = []
    link_list = []
    for link in links:
        link = link.rstrip()
        path_object = pathlib.Path(path + "\\" + link[26:])
        paths.append(path_object.parent)
        names.append(path_object)
        link_list.append(link)
    return names, paths, link_list


def download(rel_path):
    files_processed = 0
    path = os.path.dirname(os.path.realpath(__file__))
    url_list = path + rel_path
    links = open(url_list, 'r')
    names, paths, linkz = get_names(links, path)
    for i in range(len(paths)):
        if not os.path.isdir(paths[i]):
            os.makedirs(paths[i])
        Thread(target=download_link, args=(linkz[i], names[i],)).start()
        files_processed += 1
        print("Currently Processed: {}".format(files_processed))


rel_path = "/links.txt"
download(rel_path)
