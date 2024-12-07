# FIM
import os
import hashlib
import time
import shelve


monitor = [
    {
        'path': '/home/janus/projects/py35.dev/monitor/monitoring/recursive',
        'recursive': True
    },
    {
        'path': '/home/janus/projects/py35.dev/monitor/monitoring/no-recursive',
        'recursive': False
    },
]

def getFiles(monitor):
    filesList = []

    for x in monitor:
        if os.path.isdir(x['path']):
            if x['recursive']:
                filesList.extend([os.path.join(root, f) for (root, dirs, files) in os.walk(x['path']) for f in files])
            else:
                filesList.extend([item for item in os.listdir(x['path']) if os.path.isfile(item)])
        elif os.path.isfile(x['path']):
            filesList.append(x['path'])
    return filesList

def main():
    
    files = {}

    while True:
        for file in getFiles(monitor):

            hash = hashlib.sha256()

            with open(file) as f:
                for chunck in iter(lambda: f.read(2048), ""):
                    hash.update(chunck.encode("utf-8")) 

                    sha256 = hash.hexdigest()

                    if file in files and sha256 != files[file]:
                        print(f"{file} has been changed! {time.strftime('%Y-%m-%d %H:%M:%S')}")

                    files[file] = sha256

                    # print(file)

                    print(files)
                    with shelve.open('monit.db') as s:
                        s[file] = files[file]

                time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

