#!/usr/bin/env python
#
# HANNF: High-performance Artificial Neural Network Framework
# Copyright (C) 2017  Jaroslaw Piwonski, CAU, jpi@informatik.uni-kiel.de
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import numpy as np
import scipy.io as sp

# ----------------------------------------------------------------------------------------
if __name__ == "__main__":
    """
        svhn2petsc
        
        usage: $> ./svhn2petsc.py [mat-input-file]

    """
    
    # constants
    n_input             = 32*32*3
    n_output            = 10
    
    # file names
    input_file          = sys.argv[1]                   # [mat-input-file]
    data_output_file    = input_file + ".data.petsc"
    label_output_file   = input_file + ".label.petsc"

    # traing data count, use whosmat, returns a list
    n_data = sp.whosmat(input_file)[0][1][3]
    print("# n_data: " + str(n_data))

    # read mat file
    raw_data = sp.loadmat(input_file)
    
    # image format: 32 x 32 pixels, 3 color channels
    # reshape image data to vector, 3072
    # convert to doubles
    data_output = raw_data["X"].reshape((n_input, n_data), order = "F").astype(">f8")

    # write petsc data file
    # !!! data is transposed !!!, data_output is F order, tofile always writes C order
    f = open(data_output_file, 'wb')
    np.array([1211216, n_input, n_data, -1], dtype = ">i4").tofile(f)
    data_output.tofile(f)
    f.close()

    # extract labels as integer
    # squeeze single dimension
    y = np.squeeze(raw_data["y"]).astype(">i4")

    # vectorize labels
    # encode as zero vector with a one at label index
    # the labels are 1,...,9 and 10, first nine are clear, encode 10 as 0
    # compute index modulo n_output
    label_output = np.zeros((n_output, n_data), dtype = ">f8")
    for idx in range(n_data):
        label_output[y[idx] % n_output, idx] = 1.0

    # write petsc label file
    # !!! data is transposed !!!, label_output is F order, tofile always writes C order
    f = open(label_output_file, 'wb')
    np.array([1211216, n_output, n_data, -1], dtype = ">i4").tofile(f)
    label_output.tofile(f)
    f.close()


