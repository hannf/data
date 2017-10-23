# MNIST

[http://yann.lecun.com/exdb/mnist/]()

60'000 images, black/white, unsigned 8 bit int, 1 byte,

column major, transpose for reading,

**Protocol:**

```
$>
cd mnist
wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
./mnist2petsc ...
```

