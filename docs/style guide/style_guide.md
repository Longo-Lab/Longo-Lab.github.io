---
layout: default
title: Style Guide
nav_order: 3
has_children: false
has_toc: true
permalink: /docs/style_guide
---

# Under Construction...

# Style Guide 
Hello and welcome to the Longo Lab Informatics style guide. This will provide a general reference for Longo Lab members to generate reproduceble code. Open science and all that.

## Maintaining your code via Github
An essential component of your research is notes! In order to take notes on code, you need some manner of version control, and for us that is GitHub. Getting started with GitHub can be daunting, but you can start with some simple practice [via their site](https://docs.github.com/en/get-started), and some [tutorials](https://rogerdudler.github.io/git-guide)

{: .note-title }
> SCG scripts are backed up nightly
> 
> A very important reason to keep your analysis on SCG is that all coding scripts are backed up to our Github organization page nightly. You are welcome to do your own github commits as you work to save a full history of your code, and expected to ultimately break out projects on their own respective github projects for more control (for more on this, see the [lab_policies](/docs/lab_policies) section and the [tutorial](/docs/tutorials/github_project)).

More to come here...

## Headers
Another universal policy is that all scripts be they `*.py`, `*.R`, or `*.???` should have a script header that describes what the script does. We have plenty of legacy code lying around that the author themself couldn't figure out. Give it a month or two and you too can be the proud owner of a mystery box. So think of this as **mandatory**. Here are some examples of helpful information to include in your header (templates are available on SCG in the `scripts` folder): 

### R script header

```r
#!/usr/bin/env Rscript
## ---------------------------
##
## Script name: 12_sc_wkflow_subclass_de.R
##
## Version: 0.1.0
##
## Purpose of script: Performing differential expression after integration
##
## Author: Robert R Butler III
##
## Date Created: 2022-08-29
##
## Copyright (c) 2022
## Email: rrbutler@stanford.edu
##
## ---------------------------
##
## Notes:
##
##   This version introduces a breaking change, shifting date prefixes to round
##   numbers
##
##   Usage:
##     sbatch -J MG --mem=50G -c 8 -t 01:00:00 -p interactive \
##       -o %x/%A_sc_wkflow_subclass_de_%x.log \
##       --wrap "ml R/4.0; Rscript 12_sc_wkflow_subclass_de.R MG R6"
##
##   or interactive session:
##     sdev -m 50 -c 8 -t 01:00:00 -p interactive
##
## ---------------------------

## load up the packages we will need:  (uncomment as required)

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

## ---------------------------
```

### Python script header

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

### Shell script header

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

## Annotation

# Languages

## R and Rnotenook

## Python

## Shell scripts

## Etc

