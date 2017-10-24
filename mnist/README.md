# MNIST

[http://yann.lecun.com/exdb/mnist/]()

60'000 images, black/white, unsigned 8 bit int, 1 byte,

column major, transpose for reading,

```
# train
[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000803(2051) magic number
0004     32 bit integer  60000            number of images
0008     32 bit integer  28               number of rows
0012     32 bit integer  28               number of columns
0016     ...

[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000801(2049) magic number (MSB first)
0004     32 bit integer  60000            number of items
0008     ...

# test
[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000803(2051) magic number
0004     32 bit integer  10000            number of images
0008     32 bit integer  28               number of rows
0012     32 bit integer  28               number of columns
0016     ...

[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000801(2049) magic number (MSB first)
0004     32 bit integer  10000            number of items
0008     ...
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

./mnist2petsc ...
```

