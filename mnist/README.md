# MNIST

[http://yann.lecun.com/exdb/mnist/](),
60'000 images, black/white, unsigned 8 bit int, 1 byte,
28 x 28 pixels,
column major, transpose for reading,

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
# n_data: 60000
# n_label: 60000

./mnist2petsc.py t10k-images-idx3-ubyte t10k-labels-idx1-ubyte
# n_data: 10000
# n_label: 10000

jpicau@m-053:mnist> tree
.
├── README.md
├── mnist2petsc.py
├── t10k-images-idx3-ubyte
├── t10k-images-idx3-ubyte.in.petsc
├── t10k-labels-idx1-ubyte
├── t10k-labels-idx1-ubyte.out.petsc
├── train-images-idx3-ubyte
├── train-images-idx3-ubyte.in.petsc
├── train-labels-idx1-ubyte
└── train-labels-idx1-ubyte.out.petsc

0 directories, 10 files

```





