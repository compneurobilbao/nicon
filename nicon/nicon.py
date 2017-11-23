# -*- coding: utf-8 -*-
import os
from os.path import join as opj

DATA_DIR = '/home/asier/git/nicon/nicon/data'
subject = 'sub-001'
OUTPUT_DIR = '/home/asier/Desktop/nicon_test/output'
WORK_DIR = '/home/asier/Desktop/nicon_test/workdir'


# optional: mriqc
# NOTE: OUTPUT -> better to put it's own folder. opj(OUTPUT_DIR, 'mriqc')

# perform: fmriprep
# perform extract series nilearn

# perform ICA -> RSN (DMN...)

# perform (optional?) dwi motion correction
# perform ndmg

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


def run_fmriprep():

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


def run_mriqc():

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