
import SimpleITK as sitk
import radiomics
import numpy as np
mask_name = r"C:/Users/16414/Desktop/pet/data/ICBM_Template.zipfile/ICBM_Template.img"
mask = sitk.ReadImage(mask_name)
np_mask = sitk.GetArrayFromImage(mask)

