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

# debug
-HANNFDebug                         1

# network type
# ffnn, (deep) feed forward neural network
# rnn, (deep) recurrent neural network
# cnn, (deep) convolutional neural network
-HANNFNetworkType                   ffnn

# binary test
-HANNFNetworkTopology               2,2
# training data
-HANNFTrainingDataCount             3
-HANNFTrainingDataIn                ../data/binary/binary.feature.petsc
-HANNFTrainingDataOut               ../data/binary/binary.class.petsc

# optimization, training
-HANNFTraining_tao_type             cg
-HANNFTraining_tao_type             blmvm
-HANNFTraining_tao_view
-HANNFTraining_tao_monitor
#-HANNFTraining_tao_max_it           1
#-HANNFTraining_tao_max_funcs        1

# output, W_i, b_i
-HANNFTrainingOutFileFormat         work/W_%02d.petsc,work/b_%02d.petsc

# input, W_i, b_i
#-HANNFMapInFileFormat               work/W_%02d.petsc,work/b_%02d.petsc



