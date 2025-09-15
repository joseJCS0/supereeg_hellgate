#!/bin/bash -l

# DO NOT MODIFY THIS FILE!
# MODIFY config.py AND create_and_submit_jobs.py AS NEEDED

#SBATCH --job-name=full_mats

#SBATCH --output=full_mats%A_%a.out
#SBATCH --error=full_mats%A_%a.err
#SBATCH --output = directory/to/put/in/full_mats_log.txt
#SBATCH --error = directory/to/put/in/full_mats_error.txt

#SBATCH --nodes=1

#SBATCH --cpus-per-task=20

#SBATCH --mem-per-cpu=6gb

#SBATCH --mail-type=BEGIN,END,FAIL

#SBATCH --main-user=jose.carmona-sanchez@umconnect.umt.edu

#ENV set up, check if env is installed
ENV_NAME="supereeg_env"

# Check if the conda environment exists
if conda env list | grep -q "${ENV_NAME}"; then
    echo "Conda environment '${ENV_NAME}' already exists."
else

    # Create supereeg_env
    echo "Conda environment '${ENV_NAME}' does not exist."
    if ! conda env create -f create_supereeg_env.yml; then
        echo "Error: Failed to create conda environment" >&2
        exit 1
    fi

    CONDA_PYTHON_PATH=$(conda run -n $ENV_NAME which python)
    SITE_PACKAGES_PATH=$(conda run -n $ENV_NAME python -c "import site; print(site.getsitepackages()[0])")

    file_path="${SITE_PACKAGES_PATH}/deepdish"
    file_path_supereeg="${SITE_PACKAGES_PATH}/supereeg/deepdish"

    echo $file_path
    echo $file_path_supereeg


    # Move deepdish to site-packages
    echo "Copying deepdish to site-packages..."
    if cp -r "$file_path_supereeg" "$file_path"; then
        echo "Deepdish successfully copied to site-packages"
    else
        echo "Error: Failed to copy deepdish" >&2
        exit 1
    fi
fi

echo "Setup completed successfully!"

conda activate supereeg_env

# set the working directory *of the job* to the specified start directory
cd <config['startdir']>

# run the job
<config['cmd_wrapper']> <job_command> #note: job_command is reserved for the job command; it should not be specified in config.py

conda deactivate
