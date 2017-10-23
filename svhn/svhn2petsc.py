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
        
        The ``svhn2petsc`` script converts the SVHN data set (Format 2) into two dense matrices
        written to disc in the PETSc dense matrix format.
        ...
        
        training data set
        
        $> python
        >>> import scipy.io as sp
        >>> sp.whosmat('svhn/train_32x32.mat')
        [('X', (32, 32, 3, 73257), 'uint8'), ('y', (73257, 1), 'double')]

    """
#        Convert SVHN data set to PETSc dense matrix. Create two matrices:
#            1. Data matrix. Every **column** is an input vector.
#            2. Label matrix. Every **column** is an output vector.
#
#        The resulting dimension of the matrices is:
#            1. n_input times n_data
#            2. n_output times n_data

# the input data as well as the labels are stored in a matlab file
# the format is v5, the file can be read in using scipy's ``loadmat`` routine
# the image data is stored in a variable called ``X``, labels are stored in ``y``
# the dimension of ``X`` is (32, 32, 3, 73257) assuming Fotran order, i.e.
# the leftmost dimension is the leading dimension, ``y`` (73257, 1)

    # constants
    input_file          = "svhn/train_32x32.mat"
    n_train             = 73257
    n_input             = 32*32*3
    n_output            = 10
    data_output_file    = "svhn.data.petsc"
    label_output_file   = "svhn.label.petsc"
    
    # read mat file
    raw_data = sp.loadmat(input_file)
    
    # image format: 32 x 32 pixels, 3 color channels
    # reshape image data to vector
    X = raw_data["X"].reshape((n_input, n_train), order = "F")
    
    # transpose, columns will be input vectors
    data_output = X.T.astype(">f8")

    # write petsc data file
    f = open(data_output_file, 'wb')
    np.array([1211216, n_input, n_train, -1], dtype = ">i4").tofile(f)
    data_output.tofile(f)
    f.close()

    # extract labels as integer
    # squeeze single dimension
    y = np.squeeze(raw_data["y"]).astype(">i4")

    # vectorize labels
    # encode as zero vector with a one at label index
    # the labels are 1,...,9 and 10, first nine are clear, encode 10 as 0
    # compute index modulo n_output
    label_output = np.zeros((n_output, n_train), dtype = ">f8")
    for idx in range(n_train):
        label_output[y[idx] % n_output, idx] = 1.0

    # write petsc label file
    f = open(label_output_file, 'wb')
    np.array([1211216, n_output, n_train, -1], dtype = ">i4").tofile(f)
    label_output.tofile(f)
    f.close()


