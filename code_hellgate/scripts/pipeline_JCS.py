import supereeg as se
import numpy as np
from time import sleep
from glob import glob
from os.path import exists, join
import sh
import socket

if (socket.gethostname() == 'josecsOmarchy'):
    fileIO_jobsubmit_path = "/home/josecs/miniconda3/envs/supereeg_env/supereeg_hellgate/code_hellgate/scripts/file_io/file_io_job_submit.py"
    pyFR_jobsubmit_path = "/home/josecs/miniconda3/envs/supereeg_env/supereeg_hellgate/code_hellgate/scripts/pyFR_locs/union_locs_job_submit.py"
    fullmats_jobsubmit_path = "/home/josecs/miniconda3/envs/supereeg_env/supereeg_hellgate/code_hellgate/scripts/full_mats/full_mats_job_submit.py"
    avemats_jobsubmit_path = "/home/josecs/miniconda3/envs/supereeg_env/supereeg_hellgate/code_hellgate/scripts/ave_mats/ave_mats_job_submit.py"
    reacon_jobsubmit_path = "/home/josecs/miniconda3/envs/supereeg_env/supereeg_hellgate/code_hellgate/scripts/recon/recon_job_submit.py"
else:
    fileIO_jobsubmit_path = "/mnt/beegfs/projects/jc158347/supereeg_jcs/supereeg_env/scripts/file_io/file_io_job_submit.py"
    pyFR_jobsubmit_path = "/mnt/beegfs/projects/jc158347/supereeg_jcs/supereeg_env/scripts/pyFR_locs/union_locs_job_submit.py"
    fullmats_jobsubmit_path = "/mnt/beegfs/projects/jc158347/supereeg_jcs/supereeg_env/scripts/full_mats/full_mats_job_submit.py"
    avemats_jobsubmit_path = "/mnt/beegfs/projects/jc158347/supereeg_jcs/supereeg_env/scripts/ave_mats/ave_mats_job_submit.py"
    reacon_jobsubmit_path = "/mnt/beegfs/projects/jc158347/supereeg_jcs/supereeg_env/scripts/recon/recon_job_submit.py"

run = sh.Command('python')

print("Running File_IO")
run(fileIO_jobsubmit_path)
print("Done running File_IO")

print("Running pyFR")
run(pyFR_jobsubmit_path)
print("Done running pyFR")

print("Running Full_Mats")
run(fullmats_jobsubmit_path)
print("Done running Full_mats")

print("Running Ave_mats")
run(avemats_jobsubmit_path)
print("Done running Ave_mats")

print("Running Recon")
run(reacon_jobsubmit_path)
print("Done running Recon")