# data
Train and test data

output is always PETSc matrix or vector format,
double precision, big-endian, storage

# Data sets

## MNIST

[http://yann.lecun.com/exdb/mnist/]()

60'000 images, black/white, unsigned 8 bit int, 1 byte,

column major, transpose for reading,


**Protocol:**

```
$>
cd mnist
wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz

```

## SVHN

The Street View House Numbers (SVHN) Dataset
[http://ufldl.stanford.edu/housenumbers/]()

column major ???

**Protocol:**

```
$>
cd svhn
wget http://ufldl.stanford.edu/housenumbers/train_32x32.mat
wget http://ufldl.stanford.edu/housenumbers/test_32x32.mat

```

## Proben1

[https://publikationen.bibliothek.kit.edu/39794/2050]()

copy of data set at github,
[https://github.com/jeffheaton/proben1]()

**Protocol:**

```
$>
cd proben1
git clone https://github.com/jeffheaton/proben1.git

```

