# MNIST

[http://yann.lecun.com/exdb/mnist/](),
60'000 images, black/white, unsigned 8 bit int, 1 byte,
28 x 28 pixels,
column major, transpose for reading,
label values: 0,...,9
# constants

```
n_input     = 28*28 # = 784
n_output    = 10
```

input and output in separate files,

**Train data set:**

```
train-images-idx3-ubyte
train-labels-idx1-ubyte
```


**Test data set:**

```
t10k-images-idx3-ubyte
t10k-labels-idx1-ubyte
```

```
The ``mnist2petsc`` script converts the MNIST data set into two dense matrices
written to disc in the PETSc dense matrix format.
...

```

```
# train
[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000803(2051) magic number
0004     32 bit integer  60000            number of images
0008     32 bit integer  28               number of rows
0012     32 bit integer  28               number of columns
0016     unsigned byte   ...

[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000801(2049) magic number (MSB first)
0004     32 bit integer  60000            number of items
0008     unsigned byte   ...

# test
[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000803(2051) magic number
0004     32 bit integer  10000            number of images
0008     32 bit integer  28               number of rows
0012     32 bit integer  28               number of columns
0016     unsigned byte   ...

[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000801(2049) magic number (MSB first)
0004     32 bit integer  10000            number of items
0008     unsigned byte   ...
```


**Protocol:**

The data in PETSc format for HANNF was downloaded first and
created

```
$>
wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
gunzip train-images-idx3-ubyte.gz
wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
gunzip train-labels-idx1-ubyte.gz

wget http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
gunzip t10k-images-idx3-ubyte.gz
wget http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
gunzip t10k-labels-idx1-ubyte.gz

./mnist2petsc.py train-images-idx3-ubyte train-labels-idx1-ubyte
./mnist2petsc.py t10k-images-idx3-ubyte t10k-labels-idx1-ubyte
```

Execution times on a MacBook Pro, 2,7 GHz Intel Core i5:

```
$> time ./mnist2petsc.py train-images-idx3-ubyte train-labels-idx1-ubyte
# n_data: 60000
# n_label: 60000

real    0m6.595s
user    0m5.864s
sys    0m0.704s

$> time ./mnist2petsc.py t10k-images-idx3-ubyte t10k-labels-idx1-ubyte
# n_data: 10000
# n_label: 10000

real    0m0.773s
user    0m0.604s
sys    0m0.148s
```

Contents of the `mnist` directory after download and formatting:

```
$> tree -hs
.
├── [3.0K]  README.md
├── [3.5K]  mnist2petsc.py
├── [7.5M]  t10k-images-idx3-ubyte
├── [ 60M]  t10k-images-idx3-ubyte.in.petsc
├── [9.8K]  t10k-labels-idx1-ubyte
├── [781K]  t10k-labels-idx1-ubyte.out.petsc
├── [ 45M]  train-images-idx3-ubyte
├── [359M]  train-images-idx3-ubyte.in.petsc
├── [ 59K]  train-labels-idx1-ubyte
└── [4.6M]  train-labels-idx1-ubyte.out.petsc

0 directories, 10 files
```





