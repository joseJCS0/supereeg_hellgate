import supereeg as se
import numpy as np
from time import sleep
from glob import glob
from os.path import exists, join
import sh
import socket

"""
WIP, automated pipeline for whole analysis
"""

### IMPORTANT CONFIG
num_models = 5

if (socket.gethostname() == 'jose-Cyborg-15-A13VE'):
    og_bodir = '/home/jose/Desktop/supereeg_env/bo'
    scripts_path = '/home/jose/miniconda3/envs/supereeg_pipeline_test/startdir/workingdir/scripts'
    locs_dir = "holder/pyFR_locs/results"
else:
    og_bodir = '/mnt/beegfs/projects/jc158347/supereeg_jcs/supereeg_env/bo'
    scripts_path = '/mnt/beegfs/projects/jc158347/supereeg_jcs/supereeg_env/scripts'
    locs_dir = '/mnt/beegfs/projects/jc158347/supereeg_jcs/supereeg_env/pyFR_locs/results'




def check(update, check, step, wait_time=60, timeout=60*20):
    newest_file = 0
    n = update()
    while not check():
        if newest_file > timeout:
            print('something broken with ' + step)
            exit()
        if n < update():
            newest_file = 0
        else:
            newest_file += wait_time
        n = update()
        sleep(wait_time)

run = sh.Command('python')


run(join(scripts_path,'file_io/file_io_job_submit.py'))


num_locs = len(glob(join(locs_dir, '*locs.npz')))
if num_locs < 1:
    run('/home/jose/miniconda3/envs/supereeg_pipeline_test/startdir/workingdir/scripts/pyFR_locs/union_locs_job_submit.py')
    check(lambda: len(glob(join(locs_dir, '*locs.npz'))),\
        lambda: len(glob(join(locs_dir, '*locs.npz'))) == 1, 'locs')

print('locs done')

loc_fs = glob(join(locs_dir, '*locs.npz'))
arr = np.load(loc_fs[0])['locs']
for f in loc_fs:
    arr2 = np.load(f)['locs']
    if not np.array_equal(arr, arr2):
        print('something wrong with locs')
        exit()

results_dir = '/home/jose/miniconda3/envs/supereeg_pipeline_test/startdir/datadir/'

locs_dir = join(results_dir, 'union')
def check_freqs():
    freqs = ['raw']
    full_mats = [glob(join(locs_dir, '*'+freq+'*')) for freq in freqs]
    for freq_mats in full_mats:
        if len(freq_mats) != num_models:
            return False
    return True

if not check_freqs():
    run('/home/jose/miniconda3/envs/supereeg_pipeline_test/startdir/workingdir/scripts/full_mats/full_mats_job_submit.py')
    check(lambda: len(glob(join(locs_dir, '*'))), lambda: check_freqs, 'full mats')

print('full mats done')

num_ave = lambda: len(glob(join(results_dir,'*.mo')))
if num_ave() < 6:
    run('/home/jose/miniconda3/envs/supereeg_pipeline_test/startdir/workingdir/scripts/ave_mats/ave_mats_job_submit.py')
    check(num_ave, lambda: num_ave() < 6, 'ave mats')

print('ave mats done')