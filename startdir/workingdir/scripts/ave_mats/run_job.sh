#!/bin/bash -l

# DO NOT MODIFY THIS FILE!
# MODIFY config.py AND create_and_submit_jobs.py AS NEEDED

#SBATCH --job-name==ave_mats

#SBATCH --output=ave_mats%A_%a.out
#SBATCH --error=ave_mats%A_%a.err
#SBATCH --output = directory/to/put/in/avemats_log.txt
#SBATCH --error = directory/to/put/in/avemats_error.txt

#SBATCH --nodes=1

#SBATCH --cpus-per-task=20

#SBATCH --mem-per-cpu=6gb

#SBATCH --mail-type=BEGIN,END,FAIL

#SBATCH --main-user=jose.carmona-sanchez@umconnect.umt.edu

echo ACTIVATING supereeg VIRTUAL ENVIRONMENT

# conda init bash
conda activate supereeg_env

# run the job
<config['cmd_wrapper']> <job_command> #note: job_command is reserved for the job command; it should not be specified in config.py
