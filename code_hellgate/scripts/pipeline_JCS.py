import supereeg as se
import sh
import socket
import time
import numpy as np

if (socket.gethostname() == 'josecsOmarchy'):
    supereeg_env = "/home/josecs/Desktop/supereeg_env"
    fileIO_jobsubmit_path = "/home/josecs/miniconda3/envs/supereeg_env/supereeg_hellgate/code_hellgate/scripts/file_io/file_io_job_submit.py"
    pyFR_jobsubmit_path = "/home/josecs/miniconda3/envs/supereeg_env/supereeg_hellgate/code_hellgate/scripts/pyFR_locs/union_locs_job_submit.py"
    fullmats_jobsubmit_path = "/home/josecs/miniconda3/envs/supereeg_env/supereeg_hellgate/code_hellgate/scripts/full_mats/full_mats_job_submit.py"
    avemats_jobsubmit_path = "/home/josecs/miniconda3/envs/supereeg_env/supereeg_hellgate/code_hellgate/scripts/ave_mats/ave_mats_job_submit.py"
    reacon_jobsubmit_path = "/home/josecs/miniconda3/envs/supereeg_env/supereeg_hellgate/code_hellgate/scripts/recon/recon_job_submit.py"
else:
    supereeg_env = "/mnt/beegfs/projects/jc158347/supereeg_jcs/supereeg_env"
    fileIO_jobsubmit_path = "/mnt/beegfs/projects/jc158347/supereeg_jcs/supereeg_env/scripts/file_io/file_io_job_submit.py"
    pyFR_jobsubmit_path = "/mnt/beegfs/projects/jc158347/supereeg_jcs/supereeg_env/scripts/pyFR_locs/union_locs_job_submit.py"
    fullmats_jobsubmit_path = "/mnt/beegfs/projects/jc158347/supereeg_jcs/supereeg_env/scripts/full_mats/full_mats_job_submit.py"
    avemats_jobsubmit_path = "/mnt/beegfs/projects/jc158347/supereeg_jcs/supereeg_env/scripts/ave_mats/ave_mats_job_submit.py"
    reacon_jobsubmit_path = "/mnt/beegfs/projects/jc158347/supereeg_jcs/supereeg_env/scripts/recon/recon_job_submit.py"

run = sh.Command('python')

print("Running File_IO")
start_time_fileIO = time.time()
run(fileIO_jobsubmit_path)
end_time_fileIO = time.time()
elapsed_time_fileIO = end_time_fileIO - start_time_fileIO
print("Done running File_IO\n")
print(f"Total run time {elapsed_time_fileIO} sec")

print("Running pyFR")
start_time_pyFR = time.time()
run(pyFR_jobsubmit_path)
end_time_pyFR = time.time()
elapsed_time_pyFR = end_time_pyFR - start_time_pyFR
print("Done running pyFR\n")
print(f"Total run time {elapsed_time_pyFR} sec")

print("Running Full_Mats")
start_time_fullmats = time.time()
run(fullmats_jobsubmit_path)
end_time_fullmats = time.time()
elapsed_time_fullmats = end_time_fullmats - start_time_fullmats
print("Done running Full_mats\n")
print(f"Total run time {elapsed_time_fullmats} sec")

print("Running Ave_mats")
start_time_avemats = time.time()
run(avemats_jobsubmit_path)
end_time_avemats = time.time()
elapsed_time_avemats = end_time_avemats - start_time_avemats
print("Done running Ave_mats\n")
print(f"Total run time {elapsed_time_avemats} sec")

print("Running Recon")
run(reacon_jobsubmit_path)
start_time_recon = time.time()
end_time_recon = time.time()
elapsed_time_recon = end_time_recon - start_time_recon
print("Done running Recon\n")
print(f"Total run time {elapsed_time_recon} sec")

run_time = np.array([elapsed_time_fileIO,elapsed_time_pyFR,elapsed_time_fullmats,elapsed_time_avemats,elapsed_time_recon])
np.savez(supereeg_env+"/Total_Run_Time.npz",run_time)