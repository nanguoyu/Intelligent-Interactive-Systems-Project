"""
@File : DownloadWeights.py
@Author: Dong Wang
@Date : 2020/5/12
"""
import sys
import requests
import os

requests.packages.urllib3.disable_warnings()


def download(url, file_path):
    r1 = requests.get(url, stream=True, verify=False)
    total_size = int(r1.headers['Content-Length'])
    if os.path.exists(file_path):
        temp_size = os.path.getsize(file_path)
    else:
        temp_size = 0
    print("Downloaded size", temp_size)
    print("Total size", total_size)
    headers = {'Range': 'bytes=%d-' % temp_size}
    r = requests.get(url, stream=True, verify=False, headers=headers)

    with open(file_path, "ab") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                temp_size += len(chunk)
                f.write(chunk)
                f.flush()
                done = int(50 * temp_size / total_size)
                sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                sys.stdout.flush()
    print()


if __name__ == '__main__':
    url = "https://github.com/nanguoyu/Intelligent-Interactive-Systems-Project/releases/latest/download/"
    models = ["End2endWeights-best.hdf5", "Sub1-weights-best.hdf5", "Sub2-weights-best.hdf5"]
    folder = "model/"
    for model in models:
        print("[Downloader]: ", url + model)
        download(url + model, folder + model)
