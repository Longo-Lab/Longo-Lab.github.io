---
layout: default
title: Style Guide
nav_order: 3
has_children: false
has_toc: true
permalink: /docs/style_guide
code_folding: hide
---

# Style Guide 
{: .no_toc }

Hello and welcome to the Longo Lab Informatics style guide. This will provide a general reference for Longo Lab members to generate reproduceble code. Open science and all that.

1. Languages
2. Headers
3. Code documentation
4. Maintaining your code via GitHub
5. Etc
{:toc}

## Languages
We end up using quite a few languages in the Longo Lab, but the core of our codebase is centered around `R` for bioinformatic analysis (with `python` supporting) and `sh`ell scripting to interface with the clusters and document any and all command line entries necessary to reproduce research results. In order to keep it manageable we use the folllowing resources for coding style. In addition to basic syntax, each has some resources for checking or modifying code style on the fly

### R and Rnotenook
We use R scripts `*.R` when running analyses in batch mode. For interactive analyses, R markdown notebooks `*.Rmd` provide an easy way to run limited analysis on [SCG OnDemand](https://ondemand.scg.stanford.edu/) and track your notes on one-off analyses and projects.

For R style, [tidyverse style guide](https://style.tidyverse.org/index.html) has been extensively updated by Hadley Wickham and offers a consistent solution *with a code lintr and interactive* `styler`. You can use this resource in an OnDemand Rstudio session to reformat legacy code quickly.

### Python
We primarily use python scripts in batch processing, but [SCG OnDemand](https://ondemand.scg.stanford.edu/) contains the resources for Jupyter notebooks (`*.ipynb`) to generate interactive analysis sessions.
 
For python style, it showed up with [PEP8](https://peps.python.org/pep-0008) baked in, making it pretty easy. There are a number of lintrs to check or [autoformat](https://docs.python-guide.org/writing/style/#auto-formatting) your code.

### Shell scripts
In general shell scripting is not useful for code development, but for `sbatch` submissions to slurm, and for documenting commands used in an analysis. Every analysis folder should have a shell script `00-commands.sh` that records **every** command used in the analysis, including sbatch submissions.

Style is loosely structured around the Google [guide](https://google.github.io/styleguide/shellguide.html) but primarily focused on documentation (see also [Headers](/docs/style_guide#headers) below) 

{: .info-title }
> Linters, stylers & auto-formatting
> 
> These things can make your life much easier by automating the tedious things. In the same way generative ML models for code can speed things along too, by asking it to clean up your code. But you should check with a the output with a linter.


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
In addition to headers, code should also be well commented in the manner of each respective language. In particular, function documentation is a must. To support eventual utilization of functions across multiple scripts, follow the annotation [guidelines](https://roxygen2.r-lib.org/articles/rd.html) for `Roxygen2` package building in R (also see R style guide above):

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


## Maintaining your code via GitHub
An essential component of your research is notes! In order to take notes on code, you need some manner of version control, and for us that is GitHub. Getting started with GitHub can be daunting, but you can start with some simple practice [via their site](https://docs.github.com/en/get-started), and some [tutorials](https://rogerdudler.github.io/git-guide)

{: .note-title }
> SCG scripts are backed up nightly
> 
> A very important reason to keep your analysis on SCG is that all coding scripts are backed up to our GitHub organization page nightly. You are welcome to do your own github commits as you work to save a full history of your code, and to ultimately break out projects on their own respective github projects for more control.

Their are several unusual things about this setup from traditional GitHub projects:
### Only code is backed up to the repository

File sizes on GitHub are limited to 100 MiB, and our primary purpose is script maintenance, so anything other than scripts has to be opted in. Every git parent directory (your project directory), should have a .gitignore file like this:

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

Note that `celltype-gene-database.xlsx` and `overall.name_schema.txt` are special files that have been opted into backup in this folder, and `deploy.R` has been opted out of backups (see [for this reason](https://github.com/Longo-Lab/de_dashboards#deploying-to-shinyappsio)).


### Code is backed up to the `main` branch
Traditionally, commits should not be made to the `main` branch in GitHub. However, the cluster is a shared resource, which will have multiple users working in the same filesystem. If they were trying to each work on a different branches in the same location they would collide. So, an imperfect solution to be sure, but necessary.


### Strategies to follow for effective project control
These are a couple of things to keep your GitHub on the rails: 

#### Break out your own project
The instructions for doing so are [here](https://github.com/Longo-Lab/scg_backup#split-existing-subdirectory-into-separate-repository). You can add it to the nightly backup (by contacting the Senior Research Scientist) or not, but once broken out it is much easier to branch and develop at your own pace.

#### Version control
[Semantic versioning](https://semver.org/) is softly included in each of the script headers above. Use it to gain control of the versions of your scripts on GitHub. We are perpetually stuck in development, so if you ever advance to `v1.0.0`, that will be quite a feat.

#### Tie your commits to issues and projects
When you make a commit, you can tie it to issues by mentioning their `issue #` in the git commit message. It should then go without saying you always add a meaningful commit message to your commits. Also, you can and should link those repository issues to a respective project. If you forget, you can comment on the desired issue with the git-commit-id (e.g. `356b039`).

{: .note-title }
> Note
> 
> Not only can you say, `updated #3`, you can instantly [manage](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests) issues and pull requests by `git commit -m "Closed #5"`

#### USE PROJECTS!
Having a plan and keeping track of it helps a great deal once you have multiple branches, multiple issues, multiple pull requests. See [Project Management](/docs/lab_policies#project-management)


## Etc
For any additional issues that do arise, don't forget to ask for help! troubleshooting is the name of the game in bioinfomatics.

























