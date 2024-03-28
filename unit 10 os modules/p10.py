# This function uses real uid/gid to test if the invoking user has access to the path.

import os
import sys
path1 = os.access("Pytho1.txt", os.F_OK)
print("Exist path:", path1)
path2 = os.access("Pytho1.txt", os.R_OK)
print("It access to read the file:", path2)
path3 = os.access("Pytho1.txt", os.W_OK)
print("It access to write the file:", path3)
path4 = os.access("Pytho1.txt", os.X_OK)
print("Check if path can be executed:", path4)
