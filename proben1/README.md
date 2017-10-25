# Proben1

[https://publikationen.bibliothek.kit.edu/39794/2050](),
copy of data set at github,
[https://github.com/jeffheaton/proben1](),

input and output combined in one file,
train, test and validation data sets combined in one file,
3 versions (different shuffles) of each data set,

text files, numbers separated by a space " ",


```
$>
tree -d
.
└── proben1
    ├── Doc
    ├── Scripts
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

15 directories

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

time ./proben12petsc.py proben1/building/
time ./proben12petsc.py proben1/cancer/
time ./proben12petsc.py proben1/card/
time ./proben12petsc.py proben1/diabetes/
time ./proben12petsc.py proben1/flare/
time ./proben12petsc.py proben1/gene/
time ./proben12petsc.py proben1/glass/
time ./proben12petsc.py proben1/heart/
time ./proben12petsc.py proben1/horse/
time ./proben12petsc.py proben1/mushroom/
time ./proben12petsc.py proben1/soybean/
time ./proben12petsc.py proben1/thyroid/

jpicau@m-053:proben1> du -sh proben1/*
604K    proben1/Doc
4,0K    proben1/Makefile
8,0K    proben1/README.txt
 40K    proben1/Scripts
3,1M    proben1/building
296K    proben1/cancer
1012K   proben1/card
356K    proben1/diabetes
784K    proben1/flare
 10M    proben1/gene
164K    proben1/glass
2,5M    proben1/heart
704K    proben1/horse
 25M    proben1/mushroom
1,7M    proben1/soybean
5,0M    proben1/thyroid

```

