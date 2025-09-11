
import os
import socket

config = dict()

config['template'] = 'run_job.sh'

# ====== MODIFY ONLY THE CODE BETWEEN THESE LINES ======
if (socket.gethostname() == 'jose-Cyborg-15-A13VE'):
    config['datadir'] = '/home/jose/miniconda3/envs/supereeg_pipeline_test/supereeg_hellgate/startdir/workingdir/full_mats/results'
    config['workingdir'] = '/home/jose/miniconda3/envs/supereeg_pipeline_test/supereeg_hellgate/startdir/workingdir/ave_mats'
    config['startdir'] = '/home/jose/miniconda3/envs/supereeg_pipeline_test/supereeg_hellgate/startdir'  # directory to start the job in
    config['template'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'run_job_local.sh')
else:
    '''config['datadir'] = '/dartfs/rc/lab/D/DBIC/CDL/f003f64/results/union'
    config['workingdir'] = '/dartfs/rc/lab/D/DBIC/CDL/f003f64'
    config['startdir'] = '/dartfs/rc/lab/D/DBIC/CDL/f003f64'
    config['template'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'run_job.sh')'''

# job creation options
config['scriptdir'] = os.path.join(config['workingdir'], 'scripts')
config['lockdir'] = os.path.join(config['workingdir'], 'locks')
config['resultsdir'] = os.path.join(config['workingdir'], 'results')

# runtime options
config['jobname'] = "ave_mats"  # default job name
config['q'] = "default"  # options: default, testing, largeq
config['feature'] = 'celln'
config['nnodes'] = 1  # how many nodes to use for this one job
config['ppn'] = 16  # how many processors to use for this one job (assume 4GB of RAM per processor)
config['walltime'] = '24:00:00'  # maximum runtime, in h:MM:SS
config['cmd_wrapper'] = "python3"  # replace with actual command wrapper (e.g. matlab, python, etc.)
config['modules'] = "(\"python/3.5\")"  # separate each module with a space and enclose in (escaped) double quotes
# ====== MODIFY ONLY THE CODE BETWEEN THESE LINES ======
