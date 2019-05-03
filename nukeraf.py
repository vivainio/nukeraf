import tempfile, os, uuid, shutil
from os.path import join

trashcan = os.path.join(tempfile.gettempdir(), "nukeraf")

#trashcan = join(os.path.splitdrive(os.getcwd())[0], "/$Recycle.Bin/nukeraf")
print(trashcan)

if not os.path.isdir(trashcan):
    os.makedirs(trashcan)


def randname():
    return uuid.uuid4().hex


trash_work = join(trashcan, randname())
os.makedirs(trash_work)


def purge_dir(pth: str):
    print("Purge", pth)


def nuke_dir(pth):
    pth = os.path.abspath(pth)
    td = os.path.join(trash_work, randname())
    os.rename(pth, td)


def git_clean():
    garbage = os.popen("git ls-files -o --directory", "r").readlines()
    for d in garbage:
        nuke_dir(d.strip())

    purge_dir(trashcan)


git_clean()
