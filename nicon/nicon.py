# -*- coding: utf-8 -*-
import sys

from external_calls import (run_mriqc,
                            run_fmriprep,
                            extract_timeseries,
                            calc_fc_matrix,
                            run_ica_rsn,
                            correct_dwi,
                            run_mrtrix3,
                            )

from config import (QC,
                    FMRI,
                    ICA_RSN,
                    DWI,
                    DWI_CORRECTION,
                    )


def run_nicon():

    # load global variables

    # optional: mriqc
    if QC:
        run_mriqc()
        # NOTE: OUTPUT -> better to put it's own folder.
        # opj(OUTPUT_DIR, 'mriqc')

    # fmriprep
        # optional: freesurfer
    # extract series nilearn
    # calculate FC matrix
    # optional: ICA -> RSN (DMN...)
    if FMRI:
        run_fmriprep()
        extract_timeseries()
        calc_fc_matrix()
        if ICA_RSN:
            run_ica_rsn()

    # optional: dwi motion correction
    # ndmg
    if DWI:
        if DWI_CORRECTION:
            correct_dwi()
        run_mrtrix3()
        

if __name__ == "__main__":
    
    run_nicon()
    sys.exit()