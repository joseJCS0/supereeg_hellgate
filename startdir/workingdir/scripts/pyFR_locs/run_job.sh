#!/bin/bash -l

# DO NOT MODIFY THIS FILE!
# MODIFY config.py AND create_and_submit_jobs.py AS NEEDED

#SBATCH --job-name==compile_locs

#SBATCH --output=compile_locs%A_%a.out
#SBATCH --error=compile_locso%A_%a.err
#SBATCH --output =directory/to/put/in/compile_locs_log.txt
#SBATCH --error =directory/to/put/in/compile_locs_error.txt

#SBATCH --nodes=1

#SBATCH --cpus-per-task=20

#SBATCH --mem-per-cpu=6gb

#SBATCH --mail-type=BEGIN,END,FAIL

#SBATCH --main-user=jose.carmona-sanchez@umconnect.umt.edu

# set the working directory *of this script* to the directory from which the job was submitted

# set the working directory *of the job* to the specified start directory
cd <config['startdir']>

echo ACTIVATING supereeg VIRTUAL ENVIRONMENT
conda activate supereeg_env

# run the job
<config['cmd_wrapper']> <job_command> #note: job_command is reserved for the job command; it should not be specified in config.py

conda deactivate supereeg_env

