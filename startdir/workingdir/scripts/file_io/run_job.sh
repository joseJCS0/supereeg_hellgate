#!/bin/bash -l

# DO NOT MODIFY THIS FILE!
# MODIFY config.py AND create_and_submit_jobs.py AS NEEDED

#SBATCH --job-name==file_io_npz_bo

#SBATCH --output=file_io_npz_bo%A_%a.out
#SBATCH --error=file_io_npz_bo%A_%a.err
#SBATCH --output =directory/to/put/in/file_io_npz_bo_log.txt
#SBATCH --error =directory/to/put/in/file_io_npz_bo_error.txt

#SBATCH --nodes=1

#SBATCH --cpus-per-task=20

#SBATCH --mem-per-cpu=6gb

#SBATCH --mail-type=BEGIN,END,FAIL

#SBATCH --main-user=jose.carmona-sanchez@umconnect.umt.edu

# set the working directory *of the job* to the specified start directory
cd <config['startdir']>

echo ACTIVATING supereeg VIRTUAL ENVIRONMENT
source activate supereeg_env

# run the job
<config['cmd_wrapper']> <job_command> #note: job_command is reserved for the job command; it should not be specified in config.py

source deactivate supereeg_env

