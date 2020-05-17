import SimpleITK as sitk
import numpy as np
import radiomics
mask_name = r"C:/Users/16414/Desktop/pet/data/sz_xiaoyu_normal.nii"
mask = sitk.ReadImage(mask_name)
np_mask = sitk.GetArrayFromImage(mask)
nnp_mask = np_mask.copy()
# nnp_mask=nnp_mask.swapaxes(1,2)
# nnp_mask =nnp_mask.swapaxes(0,1)
nnp_mask[nnp_mask!=0] = 1
nnp_mask = nnp_mask.astype(np.int32)
img = sitk.GetImageFromArray(nnp_mask)
img = sitk.WriteImage(img,"neg.nii")

