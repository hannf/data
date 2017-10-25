# Proben1

[https://publikationen.bibliothek.kit.edu/39794/2050](),
copy of data set at github,
[https://github.com/jeffheaton/proben1](),

input and output combined in one file,
train, test and validation data sets combined in one file,
3 versions (different shuffles) of each data set,

text files, numbers separated by a space " ",


```
jpicau@m-053:proben1> tree -L 1
.
├── building
├── cancer
├── card
├── diabetes
├── flare
├── gene
├── glass
├── heart
├── horse
├── mushroom
├── soybean
└── thyroid
```

header file format, numbers are examples,

```
bool_in=0
real_in=14
bool_out=0
real_out=3
training_examples=2104
validation_examples=1052
test_examples=1052
```


**Protocol:**

```
$>
cd proben1
git clone https://github.com/jeffheaton/proben1.git

./proben12petsc.py proben1/building/
./proben12petsc.py proben1/cancer/
./proben12petsc.py proben1/card/
./proben12petsc.py proben1/diabetes/
./proben12petsc.py proben1/flare/
./proben12petsc.py proben1/gene/
./proben12petsc.py proben1/glass/
./proben12petsc.py proben1/heart/
./proben12petsc.py proben1/horse/
./proben12petsc.py proben1/mushroom/
./proben12petsc.py proben1/soybean/
./proben12petsc.py proben1/thyroid/

```

