import os
import socket

config = dict()

config['template'] = 'run_job.sh'

# ====== MODIFY ONLY THE CODE BETWEEN THESE LINES ======
if (socket.gethostname() == 'jose-Cyborg-15-A13VE'):
    config['datadir'] = '/home/jose/miniconda3/envs/supereeg_pipeline_test/supereeg_hellgate/startdir/datadir/bo'
    config['workingdir'] = '/home/jose/miniconda3/envs/supereeg_pipeline_test/supereeg_hellgate/startdir/workingdir/pyFR_locs'
    config['startdir'] = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # directory to start the job in
    config['template'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'run_job_local.sh')
else:
    '''config['datadir'] = '/dartfs/rc/lab/D/DBIC/CDL/f003f64/freqs'
    config['workingdir'] = '/dartfs/rc/lab/D/DBIC/CDL/f003f64'
    config['startdir'] = '/dartfs/rc/lab/D/DBIC/CDL/f003f64'
    config['template'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'run_job.sh')'''

# job creation options
config['scriptdir'] = os.path.join(config['workingdir'], 'scripts')
config['lockdir'] = os.path.join(config['workingdir'], 'locks')
config['resultsdir'] = os.path.join(config['workingdir'], 'results')
config['og_bodir'] = config['datadir'] # KEEP AN EYE
config['og_bodir'] = config['datadir'] # KEEP AN EYE
# ====== MODIFY ONLY THE CODE BETWEEN THESE LINES ======
