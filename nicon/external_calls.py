# -*- coding: utf-8 -*-
import subprocess


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
           '--participant_label', subject,
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
           'poldracklab/fmriprep:latest',
           '/data', '/output', 'participant',
           '--participant_label', subject,
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
    pass


def run_ndmg():
    # ndmg docker
    pass



