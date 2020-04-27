# Homework2
###### Contributors: Zahin Ibnat, Tikahari Khanal, Hannah Mathew
#### Necessary Installs (pip3 install -r requirements.txt)
* numpy 1.16.2
* matplotlib 3.0.3

## Overview
In this repository we implement a genetic algorithm to optimize for hydrophobic contact points in 2D protein folding. A sequence of amino acids is read from a fasta file and passed through a genetic algorithm parameterized through command line argumenst (see usage). <br/>
![alt text](https://github.com/ibnatz16/Homework2/blob/master/imgs/GeneticAlgorithm.png?raw=true)
## Usage <br/>
    python3 GeneticAlgorithm.py <filename> <population size> <percent nonrandom selection> <mutation rate>
Percent nonrandom selection and mutation rate should be entered as decimals between 0 and 1
#### Example:
    python3 GeneticAlgorithm.py rcsb_pdb_4BWD.fasta 15 14 0.4 0.0005

## File Structure / Naming Convention <br/>
This repository has the following file structure:<br/>

├── Debug.py<br/>
├── fitness<br/>
├── folding<br/>
│   ├── generations<br/>
│   └── outputs<br/>
├── GeneticAlgorithm.py<br/>
├── Matrix.py<br/>
├── Mutation.py<br/>
├── rcsb_pdb_4BWD.fasta<br/>
├── rcsb_pdb_6EZQ.fasta<br/>
├── README.md<br/>
├── requirements.txt<br/>
├── Score.py<br/>
└── test.fasta<br/>

Plots of the folding for every sequence in every generation can be found in `folding/generations/`. `folding/outputs/` will contain a maximum of 10 similar plots from randomly chosen sequences of the first and last generation of the algorithm. Plots of fitness vs iterations can be found in `fitness/`.<br/><br/>
Plots in `folding/generations/` will be named according to: `<fasta filename>_<population size>_<percent nonrandom selection>_<mutation rate>_gen_<generation number>_seq_<sequence number>.png`<br/><br/>
Plots in `folding/outputs/` will be named according to:  `<fasta filename>_<population size>_<percent nonrandom selection>_<mutation rate>_<plot number>.png`<br/><br/>
Plots in `fitness/` will be named according to: `<fasta filename>_<population size>_<percent nonrandom selection>_<mutation rate>.png`<br/>

## Outputs
The following plots were obtained from the following command: `python3 GeneticAlgorithm.py test.fasta 10 5 .90 0.05`.
#### Generation 0 Sequence 1
![alt text](https://github.com/ibnatz16/Homework2/blob/master/imgs/ex1_gen0.png)
#### Generation 0 Sequence 4
![alt text](https://github.com/ibnatz16/Homework2/blob/master/imgs/ex2_gen0.png)
#### Generation 0 Sequence 6
![alt text](https://github.com/ibnatz16/Homework2/blob/master/imgs/ex3_gen0.png)
#### Generation 5 Sequence 2
![alt text](https://github.com/ibnatz16/Homework2/blob/master/imgs/ex1_genF.png)
#### Generation 5 Sequence 4
![alt text](https://github.com/ibnatz16/Homework2/blob/master/imgs/ex2_genF.png)
#### Generation 5 Sequence 8
![alt text](https://github.com/ibnatz16/Homework2/blob/master/imgs/ex3_genF.png)
#### Fitness Score
![alt text](https://github.com/ibnatz16/Homework2/blob/master/imgs/fitness.png)
