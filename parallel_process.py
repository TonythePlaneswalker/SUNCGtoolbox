import os
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
from termcolor import colored


base_dir = '/data/SUNCG'
with open(os.path.join(base_dir, 'train_sceneId.txt')) as file:
    train_ids = file.read().splitlines()
with open(os.path.join(base_dir, 'test_sceneId.txt')) as file:
    test_ids = file.read().splitlines()
scene_ids = train_ids + test_ids
commands = ['./process_houses.sh %s' % os.path.join(base_dir, 'house', scene_id) for scene_id in scene_ids]

nproc = 8
pool = Pool(nproc)
for idx, return_code in enumerate(pool.imap(partial(call, shell=True), commands)):
    if return_code != 0:
        print(colored('Command \"%s\" failed' % commands[idx], 'yellow'))
    else:
        print(colored('-- Processed %d/%d' % (idx + 1, len(commands)), 'white', 'on_blue'))
