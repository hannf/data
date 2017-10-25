# SVHN

The Street View House Numbers (SVHN) Dataset,
[http://ufldl.stanford.edu/housenumbers/](),
column major ???,

input and output combined,

**Train data set:**

```
train_32x32.mat
```


**Test data set:**

```
test_32x32.mat
```

```

The ``svhn2petsc`` script converts the SVHN data set (Format 2) into two dense matrices
written to disc in the PETSc dense matrix format.
...

SVHN data set (Format 2):

PETSc dense matrix format:

$> python
>>> import scipy.io as sp
>>> sp.whosmat('train_32x32.mat')
[('X', (32, 32, 3, 73257), 'uint8'), ('y', (73257, 1), 'double')]
>>> sp.whosmat('test_32x32.mat')
[('X', (32, 32, 3, 26032), 'uint8'), ('y', (26032, 1), 'double')]



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

```

**Protocol:**

```
$>
wget http://ufldl.stanford.edu/housenumbers/train_32x32.mat
wget http://ufldl.stanford.edu/housenumbers/test_32x32.mat

./svhn2petsc.py train_32x32.mat
# n_data: 73257

./svhn2petsc.py test_32x32.mat
# n_data: 26032

tree -hs
.
├── [1.9K]  README.md
├── [2.7K]  svhn2petsc.py
├── [ 61M]  test_32x32.mat
├── [610M]  test_32x32.mat.in.petsc
├── [2.0M]  test_32x32.mat.out.petsc
├── [174M]  train_32x32.mat
├── [1.7G]  train_32x32.mat.in.petsc
└── [5.6M]  train_32x32.mat.out.petsc

0 directories, 8 files
```


