# -*- coding: utf-8 -*-
import subprocess

# from utils import correct_dwi_conmat

from config import (DATA_DIR,
                    SUBJECT,
                    OUTPUT_DIR,
                    WORK_DIR,
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
    # TODO: check template
    # TODO: Load global variables

    command = [
           'docker', 'run', '-i', '--rm',
           '-v', DATA_DIR + ':/data:ro',
           '-v', OUTPUT_DIR + ':/output',
           '-v', WORK_DIR + ':/work',
           '-w', '/work',
           'nicon/mrtrix3_connectome', 'fmriprep',
           '/data', '/output', 'participant',
           '--participant_label', SUBJECT,
           '-w', '/work', '--no-freesurfer', '--ignore', 'fieldmaps',
           '--output-space', 'template',
           '--template', 'MNI152NLin2009cAsym',
        ]

    for output in execute(command):
        print(output)


def extract_timeseries():
    # nilearn
    pass


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
       'nicon/mrtrix3_connectome:latest', 'run.py',
       '/bids_dataset', '/outputs', 'participant',
       '--participant_label', subject,
       '--parcellation', 'aal',
    ]

    for output in execute(command):
        print(output)

    # correct_dwi_conmat(atlas, subject)

    pass
