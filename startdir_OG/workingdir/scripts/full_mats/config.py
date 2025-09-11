import os
import socket

config = dict()

config['template'] = 'run_job.sh'

# ====== MODIFY ONLY THE CODE BETWEEN THESE LINES ======
if (socket.gethostname() == 'jose-Cyborg-15-A13VE'):
    config['datadir'] = '/home/jose/miniconda3/envs/supereeg_pipeline_test/startdir/datadir/bo'
    config['workingdir'] = '/home/jose/miniconda3/envs/supereeg_pipeline_test/startdir/workingdir/full_mats/'
    config['startdir'] = '/home/jose/miniconda3/envs/supereeg_pipeline_test/startdir'  # directory to start the job in
    config['template'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'run_job_local.sh')
    config['og_bodir'] = '/home/jose/miniconda3/envs/supereeg_pipeline_test/startdir/datadir/RAM_analysis/bos' 
    config['og_bodir'] = '/home/jose/miniconda3/envs/supereeg_pipeline_test/startdir/datadir/pyFR/data/bo' 
else:
    '''config['datadir'] = '/dartfs/rc/lab/D/DBIC/CDL/f003f64/freqs'
    config['workingdir'] = '/dartfs/rc/lab/D/DBIC/CDL/f003f64/'
    config['startdir'] = '/dartfs/rc/lab/D/DBIC/CDL/f003f64/'
    config['template'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'run_job.sh')
    config['og_bodir'] = '/home/jose/miniconda3/envs/supereeg_pipeline_test/startdir/datadir/RAM_analysis/bos' 
    config['og_bodir'] = '/home/jose/miniconda3/envs/supereeg_pipeline_test/startdir/datadir/pyFR/data/bo'''

# job creation options
config['scriptdir'] = os.path.join(config['workingdir'], 'scripts')
config['lockdir'] = os.path.join(config['workingdir'], 'locks')
config['resultsdir'] = os.path.join(config['workingdir'], 'results','union')
config['locsdir'] = os.path.join(config['workingdir'], 'results')
# ====== MODIFY ONLY THE CODE BETWEEN THESE LINES ======
