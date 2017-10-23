# SVHN

The Street View House Numbers (SVHN) Dataset
[http://ufldl.stanford.edu/housenumbers/]()

column major ???

**Protocol:**

```
$>
wget http://ufldl.stanford.edu/housenumbers/train_32x32.mat
wget http://ufldl.stanford.edu/housenumbers/test_32x32.mat
./svhn2petsc.py train_32x32.mat
n_data: 73257
./svhn2petsc.py test_32x32.mat
n_data: 26032

ls train_32x32.mat*
train_32x32.mat train_32x32.mat.data.petsc train_32x32.mat.label.petsc

```


