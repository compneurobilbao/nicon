# -*- coding: utf-8 -*-
import subprocess

from utils import aal_atlas_to_subject_space
from config import (DATA_DIR,
                    SUBJECT,
                    OUTPUT_DIR,
                    WORK_DIR,
                    CONFOUNDS_ID,
                    )


def execute(cmd):
    popen = subprocess.Popen(cmd,
                             stdout=subprocess.PIPE,
                             universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


def run_mriqc():

    # TODO: Load global variables

    command = [
           'docker', 'run', '-i', '--rm',
           '-v', DATA_DIR + ':/data:ro',
           '-v', OUTPUT_DIR + ':/output',
           '-v', WORK_DIR + ':/work',
           '-w', '/work',
           'poldracklab/mriqc:latest',
           '/data', '/output', 'participant',
           '--participant_label', SUBJECT,
           '-w', '/work', '--verbose-reports',
        ]

    for output in execute(command):
        print(output)


def run_fmriprep():

    # TODO: check if FreeSurfer

    command = [
           'docker', 'run', '-i', '--rm',
           '-v', DATA_DIR + ':/data:ro',
           '-v', OUTPUT_DIR + ':/output',
           '-v', WORK_DIR + ':/work',
           '-w', '/work',
           'poldracklab/fmriprep:latest', #'fmriprep',
           '/data', '/output', 'participant',
           '--participant_label', SUBJECT,
           '-w', '/work', '--no-freesurfer', '--ignore', 'fieldmaps',
           '--output-space', 'template',
           '--template', 'MNI152NLin2009cAsym',
        ]

    for output in execute(command):
        print(output)


def extract_timeseries():
    import pandas as pd
    import os
    from os.path import join as opj
    import numpy as np
    
    from nilearn.input_data import NiftiLabelsMasker

    
    atlas_path = aal_atlas_to_subject_space(OUTPUT_DIR, SUBJECT)
    
    preproc_data_path = opj(OUTPUT_DIR,
                            'fmriprep',
                            SUBJECT,
                            'func')
    
    for file in os.listdir(preproc_data_path):
        if file.endswith('preproc.nii.gz'):
            preproc_file = opj(preproc_data_path, file)
        if file.endswith('confounds.tsv'):
            confounds_file = opj(preproc_data_path, file)        
            
    confounds = pd.read_csv(confounds_file,
                            delimiter='\t', na_values='n/a').fillna(0)

    confounds_matrix = confounds[CONFOUNDS_ID].as_matrix()

    masker = NiftiLabelsMasker(labels_img=atlas_path,
                               background_label=0, verbose=5,
                               detrend=True, standardize=True,
                               t_r=None, smoothing_fwhm=6,
                               #TODO: TR should not be a variable
                               low_pass=0.1, high_pass=0.01)
    # 1.- Confound regression
    confounds_matrix = confounds[CONFOUNDS_ID].as_matrix()

    time_series = masker.fit_transform(preproc_file,
                                       confounds=confounds_matrix)

    # 2.- Scrubbing
    # extract FramewiseDisplacement
#    FD = confounds.iloc[:, 5].as_matrix()
#    thres = 0.2
#    time_series = scrubbing(time_series, FD, thres)

    # Save time series 
    # TODO: save better
    np.savetxt(opj(OUTPUT_DIR, 'time_series_' + SUBJECT + '.txt'),
               time_series)
    
    return

def calc_fc_matrix():
    # nilearn
    pass


def run_ica_rsn():
    # ?¿
    pass


def correct_dwi():
    # nilearn + fsl ?¿

    # dipy: nlmeans_pipeline() in nipype
    # fsl: ecc_pipeline() in nipype for eddy currents
    # fsl: hmc_pipeline() in nipype for head motion
    pass


def run_mrtrix3():
    # mrtrix3 docker

    # NOTE: JUST subject number, without "sub-" prefix
    prefix = 'sub-'
    subject = SUBJECT[len(prefix):] if SUBJECT.startswith(prefix) else SUBJECT

    command = [
       'docker', 'exec', '-i', '--rm',
       '-v', DATA_DIR + ':/bids_dataset:ro',
       '-v', OUTPUT_DIR + ':/outputs',
       '-w', '/work',
       'erramuzpe/nicon_mrtrix3:latest', 'run.py',
       '/bids_dataset', '/outputs', 'participant',
       '--participant_label', subject,
       '--parcellation', 'aal',
    ]

    for output in execute(command):
        print(output)

    # correct_dwi_conmat(atlas, subject)

    pass
