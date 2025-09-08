import os
import socket

config = dict()

config['template'] = 'run_job.sh'

# ====== MODIFY ONLY THE CODE BETWEEN THESE LINES ======
if (socket.gethostname() == 'jose-Cyborg-15-A13VE'):
    config['datadir'] = '/home/jose/miniconda3/envs/supereeg_pipeline_test/supereeg_hellgate/startdir/datadir'
    config['workingdir'] = '/home/jose/miniconda3/envs/supereeg_pipeline_test/supereeg_hellgate/startdir/workingdir'
    config['startdir'] = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # directory to start the job in
    config['template'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'run_job_local.sh')
else:
   ''' config['datadir'] = '/idata/cdl/data/ECoG/pyFR/data/'
    config['workingdir'] = '/idata/cdl/data/ECoG/pyFR/data/bo'
    config['startdir'] = '/idata/cdl/lowen'
    config['template'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'run_job.sh')'''

# job creation options
config['scriptdir'] = os.path.join(config['workingdir'], 'scripts')
config['lockdir'] = os.path.join(config['workingdir'], 'locks')
config['resultsdir'] = config['workingdir']
# ====== MODIFY ONLY THE CODE BETWEEN THESE LINES ======

