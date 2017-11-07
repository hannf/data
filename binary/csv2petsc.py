#!/usr/bin/env python

#
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

#import os
import sys
#import re
import numpy as np

#
#   read_csv_data
#
def read_csv_data(nfeature, nclass, csv_file):
    # debug
    print("reading csv data ...")
    # feature and class data
    ndata = 0
    feature_data = []
    class_data = []
    # scan file
    f = open(csv_file, 'r')
    for line in f:
        # debug
#        print(line)
        # strip new line at the end
        # split by separator
        data_row = line.rstrip().split(";")
        # check if numeric
        try:
            line_array = np.asarray(data_row, dtype = ">f8")
        except ValueError:
            print("line skipped ... %s" % data_row[0:3])
            continue
        # append appropriately
        feature_data.append(line_array[:nfeature])
        class_data.append(line_array[nfeature:])
        ndata = ndata + 1
    # debug
    print("read in %d rows ..." % ndata)
    # close file
    f.close()
    # return data
    return feature_data, class_data

##
##   write_matrix
##
#def write_matrix(nrow, ncol, filepath, data):
#    print("writing matrix ... %s" % filepath)
#
#    # combine to 2d array
#    # transpose
#    # flatten
#    mat_data = np.asarray(data, dtype = ">f8")
#    mat_data = mat_data.T
#    mat_data = mat_data.flatten()
#    # open file
#    f = open(filepath, 'wb')
#    # header
#    header = np.asarray([1211216, nrow, ncol, -1], dtype = ">i4")
#    # write header
#    header.tofile(f)
#    # write matrix as array
#    mat_data.tofile(f)
#    # close file
#    f.close()

#
#   write vectors
#
def write_vectors(nrow, ncol, filepath, data):
    print("writing vectors ... %s" % filepath)
#    # write data to petsc vec file
#    f = open(data_output_file, 'wb')
#    for i in range(n_data):
#        np.array([1211214, n_input], dtype = ">i4").tofile(f)
#        data_output[i,:].tofile(f)
#    f.close()
    # numpy array
    mat_data = np.asarray(data, dtype = ">f8")
    f = open(filepath, 'wb')
    for i in range(ncol):
        np.array([1211214, nrow], dtype = ">i4").tofile(f)
        mat_data[i,:].tofile(f)
    f.close()

#
#   write_petsc_dense_matrices
#
def write_petsc_dense_matrices(nfeature, feature_data, nclass, class_data, csv_file):
    print("writing petsc dense matrices ...")

    # feature matrix
    nrow = nfeature
    ncol = len(feature_data)
    filepath = csv_file.replace(".csv", ".feature.petsc")
#    # write matrix
#    write_matrix(nrow, ncol, filepath, feature_data)
    # write vectors
    write_vectors(nrow, ncol, filepath, feature_data)

    # class matrix
    nrow = nclass
    ncol = len(class_data)
    filepath = csv_file.replace(".csv", ".class.petsc")
#    # write matrix
#    write_matrix(nrow, ncol, filepath, class_data)
    # write vectors
    write_vectors(nrow, ncol, filepath, class_data)

#
#   main
#
if __name__ == "__main__":
    # no arguments?
    if len(sys.argv) <= 3:
        # print usage and exit with code 1
        print("usage: %s [number-of-features] [number-of-classes] [csv-file]" % sys.argv[0])
        print("");
        print("example:");
        print("  $> ./csv2petsc.py 19 12 sensor_data_all.csv");
        print("  $> ls");
        print("sensor_data_all.feature.petsc");
        print("sensor_data_all.class.petsc");
        print("");
        sys.exit(1)

    # feature count
    # class count
    # csv file
    # petsc file
    nfeature   = int(sys.argv[1])
    nclass     = int(sys.argv[2])
    csv_file   = sys.argv[3]

    # debug
    print("csv2petsc ... nfeature: %d, nclass: %d, csv_file: %s" % (nfeature, nclass, csv_file))

    # read csv data
    feature_data, class_data = read_csv_data(nfeature, nclass, csv_file)
#    print(feature_data)
#    print(class_data)

    # write petsc dense matrix
    write_petsc_dense_matrices(nfeature, feature_data, nclass, class_data, csv_file)


