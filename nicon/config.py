# -*- coding: utf-8 -*-

DATA_DIR = ''
SUBJECT = 'sub-001'
OUTPUT_DIR = '/home/output_nicon'
WORK_DIR = '/tmp/tmp_nicon'

QC = False
FMRI = True
ICA_RSN = False
DWI = True
DWI_CORRECTION = False

CONFOUNDS_ID = ['FramewiseDisplacement',
                'WhiteMatter',
                'GlobalSignal',
                'X',
                'Y',
                'Z',
                'RotX',
                'RotY',
                'RotZ',
                ]

#CONFOUNDS_ID = ['FramewiseDisplacement',
#                'aCompCor0',
#                'aCompCor1',
#                'aCompCor2',
#                'aCompCor3',
#                'aCompCor4',
#                'aCompCor5',
#                'X',
#                'Y',
#                'Z',
#                'RotX',
#                'RotY',
#                'RotZ',
#                ]