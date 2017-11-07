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
import re
import glob
import numpy as np

#
#   write vectors
#
def write_vectors(nrow, ncol, filepath, data):
    print("writing vectors ... %s" % filepath)
    mat_data = np.asarray(data, dtype = ">f8")
    f = open(filepath, 'wb')
    for i in range(ncol):
        np.array([1211214, nrow], dtype = ">i4").tofile(f)
        mat_data[i,:].tofile(f)
    f.close()

# ----------------------------------------------------------------------------------------
if __name__ == "__main__":
    """
        proben12petsc.py
        
        The ``proben12petsc.py`` script converts the Proben1 data sets into dense matrices
        written to disc in the PETSc dense matrix format.
        ...
        
        """

    # header, exmaple:
    #    bool_in=0
    #    real_in=14
    #    bool_out=0
    #    real_out=3
    #    training_examples=2104
    #    validation_examples=1052
    #    test_examples=1052

    # constants
    n_header = 7

    # paths and files
    data_set_path = sys.argv[1]
    data_set_file_path = glob.glob(data_set_path + "*.dt")

    # process each file
    for file_path in data_set_file_path:
        
        # open file
        f = open(file_path, 'r')
        
        # read counts
        count_list = []
        for _ in range(n_header):
            count_list.append(int(f.readline().rstrip().split("=")[1]))
        
        # assign counts
        # do not distinguish between bools and reals
        n_input = max(count_list[0:2])
        n_output = max(count_list[2:4])
        n_train = count_list[4]
        n_valid = count_list[5]
        n_test = count_list[6]
        print("# " + file_path + ", " + str(count_list))
        
        # read train data set
        raw_train = []
        for _ in range(n_train):
            raw_train.append(re.split("\s+", f.readline().strip()))

        # read validate data set
        raw_valid = []
        for _ in range(n_valid):
            raw_valid.append(re.split("\s+", f.readline().strip()))
        
        # read test data set
        raw_test = []
        for _ in range(n_test):
            raw_test.append(re.split("\s+", f.readline().strip()))
        
        # close file
        f.close()

        #
        # use train and test only
        #
        
        # train
        # separate in and out
        raw_train = np.array(raw_train, ">f8")
        raw_train_in = raw_train[:, 0:n_input]
        raw_train_out = raw_train[:, n_input:]
        # file paths
        train_file_in = file_path + ".train.in.petsc"
        train_file_out = file_path + ".train.out.petsc"
        # write petsc file, transpose before
        # in
        write_vectors(n_input, n_train, train_file_in, raw_train_in)
#        f = open(train_file_in, 'wb')
#        np.array([1211216, n_input, n_train, -1], dtype = ">i4").tofile(f)
#        raw_train_in.T.tofile(f)
#        f.close()
        # out
        write_vectors(n_output, n_train, train_file_out, raw_train_out)
#        f = open(train_file_out, 'wb')
#        np.array([1211216, n_output, n_train, -1], dtype = ">i4").tofile(f)
#        raw_train_out.T.tofile(f)
#        f.close()

        # test
        # separate in and out
        raw_test = np.array(raw_test, ">f8")
        raw_test_in = raw_test[:, 0:n_input]
        raw_test_out = raw_test[:, n_input:]
        # file paths
        test_file_in = file_path + ".test.in.petsc"
        test_file_out = file_path + ".test.out.petsc"
        # write petsc file, transpose before
        # in
        write_vectors(n_input, n_test, test_file_in, raw_test_in)
#        f = open(test_file_in, 'wb')
#        np.array([1211216, n_input, n_test, -1], dtype = ">i4").tofile(f)
#        raw_test_in.T.tofile(f)
#        f.close()
        # out
        write_vectors(n_output, n_test, test_file_out, raw_test_out)
#        f = open(test_file_out, 'wb')
#        np.array([1211216, n_output, n_test, -1], dtype = ">i4").tofile(f)
#        raw_test_out.T.tofile(f)
#        f.close()



