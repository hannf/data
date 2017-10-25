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

# ----------------------------------------------------------------------------------------
if __name__ == "__main__":
    """
        mnist2petsc
        
        usage: $> ./mnist2petsc.py [data-input-file] [label-input-file]
        
    """

    # constants
    n_input     = 28*28
    n_output    = 10

    # file names
    data_input_file     = sys.argv[1]                   # [data-input-file]
    label_input_file    = sys.argv[2]                   # [label-input-file]
    data_output_file    = data_input_file + ".in.petsc"
    label_output_file   = label_input_file + ".out.petsc"

    # file formats
    # data
    #    [offset] [type]          [value]          [description]
    #    0000     32 bit integer  0x00000803(2051) magic number
    #    0004     32 bit integer  n_data           number of images
    #    0008     32 bit integer  28               number of rows
    #    0012     32 bit integer  28               number of columns
    #    0016     unsigned byte   ...
    #
    # labels
    #    [offset] [type]          [value]          [description]
    #    0000     32 bit integer  0x00000801(2049) magic number (MSB first)
    #    0004     32 bit integer  n_label          number of items
    #    0008     unsigned byte   ...

    # read data count
    f_data_in = open(data_input_file, 'rb')
    mno, n_data, nrow, ncol = np.fromfile(f_data_in, dtype = ">i4", count = 4)
    print("# n_data: " + str(n_data))

    # read label count
    f_label_in = open(label_input_file, 'rb')
    mno, n_label = np.fromfile(f_label_in, dtype = ">i4", count = 2)
    print("# n_label: " + str(n_label))

    # check counts
    if not n_data == n_label:
        print("### ERROR ### Count missmatch. n_data: " + str(n_data) + " n_label: " + str(n_label))
        sys.exit(1)

    # read data
    raw_data = np.fromfile(f_data_in, dtype = 'u1', count = n_input * n_data)

    # reorganize data, C order
    data_output = np.reshape(raw_data, (n_data, n_input)).T.astype(">f8")

    # write petsc data file
    f = open(data_output_file, 'wb')
    np.array([1211216, n_input, n_data, -1], dtype = ">i4").tofile(f)
    data_output.tofile(f)
    f.close()

    # read labels
    raw_label = np.fromfile(f_label_in, dtype = 'u1', count = n_label)

    # vectorize labels, label values are already from 0 to 9
    # C order, n_data leading
    label_output = np.zeros((n_output, n_data), dtype = ">f8")
    for idx in range(n_data):
        label_output[raw_label[idx], idx] = 1.0

    # write petsc label file
    f = open(label_output_file, 'wb')
    np.array([1211216, n_output, n_data, -1], dtype = ">i4").tofile(f)
    label_output.tofile(f)
    f.close()

    # close input files
    f_data_in.close()
    f_label_in.close()




