# -*- coding: utf-8 -*-

import os
from nilearn.image import resample_img
import nibabel as nib
import numpy as np

for root, dirs, files in os.walk("/home/asier/Desktop/ds114"):
    for file in files:
        if file.endswith(".nii.gz"):
            img = nib.load(os.path.join(root,file))
            img.affine
            
            epi_img_data = img.get_data()
            epi_img_data.shape
            
            resampled_img = resample_img(img, target_affine=np.diag((4, 4, 4)))
            resampled_img.shape
            resampled_img
            
            nib.save(resampled_img, os.path.join(root,file))
