# Sharks

The aim of this project is, after the cleaning of a database, to answer the hypotheses raised with the help of images, maps, graphs... 

![image](https://user-images.githubusercontent.com/79655025/113981717-45243480-9848-11eb-896c-27306986d919.png)

## Table of Contents
1. [General Info](#general-info)
2. [Data treatment](#Data-treatment)
3. [Libraries](#Libraries)
4. [Technology](#Technology)
5. [Methodology](#Methodology)

## General Info and Hypotheses

In this analysis we try to prove some hypotheses through a dataset obtained from Kaggle https://www.kaggle.com/teajay/global-shark-attacks. The Hypotheses are the following: 

### 1. Which shark species are the most aggressive towards humans, and which are the most morbid? 

![Total attacks by specie (1950-2018)](https://user-images.githubusercontent.com/79655025/113989517-ce3f6980-9850-11eb-87b2-769c7c8ca661.png)

As can be seen in the graph above, the white shark is the species with the highest incidence of attacks, followed by the tiger shark and finally the bull shark. the rest are more rare and uncommon attacks, bearing in mind that we analysed over 65 years. 

To analyse the mortality of such attacks. In it we can see that although the white shark species is the one with more fatal attacks, the percentage of dying in an attack by the tiger shark or bull shark is higher. The rest of the species have a very low mortality rate. 

![Mortality by species (1950-2018)](https://user-images.githubusercontent.com/79655025/113990443-c16f4580-9851-11eb-92b5-6d87793bb992.png)


### 2. ¿Dónde hay más ataques? ¿Dónde son más mortales?

![Not Mortal shark attacks (1950-2018)](https://user-images.githubusercontent.com/79655025/113993456-c7b2f100-9854-11eb-94ab-84a62cf82e5c.png)

The map above shows the number of non-fatal attacks per country. We can see with the help of the map below (only fatal attacks) that the relationship is proportional and that the more non-fatal attacks the higher the number of fatal attacks; i.e. we can say that the USA, Australia and South Africa not only have more non-fatal attacks but also more fatal attacks and therefore, either the species are more or less equally distributed all over the world, or the attacks have a similar mortality rate in all countries.

![Mortal_Atacks_by_Country](https://user-images.githubusercontent.com/79655025/113993487-cf729580-9854-11eb-8ac7-b17a970921a1.png)


### 3. ¿Están aumentando los ataques?

![Attacks per year](https://user-images.githubusercontent.com/79655025/114000785-9984df80-985b-11eb-8bca-757328ba424c.png)

This graph shows that the rate of (registered) attacks increases dramatically every year. The reasons for this need to be analysed:

- Are there more and more water sportsmen and women?
- Are there more and more bathers on the beaches?
- Are sharks becoming more aggressive due to overfishing?

These questions should be analysed with other data to explain the increase.


## Data treatment

The realization of the project is divided into up to 3 parts: 

1. Preliminary cleaning of the dataset. (Analysis)
2. Cleaning of the dataset according to the hypotheses. (Analysis)
3. Conclusions above to the hypotheses whit the help of the created graphs and maps.


## Libraries

```
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import regex as re
import src.functions as sr
import pycountry 
import plotly.express as px

```

## Technology: 

A list of technologies used within the project:

1. [Jupyter Notebook](https://jupyter.org/) : Version 6.1.4
2. [Python](https://www.python.org/): Version 3.8
3. [Visual Studio Code](https://code.visualstudio.com/)

## Methodology: 

The realization of the project is divided into up to 3 parts: 

1. Preliminary cleaning of the dataset. 

* Import the df from the files.
* changing the names of the columns, eliminating those that do not help me to solve my hiphothesis and, deleating rows whit more than four missing values
* Cleaning the rows values column by column (Year, Species, Fatal and Country columns) 

2. Cleaning of the dataset according to the hypotheses. 

* Ultimate cleaning from the original dataframe into different dfs
* Creating the visualization to hel answering my hyphothesis 

3. Conclusions according to the hypotheses whit the help of the created graphs and maps.

* Response to the hypotheses raised with the help of images


## Author

* **Bertrán Gil de Santivañes Finat** - *Initial work* - (https://github.com/Bertrangsf/Sharks)
