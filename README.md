# applied-statistics

**Author** Jennifer Ibanez Cano

This repository contains the submission of the assessments for the module **Applied Statistic**, part of the HDip in Data Analytics from the ATU, Galway and imparted by the lecture Ian McLoughlin.  

The assessment is presented in the form of a Jupyter Notebook and addresses a set of analytical and computational problems assigned as part of the course requirements.

The details of the problems can be found here [assessment/problems.md](https://github.com/ianmcloughlin/applied-statistics/blob/main/assessment/problems.md)

## Purpose of this repository.

The aim of this module is to be able to demonstrate through the assessments problems the ability to:

- Describe the stochastic nature of real-world measurements.
- Source documentation to programmatically perform a statistical test.
- Select an appropriate statistical test to investigate a claim.
- Perform a statistical test on a data set.

## Learning Outcomes

This assessment assesses the ability to:
- Apply core statistical concepts to structured problems
- Use Python for statistical computation and analysis
- Interpret and explain statistical results
- Present reproducible work using Jupyter Notebooks

## Repository Structure
```
applied-statistics/
├── problems.ipynb          # Main assessment notebook
├── README.md               # Repository documentation
├── requirements.txt 
├── 
└── 
```

## Computing environments Used

The assessment was completed using:
- Python 3.x
- Jupyter Notebook

Primary libraries used include:
- NumPy
- Pandas
- Matplotlib
- SciPy
- Math
- Statsmodels
- Seaborn
- Itertools

## Instructions for Review

To review the assessment:
1. Open `problems.ipynb` using Jupyter Notebook or JupyterLab
2. Run the notebook cells sequentially to reproduce the results
3. Refer to markdown cells for explanations and interpretations








### References for the README 

Problem 1 Lady tasting tea


math.comb(n, k)
https://docs.python.org/3/library/math.html#math.comb

Math factorial

https://docs.python.org/3.12/library/math.html#math.factorial

itertools.combinations

https://docs.python.org/3/library/itertools.html#itertools.combinations

Type I Errors, Type II Errors, and Powe

* Type I and Type II errors: https://en.wikipedia.org/wiki/Type_I_and_type_II_errors#Table_of_error_types
* Power: https://en.wikipedia.org/wiki/Power_(statistics)#Description


Problem 2 Normal distribution.

Normal distribution 

https://en.wikipedia.org/wiki/Normal_distribution

Numpy mean

https://numpy.org/devdocs/reference/generated/numpy.mean.html


Numpy random.normal

https://www.w3schools.com/python/numpy/numpy_random_normal.asp

https://numpy.org/devdocs/reference/random/generated/numpy.random.normal.html

scipy.stats. probplot

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.probplot.html

scipy.stats shapiro
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html

Shapiro-Wilk test for normality
https://docs.scipy.org/doc/scipy/tutorial/stats/hypothesis_shapiro.html#hypothesis-shapiro


Problem 3  T-test

Numpy random.normal
https://numpy.org/doc/2.0/reference/random/generated/numpy.random.normal.html

Numpy plot.subplots

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

seaborn.stripplot

https://seaborn.pydata.org/generated/seaborn.stripplot.html

scipy.stats.  ttest_rel
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html


Problem 4 Anova

Perform a one-way ANOVA
https://www.geeksforgeeks.org/python/how-to-perform-a-one-way-anova-in-python/

scipy.stats.
f_oneway
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html

boxplots 
https://www.geeksforgeeks.org/machine-learning/box-plot/
https://www.jmp.com/en/statistics-knowledge-portal/exploratory-data-analysis/box-plot

color and design for boxplot
https://www.geeksforgeeks.org/data-visualization/box-plot-in-python-using-matplotlib/

