# -*- coding: utf-8 -*-
import sys

from external_calls import (run_mriqc,
                            run_fmriprep,
                            extract_timeseries,
                            calc_fc_matrix,
                            run_ica_rsn,
                            correct_dwi,
                            run_ndmg
                            )


# TODO: All this global variables should go in an external file
DATA_DIR = '/home/asier/git/nicon/nicon/data'
subject = 'sub-001'
OUTPUT_DIR = '/home/asier/Desktop/nicon_test/output'
WORK_DIR = '/home/asier/Desktop/nicon_test/workdir'
INPUT_ATLAS_PATH = ''


def run_nicon():

    # load global variables

    # optional: mriqc
    if qc:
        run_mriqc()
        # NOTE: OUTPUT -> better to put it's own folder.
        # opj(OUTPUT_DIR, 'mriqc')

    # fmriprep
        # optional: freesurfer
    # extract series nilearn
    # calculate FC matrix
    # optional: ICA -> RSN (DMN...)
    if fmri:
        run_fmriprep()
        extract_timeseries()
        calc_fc_matrix()
        if ica_rsn:
            run_ica_rsn()

    # optional: dwi motion correction
    # ndmg
    if dwi:
        if dwi_correction:
            correct_dwi()
        run_ndmg()
        

if __name__ == "__main__":
    
    run_nicon()
    sys.exit()