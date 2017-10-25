# data

Train and test data,

output is always PETSc matrix or vector format,
double precision, big-endian, storage,


# Data sets

## MNIST

[http://yann.lecun.com/exdb/mnist/](),
60'000 images, black/white, unsigned 8 bit int, 1 byte,
column major, transpose for reading,


## SVHN

The Street View House Numbers (SVHN) Dataset,
[http://ufldl.stanford.edu/housenumbers/](),
column major ???,


## Proben1

[https://publikationen.bibliothek.kit.edu/39794/2050](),
copy of data set at github,
[https://github.com/jeffheaton/proben1](),


# Contents

after processing all data:

```
hannf/data> du -sh *
476M    mnist
 53M    proben1
2,5G    svhn
```

Whole directory contents after processing:

```
hannf/data> tree -hs
.
├── [ 34K]  LICENSE
├── [ 19K]  README.md
├── [ 442]  mnist
│   ├── [3.0K]  README.md
│   ├── [3.5K]  mnist2petsc.py
│   ├── [7.5M]  t10k-images-idx3-ubyte
│   ├── [ 60M]  t10k-images-idx3-ubyte.in.petsc
│   ├── [9.8K]  t10k-labels-idx1-ubyte
│   ├── [781K]  t10k-labels-idx1-ubyte.out.petsc
│   ├── [ 45M]  train-images-idx3-ubyte
│   ├── [359M]  train-images-idx3-ubyte.in.petsc
│   ├── [ 59K]  train-labels-idx1-ubyte
│   └── [4.6M]  train-labels-idx1-ubyte.out.petsc
├── [ 204]  proben1
│   ├── [2.0K]  README.md
│   ├── [ 680]  proben1
│   │   ├── [ 136]  Doc
│   │   │   ├── [211K]  proben.dvi
│   │   │   └── [388K]  proben.ps
│   │   ├── [ 479]  Makefile
│   │   ├── [5.9K]  README.txt
│   │   ├── [ 408]  Scripts
│   │   │   ├── [ 496]  README
│   │   │   ├── [ 145]  a
│   │   │   ├── [ 146]  b
│   │   │   ├── [2.5K]  convertheaders
│   │   │   ├── [ 304]  countfields
│   │   │   ├── [ 464]  countmiss
│   │   │   ├── [ 813]  findminmax
│   │   │   ├── [ 141]  out
│   │   │   ├── [1.4K]  partition
│   │   │   └── [ 923]  shuffle
│   │   ├── [ 884]  building
│   │   │   ├── [ 448]  Makefile
│   │   │   ├── [2.1K]  README
│   │   │   ├── [ 89K]  a_ans.dat
│   │   │   ├── [283K]  atrain.dat
│   │   │   ├── [372K]  building.raw
│   │   │   ├── [357K]  building1.dt
│   │   │   ├── [115K]  building1.dt.test.in.petsc
│   │   │   ├── [ 25K]  building1.dt.test.out.petsc
│   │   │   ├── [230K]  building1.dt.train.in.petsc
│   │   │   ├── [ 49K]  building1.dt.train.out.petsc
│   │   │   ├── [357K]  building2.dt
│   │   │   ├── [115K]  building2.dt.test.in.petsc
│   │   │   ├── [ 25K]  building2.dt.test.out.petsc
│   │   │   ├── [230K]  building2.dt.train.in.petsc
│   │   │   ├── [ 49K]  building2.dt.train.out.petsc
│   │   │   ├── [357K]  building3.dt
│   │   │   ├── [115K]  building3.dt.test.in.petsc
│   │   │   ├── [ 25K]  building3.dt.test.out.petsc
│   │   │   ├── [230K]  building3.dt.train.in.petsc
│   │   │   ├── [ 49K]  building3.dt.train.out.petsc
│   │   │   ├── [ 110]  header
│   │   │   ├── [2.0K]  num2cod
│   │   │   ├── [ 833]  out2raw
│   │   │   └── [ 657]  raw2num
│   │   ├── [ 782]  cancer
│   │   │   ├── [ 430]  Makefile
│   │   │   ├── [1.4K]  README
│   │   │   ├── [ 19K]  breast-cancer-wisconsin.data
│   │   │   ├── [5.5K]  breast-cancer-wisconsin.names
│   │   │   ├── [ 26K]  cancer1.dt
│   │   │   ├── [ 12K]  cancer1.dt.test.in.petsc
│   │   │   ├── [2.7K]  cancer1.dt.test.out.petsc
│   │   │   ├── [ 25K]  cancer1.dt.train.in.petsc
│   │   │   ├── [5.5K]  cancer1.dt.train.out.petsc
│   │   │   ├── [ 26K]  cancer2.dt
│   │   │   ├── [ 12K]  cancer2.dt.test.in.petsc
│   │   │   ├── [2.7K]  cancer2.dt.test.out.petsc
│   │   │   ├── [ 25K]  cancer2.dt.train.in.petsc
│   │   │   ├── [5.5K]  cancer2.dt.train.out.petsc
│   │   │   ├── [ 26K]  cancer3.dt
│   │   │   ├── [ 12K]  cancer3.dt.test.in.petsc
│   │   │   ├── [2.7K]  cancer3.dt.test.out.petsc
│   │   │   ├── [ 25K]  cancer3.dt.train.in.petsc
│   │   │   ├── [5.5K]  cancer3.dt.train.out.petsc
│   │   │   ├── [ 106]  header
│   │   │   └── [ 481]  raw2cod
│   │   ├── [ 782]  card
│   │   │   ├── [ 397]  Makefile
│   │   │   ├── [2.1K]  README
│   │   │   ├── [ 92K]  card1.dt
│   │   │   ├── [ 69K]  card1.dt.test.in.petsc
│   │   │   ├── [2.7K]  card1.dt.test.out.petsc
│   │   │   ├── [137K]  card1.dt.train.in.petsc
│   │   │   ├── [5.4K]  card1.dt.train.out.petsc
│   │   │   ├── [ 92K]  card2.dt
│   │   │   ├── [ 69K]  card2.dt.test.in.petsc
│   │   │   ├── [2.7K]  card2.dt.test.out.petsc
│   │   │   ├── [137K]  card2.dt.train.in.petsc
│   │   │   ├── [5.4K]  card2.dt.train.out.petsc
│   │   │   ├── [ 92K]  card3.dt
│   │   │   ├── [ 69K]  card3.dt.test.in.petsc
│   │   │   ├── [2.7K]  card3.dt.test.out.petsc
│   │   │   ├── [137K]  card3.dt.train.in.petsc
│   │   │   ├── [5.4K]  card3.dt.train.out.petsc
│   │   │   ├── [ 31K]  crx.data
│   │   │   ├── [1.5K]  crx.names
│   │   │   ├── [ 107]  header
│   │   │   └── [2.9K]  raw2cod
│   │   ├── [ 782]  diabetes
│   │   │   ├── [ 465]  Makefile
│   │   │   ├── [2.2K]  README
│   │   │   ├── [ 46K]  diabetes1.dt
│   │   │   ├── [ 12K]  diabetes1.dt.test.in.petsc
│   │   │   ├── [3.0K]  diabetes1.dt.test.out.petsc
│   │   │   ├── [ 24K]  diabetes1.dt.train.in.petsc
│   │   │   ├── [6.0K]  diabetes1.dt.train.out.petsc
│   │   │   ├── [ 46K]  diabetes2.dt
│   │   │   ├── [ 12K]  diabetes2.dt.test.in.petsc
│   │   │   ├── [3.0K]  diabetes2.dt.test.out.petsc
│   │   │   ├── [ 24K]  diabetes2.dt.train.in.petsc
│   │   │   ├── [6.0K]  diabetes2.dt.train.out.petsc
│   │   │   ├── [ 46K]  diabetes3.dt
│   │   │   ├── [ 12K]  diabetes3.dt.test.in.petsc
│   │   │   ├── [3.0K]  diabetes3.dt.test.out.petsc
│   │   │   ├── [ 24K]  diabetes3.dt.train.in.petsc
│   │   │   ├── [6.0K]  diabetes3.dt.train.out.petsc
│   │   │   ├── [ 106]  header
│   │   │   ├── [ 23K]  pima-indians-diabetes.data
│   │   │   ├── [3.0K]  pima-indians-diabetes.names
│   │   │   └── [ 600]  raw2cod
│   │   ├── [ 816]  flare
│   │   │   ├── [ 414]  Makefile
│   │   │   ├── [2.6K]  README
│   │   │   ├── [ 27K]  flare.data2
│   │   │   ├── [2.6K]  flare.names
│   │   │   ├── [ 27K]  flare.raw
│   │   │   ├── [ 58K]  flare1.dt
│   │   │   ├── [ 50K]  flare1.dt.test.in.petsc
│   │   │   ├── [6.2K]  flare1.dt.test.out.petsc
│   │   │   ├── [100K]  flare1.dt.train.in.petsc
│   │   │   ├── [ 13K]  flare1.dt.train.out.petsc
│   │   │   ├── [ 58K]  flare2.dt
│   │   │   ├── [ 50K]  flare2.dt.test.in.petsc
│   │   │   ├── [6.2K]  flare2.dt.test.out.petsc
│   │   │   ├── [100K]  flare2.dt.train.in.petsc
│   │   │   ├── [ 13K]  flare2.dt.train.out.petsc
│   │   │   ├── [ 58K]  flare3.dt
│   │   │   ├── [ 50K]  flare3.dt.test.in.petsc
│   │   │   ├── [6.2K]  flare3.dt.test.out.petsc
│   │   │   ├── [100K]  flare3.dt.train.in.petsc
│   │   │   ├── [ 13K]  flare3.dt.train.out.petsc
│   │   │   ├── [ 107]  header
│   │   │   └── [1003]  raw2cod
│   │   ├── [ 816]  gene
│   │   │   ├── [ 473]  Makefile
│   │   │   ├── [1.9K]  README
│   │   │   ├── [312K]  gene.data
│   │   │   ├── [5.2K]  gene.names
│   │   │   ├── [2.6K]  gene.theory
│   │   │   ├── [1.1M]  gene1.dt
│   │   │   ├── [743K]  gene1.dt.test.in.petsc
│   │   │   ├── [ 19K]  gene1.dt.test.out.petsc
│   │   │   ├── [1.5M]  gene1.dt.train.in.petsc
│   │   │   ├── [ 37K]  gene1.dt.train.out.petsc
│   │   │   ├── [1.1M]  gene2.dt
│   │   │   ├── [743K]  gene2.dt.test.in.petsc
│   │   │   ├── [ 19K]  gene2.dt.test.out.petsc
│   │   │   ├── [1.5M]  gene2.dt.train.in.petsc
│   │   │   ├── [ 37K]  gene2.dt.train.out.petsc
│   │   │   ├── [1.1M]  gene3.dt
│   │   │   ├── [743K]  gene3.dt.test.in.petsc
│   │   │   ├── [ 19K]  gene3.dt.test.out.petsc
│   │   │   ├── [1.5M]  gene3.dt.train.in.petsc
│   │   │   ├── [ 37K]  gene3.dt.train.out.petsc
│   │   │   ├── [ 109]  header
│   │   │   └── [ 966]  raw2cod
│   │   ├── [ 782]  glass
│   │   │   ├── [ 414]  Makefile
│   │   │   ├── [1.4K]  README
│   │   │   ├── [ 12K]  glass.data
│   │   │   ├── [3.4K]  glass.names
│   │   │   ├── [ 17K]  glass1.dt
│   │   │   ├── [3.7K]  glass1.dt.test.in.petsc
│   │   │   ├── [2.5K]  glass1.dt.test.out.petsc
│   │   │   ├── [7.5K]  glass1.dt.train.in.petsc
│   │   │   ├── [5.0K]  glass1.dt.train.out.petsc
│   │   │   ├── [ 17K]  glass2.dt
│   │   │   ├── [3.7K]  glass2.dt.test.in.petsc
│   │   │   ├── [2.5K]  glass2.dt.test.out.petsc
│   │   │   ├── [7.5K]  glass2.dt.train.in.petsc
│   │   │   ├── [5.0K]  glass2.dt.train.out.petsc
│   │   │   ├── [ 17K]  glass3.dt
│   │   │   ├── [3.7K]  glass3.dt.test.in.petsc
│   │   │   ├── [2.5K]  glass3.dt.test.out.petsc
│   │   │   ├── [7.5K]  glass3.dt.train.in.petsc
│   │   │   ├── [5.0K]  glass3.dt.train.out.petsc
│   │   │   ├── [ 104]  header
│   │   │   └── [ 982]  raw2cod
│   │   ├── [2.5K]  heart
│   │   │   ├── [1.5K]  Makefile
│   │   │   ├── [4.5K]  README
│   │   │   ├── [ 107]  header
│   │   │   ├── [ 107]  header_a
│   │   │   ├── [ 105]  header_ac
│   │   │   ├── [ 105]  header_c
│   │   │   ├── [9.8K]  heart-disease.names
│   │   │   ├── [ 39K]  heart.raw
│   │   │   ├── [ 90K]  heart1.dt
│   │   │   ├── [ 63K]  heart1.dt.test.in.petsc
│   │   │   ├── [3.6K]  heart1.dt.test.out.petsc
│   │   │   ├── [126K]  heart1.dt.train.in.petsc
│   │   │   ├── [7.2K]  heart1.dt.train.out.petsc
│   │   │   ├── [ 90K]  heart2.dt
│   │   │   ├── [ 63K]  heart2.dt.test.in.petsc
│   │   │   ├── [3.6K]  heart2.dt.test.out.petsc
│   │   │   ├── [126K]  heart2.dt.train.in.petsc
│   │   │   ├── [7.2K]  heart2.dt.train.out.petsc
│   │   │   ├── [ 90K]  heart3.dt
│   │   │   ├── [ 63K]  heart3.dt.test.in.petsc
│   │   │   ├── [3.6K]  heart3.dt.test.out.petsc
│   │   │   ├── [126K]  heart3.dt.train.in.petsc
│   │   │   ├── [7.2K]  heart3.dt.train.out.petsc
│   │   │   ├── [ 90K]  hearta1.dt
│   │   │   ├── [ 63K]  hearta1.dt.test.in.petsc
│   │   │   ├── [1.8K]  hearta1.dt.test.out.petsc
│   │   │   ├── [126K]  hearta1.dt.train.in.petsc
│   │   │   ├── [3.6K]  hearta1.dt.train.out.petsc
│   │   │   ├── [ 90K]  hearta2.dt
│   │   │   ├── [ 63K]  hearta2.dt.test.in.petsc
│   │   │   ├── [1.8K]  hearta2.dt.test.out.petsc
│   │   │   ├── [126K]  hearta2.dt.train.in.petsc
│   │   │   ├── [3.6K]  hearta2.dt.train.out.petsc
│   │   │   ├── [ 90K]  hearta3.dt
│   │   │   ├── [ 63K]  hearta3.dt.test.in.petsc
│   │   │   ├── [1.8K]  hearta3.dt.test.out.petsc
│   │   │   ├── [126K]  hearta3.dt.train.in.petsc
│   │   │   ├── [3.6K]  hearta3.dt.train.out.petsc
│   │   │   ├── [ 31K]  heartac1.dt
│   │   │   ├── [ 21K]  heartac1.dt.test.in.petsc
│   │   │   ├── [ 616]  heartac1.dt.test.out.petsc
│   │   │   ├── [ 42K]  heartac1.dt.train.in.petsc
│   │   │   ├── [1.2K]  heartac1.dt.train.out.petsc
│   │   │   ├── [ 31K]  heartac2.dt
│   │   │   ├── [ 21K]  heartac2.dt.test.in.petsc
│   │   │   ├── [ 616]  heartac2.dt.test.out.petsc
│   │   │   ├── [ 42K]  heartac2.dt.train.in.petsc
│   │   │   ├── [1.2K]  heartac2.dt.train.out.petsc
│   │   │   ├── [ 31K]  heartac3.dt
│   │   │   ├── [ 21K]  heartac3.dt.test.in.petsc
│   │   │   ├── [ 616]  heartac3.dt.test.out.petsc
│   │   │   ├── [ 42K]  heartac3.dt.train.in.petsc
│   │   │   ├── [1.2K]  heartac3.dt.train.out.petsc
│   │   │   ├── [ 31K]  heartc1.dt
│   │   │   ├── [ 21K]  heartc1.dt.test.in.petsc
│   │   │   ├── [1.2K]  heartc1.dt.test.out.petsc
│   │   │   ├── [ 42K]  heartc1.dt.train.in.petsc
│   │   │   ├── [2.4K]  heartc1.dt.train.out.petsc
│   │   │   ├── [ 31K]  heartc2.dt
│   │   │   ├── [ 21K]  heartc2.dt.test.in.petsc
│   │   │   ├── [1.2K]  heartc2.dt.test.out.petsc
│   │   │   ├── [ 42K]  heartc2.dt.train.in.petsc
│   │   │   ├── [2.4K]  heartc2.dt.train.out.petsc
│   │   │   ├── [ 31K]  heartc3.dt
│   │   │   ├── [ 21K]  heartc3.dt.test.in.petsc
│   │   │   ├── [1.2K]  heartc3.dt.test.out.petsc
│   │   │   ├── [ 42K]  heartc3.dt.train.in.petsc
│   │   │   ├── [2.4K]  heartc3.dt.train.out.petsc
│   │   │   ├── [ 18K]  processed.cleveland.data
│   │   │   ├── [ 10K]  processed.hungarian.data
│   │   │   ├── [4.0K]  processed.switzerland.data
│   │   │   ├── [6.6K]  processed.va.data
│   │   │   └── [2.4K]  raw2cod
│   │   ├── [ 850]  horse
│   │   │   ├── [ 414]  Makefile
│   │   │   ├── [5.1K]  README
│   │   │   ├── [ 105]  header
│   │   │   ├── [ 25K]  horse-colic.data
│   │   │   ├── [8.8K]  horse-colic.names
│   │   │   ├── [5.7K]  horse-colic.test
│   │   │   ├── [ 30K]  horse.raw
│   │   │   ├── [ 59K]  horse1.dt
│   │   │   ├── [ 41K]  horse1.dt.test.in.petsc
│   │   │   ├── [2.1K]  horse1.dt.test.out.petsc
│   │   │   ├── [ 82K]  horse1.dt.train.in.petsc
│   │   │   ├── [4.3K]  horse1.dt.train.out.petsc
│   │   │   ├── [ 59K]  horse2.dt
│   │   │   ├── [ 41K]  horse2.dt.test.in.petsc
│   │   │   ├── [2.1K]  horse2.dt.test.out.petsc
│   │   │   ├── [ 82K]  horse2.dt.train.in.petsc
│   │   │   ├── [4.3K]  horse2.dt.train.out.petsc
│   │   │   ├── [ 59K]  horse3.dt
│   │   │   ├── [ 41K]  horse3.dt.test.in.petsc
│   │   │   ├── [2.1K]  horse3.dt.test.out.petsc
│   │   │   ├── [ 82K]  horse3.dt.train.in.petsc
│   │   │   ├── [4.3K]  horse3.dt.train.out.petsc
│   │   │   └── [4.3K]  raw2cod
│   │   ├── [ 850]  mushroom
│   │   │   ├── [ 193]  Index
│   │   │   ├── [ 465]  Makefile
│   │   │   ├── [3.5K]  README
│   │   │   ├── [ 853]  README.orig
│   │   │   ├── [365K]  agaricus-lepiota.data
│   │   │   ├── [4.1K]  agaricus-lepiota.names
│   │   │   ├── [ 111]  header
│   │   │   ├── [2.1M]  mushroom1.dt
│   │   │   ├── [1.9M]  mushroom1.dt.test.in.petsc
│   │   │   ├── [ 32K]  mushroom1.dt.test.out.petsc
│   │   │   ├── [3.9M]  mushroom1.dt.train.in.petsc
│   │   │   ├── [ 63K]  mushroom1.dt.train.out.petsc
│   │   │   ├── [2.1M]  mushroom2.dt
│   │   │   ├── [1.9M]  mushroom2.dt.test.in.petsc
│   │   │   ├── [ 32K]  mushroom2.dt.test.out.petsc
│   │   │   ├── [3.9M]  mushroom2.dt.train.in.petsc
│   │   │   ├── [ 63K]  mushroom2.dt.train.out.petsc
│   │   │   ├── [2.1M]  mushroom3.dt
│   │   │   ├── [1.9M]  mushroom3.dt.test.in.petsc
│   │   │   ├── [ 32K]  mushroom3.dt.test.out.petsc
│   │   │   ├── [3.9M]  mushroom3.dt.train.in.petsc
│   │   │   ├── [ 63K]  mushroom3.dt.train.out.petsc
│   │   │   └── [3.3K]  raw2cod
│   │   ├── [ 816]  soybean
│   │   │   ├── [ 556]  Makefile
│   │   │   ├── [6.3K]  README
│   │   │   ├── [ 108]  header
│   │   │   ├── [6.3K]  raw2cod
│   │   │   ├── [ 26K]  soybean-large.data
│   │   │   ├── [5.1K]  soybean-large.names
│   │   │   ├── [ 32K]  soybean-large.test
│   │   │   ├── [144K]  soybean1.dt
│   │   │   ├── [109K]  soybean1.dt.test.in.petsc
│   │   │   ├── [ 25K]  soybean1.dt.test.out.petsc
│   │   │   ├── [219K]  soybean1.dt.train.in.petsc
│   │   │   ├── [ 51K]  soybean1.dt.train.out.petsc
│   │   │   ├── [144K]  soybean2.dt
│   │   │   ├── [109K]  soybean2.dt.test.in.petsc
│   │   │   ├── [ 25K]  soybean2.dt.test.out.petsc
│   │   │   ├── [219K]  soybean2.dt.train.in.petsc
│   │   │   ├── [ 51K]  soybean2.dt.train.out.petsc
│   │   │   ├── [144K]  soybean3.dt
│   │   │   ├── [109K]  soybean3.dt.test.in.petsc
│   │   │   ├── [ 25K]  soybean3.dt.test.out.petsc
│   │   │   ├── [219K]  soybean3.dt.train.in.petsc
│   │   │   └── [ 51K]  soybean3.dt.train.out.petsc
│   │   └── [ 850]  thyroid
│   │       ├── [ 519]  Makefile
│   │       ├── [2.1K]  README
│   │       ├── [4.3K]  ann-Readme
│   │       ├── [236K]  ann-test.data
│   │       ├── [4.1K]  ann-thyroid.names
│   │       ├── [259K]  ann-train.data
│   │       ├── [ 110]  header
│   │       ├── [ 457]  raw2cod
│   │       ├── [508K]  thyroid1.dt
│   │       ├── [295K]  thyroid1.dt.test.in.petsc
│   │       ├── [ 42K]  thyroid1.dt.test.out.petsc
│   │       ├── [591K]  thyroid1.dt.train.in.petsc
│   │       ├── [ 84K]  thyroid1.dt.train.out.petsc
│   │       ├── [508K]  thyroid2.dt
│   │       ├── [295K]  thyroid2.dt.test.in.petsc
│   │       ├── [ 42K]  thyroid2.dt.test.out.petsc
│   │       ├── [591K]  thyroid2.dt.train.in.petsc
│   │       ├── [ 84K]  thyroid2.dt.train.out.petsc
│   │       ├── [508K]  thyroid3.dt
│   │       ├── [295K]  thyroid3.dt.test.in.petsc
│   │       ├── [ 42K]  thyroid3.dt.test.out.petsc
│   │       ├── [591K]  thyroid3.dt.train.in.petsc
│   │       └── [ 84K]  thyroid3.dt.train.out.petsc
│   └── [4.1K]  proben12petsc.py
└── [ 374]  svhn
    ├── [1.9K]  README.md
    ├── [2.7K]  svhn2petsc.py
    ├── [ 61M]  test_32x32.mat
    ├── [610M]  test_32x32.mat.in.petsc
    ├── [2.0M]  test_32x32.mat.out.petsc
    ├── [174M]  train_32x32.mat
    ├── [1.7G]  train_32x32.mat.in.petsc
    └── [5.6M]  train_32x32.mat.out.petsc

18 directories, 352 files
jpicau@m-053:data>

```




