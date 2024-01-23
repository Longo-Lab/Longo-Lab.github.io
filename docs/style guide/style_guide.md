---
layout: default
title: Style Guide
nav_order: 3
has_children: false
has_toc: true
permalink: /docs/style_guide
code_folding: hide
---

# Under Construction...
{: .no_toc }

# Style Guide 
{: .no_toc }

Hello and welcome to the Longo Lab Informatics style guide. This will provide a general reference for Longo Lab members to generate reproduceble code. Open science and all that.

1. Languages
2. Headers
3. Code documentation
4. Maintaining your code via Github
5. Etc
{:toc}

## Languages
We end up using quite a few languages in the Longo Lab, but the core of our codebase is centered around `R` for bioinformatic analysis (with `python` supporting) and `sh`ell scripting to interface with the clusters and document any and all command line entries necessary to reproduce research results. In order to keep it manageable 

### R and Rnotenook

### Python

### Shell scripts

More to come here...

## Headers
Another universal policy is that all scripts be they `*.py`, `*.R`, or `*.???` should have a script header that describes what the script does. We have plenty of legacy code lying around that the author themself couldn't figure out. Give it a month or two and you too can be the proud owner of a mystery box. So think of this as **mandatory**. Here are some examples of helpful information to include in your header (templates are available on SCG in the `scripts` folder): 

<details markdown=1>
  <summary>R script header</summary>
```r
#!/usr/bin/env Rscript
#' ---------------------------
#'
#' Script name: 12_sc_wkflow_subclass_de.R
#'
#' Version: 0.1.0
#'
#' Purpose of script: Performing differential expression after integration
#'
#' Author: Robert R Butler III
#'
#' Date Created: 2022-08-29
#'
#' Copyright (c) 2022
#' Email: rrbutler@stanford.edu
#'
#' ---------------------------
#'
#' Notes:
#'
#'   This version introduces a breaking change, shifting date prefixes to round
#'   numbers
#'
#'   Usage:
#'     sbatch -J MG --mem=50G -c 8 -t 01:00:00 -p interactive \
#'       -o %x/%A_sc_wkflow_subclass_de_%x.log \
#'       --wrap "ml R/4.0; Rscript 12_sc_wkflow_subclass_de.R MG R6"
#'
#'   or interactive session:
#'     sdev -m 50 -c 8 -t 01:00:00 -p interactive
#'
#' ---------------------------

#' load up the packages we will need:  (uncomment as required)

library(Seurat)
library(future.apply)
library(patchwork)
library(ggplot2)
library(ggrepel)
library(ggpubr)
library(data.table)
library(stringr)
library(Cairo)
library(dplyr)
library(RColorBrewer)

#' ---------------------------
```
</details>

<details markdown=1>
  <summary>py script header</summary>
```py
#!/usr/bin/env python
#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
Pipeline for generating a gene-set analysis using MAGMA a set of gene lists.
Runs with a range of annotation windows surrounding the gene, and can
incorporate gene-set covariate files as defined by magma
"""

# Futures
from __future__ import print_function
# […]

# Built-in/Generic Imports
import os
import sys
# […]

# Libs
import logging
import argparse
import datetime
import subprocess as sp
# […]

# Own modules
# […]

# global variables
__author__ = 'Robert R Butler III, William A. Johnson'
__copyright__ = 'Copyright 2023, Longo Lab'
__version__ = '0.0.12'
__maintainer__ = 'Robert R Butler III'
__email__ = 'rrbutler@stanford.edu'
```
</details>

<details markdown=1>
  <summary>shell script header</summary>
```sh
#!/usr/bin/env bash

###################################################################
#Script Name  : 01-magma_command_curated.sh 
#Description  : Runs magma on PREDICT-HD set using 0kb window
#Usage        : sbatch 01-magma_command_curated.sh
#Author       : Robert R Butler III
#Date Created : 2023-08-11
#Email        : rrbutler@stanford.edu
#Copyright (c) 2023
###################################################################
```
</details>


## Code documentation
In addition to headers, code should also be well commented in the manner of each respective language. In particular, function annotation is a must. To support eventual utilization of functions across multiple scripts, follow the annotation [guidelines](https://roxygen2.r-lib.org/articles/rd.html) for `Roxygen2` package building in R (also see R style guide above):

<details markdown=1>
  <summary>R function documentation</summary>
```r
# Define functions --------------------

#' For a given column of common names, replace them with ensembl gene ids.
#' Includes a filter for autosomal genes that are not pseudo or small RNAs.
#'
#' @param dt Data table to replace names
#' @param colname Name of the column containing gene symbols
#' @param keep.symbols Boolean, retain the symbols column?
#'
#' @return dt with a GENE column
convert_gene_symbol <- function(dt, colname, keep.symbols = FALSE) {
...
```
</details>


For python, we can stick with relatively simple [docstrings](https://realpython.com/documenting-python-code/#docstring-types) for functions and classes:

<details markdown=1>
  <summary>py function documentation</summary>
```py
def get_spreadsheet_cols(file_loc, print_cols=False):
    """Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    file_loc : str
        The file location of the spreadsheet
    print_cols : bool, optional
        A flag used to print the columns to the console (default is
        False)

    Returns
    -------
    list
        a list of strings used that are the header columns
    """

    file_data = pd.read_excel(file_loc)
    ...
```
</details>


<details markdown=1>
  <summary>py class documentation</summary>
```py
class Animal:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    says_str = "A {name} says {sound}"
```
</details>


## Maintaining your code via Github
An essential component of your research is notes! In order to take notes on code, you need some manner of version control, and for us that is GitHub. Getting started with GitHub can be daunting, but you can start with some simple practice [via their site](https://docs.github.com/en/get-started), and some [tutorials](https://rogerdudler.github.io/git-guide)

{: .note-title }
> SCG scripts are backed up nightly
> 
> A very important reason to keep your analysis on SCG is that all coding scripts are backed up to our Github organization page nightly. You are welcome to do your own github commits as you work to save a full history of your code, and expected to ultimately break out projects on their own respective github projects for more control (for more on this, see the [lab_policies](/docs/lab_policies) section and the [tutorial](/docs/tutorials/github_project)).

Their are several unusual things about this setup from traditional GitHub projects:
### Only code is backed up to the repository

File sizes on Github are limited to 100 MiB, and our primary purpose is script maintenance, so anything other than scripts has to be opted in. Every git parent directory (your project directory), should have a .gitignore file like this:

<details markdown=1>
  <summary>.gitignore</summary>
```sh
# Ignore everything
*

# But not these files...
!*.sh
!*.pl
!*.py
!*.R
!*.Rmd
!*.ipynb
!*.md
!README.md
!.gitignore
!celltype-gene-database.xlsx
!overall.name_schema.txt
# etc...

# ...even if they are in subdirectories
!*/
.Rproj.user

# But do ignore these files...
deploy.R
```
</details>

Note that `celltype-gene-database.xlsx` and `overall.name_schema.txt` are special files that have been opted in to backup in this folder, and `deploy.R` has been opted out of backups (see [for this reason]).


### Code is backed up to the `main` 

### ...

### Strategies to follow for effective project control

#### Break out your own project

#### Never




## Etc

