import os
from datetime import datetime
import logging

import conf.env_config as conf


def fs_tree_to_dict(path):
    file_token = ''
    for root, dirs, files in os.walk(path):
        tree = {d: fs_tree_to_dict(os.path.join(root, d)) for d in dirs}
        tree.update({f: file_token for f in files})
        return tree  # note we discontinue iteration trough os.walk


class DirComparator:
    def __init__(self, E):
        self.E = E
        pass

    def get_file_tree(self, dir):
        logging.info(f'Checking directory {dir} ...')
        onlyfiles = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]

        f = []
        for (dirpath, dirnames, filenames) in os.walk(dir):
            f.extend((dirpath, filenames))

    def list_files(self, startpath):
        import pdb; pdb.set_trace()
        tree = {startpath: {}}
        dict_p = tree
        for dir, dirs, files in os.walk(startpath):
            level = dir.replace(startpath, '').count(os.sep)

            if not dir in dict_p:
                pass

            d = dict_p[dir]
            for x in dirs:
                d[x] = {}

            for f in files:
                # Get details of f
                (_, _, _, _, _, _, size, atime, mtime, ctime) = os.stat(os.path.join(dir, f))
                ctime = datetime.fromtimestamp(ctime)
                mtime = datetime.fromtimestamp(mtime)
                atime = datetime.fromtimestamp(atime)


            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(dir)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))

    @staticmethod
    def main():
        conf.env_config()

        dc = DirComparator(conf.E)

        d1 = 'C:\\Users\\Lei\\Downloads\\~software\\win\\reg\\vid'
        # dc.get_file_tree(d1)
        dc.list_files(d1)


if __name__ == '__main__':
    DirComparator.main()
