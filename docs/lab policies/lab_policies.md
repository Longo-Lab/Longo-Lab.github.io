---
layout: default
title: Lab Policies
nav_order: 1
has_children: false
has_toc: true
permalink: /docs/lab_policies
---

# Under Construction...
{: .no_toc }

# General Data Organization
{: .no_toc }

For the purposes of general organization, it is good to think about what components exist in a research project. This is not the phase based components of project management, but the actual tangibles that can be grouped into four categories:

1. Data storage
2. Data processing
3. Project Management
4. Project Communication
{:toc}

All of these elements are ideally maintained in resources that they are suited for.

## Data Storage

While not all datasets can be immediately transferred to Stanford's [Oak Storage](https://uit.stanford.edu/service/oak-storage), any that can be should be on there. For our lab, primary access to Oak is through our [SCG](https://login.scg.stanford.edu/) account. If you are a lab member this is where you can backup your data, organized into projects. Your working machine should be set up with the University's [CrashPlan](https://uit.stanford.edu/service/crashplan) setup.
Importantly if you are going to be using High Risk data in your project, both your computer and the server need to be configured appropriately, and we will design a specific data plan (i.e. not on Oak/SCG).

Ultimately, all raw data will be deposited in the appropriate repository during publication, and code for generating data will be backed up and made available as described below. Importantly, this all happens through SCG, so...put your project on SCG.

{: .info-title }
> Project naming
> 
> The easiest way to track data is by `model_compound_experiment` nomenclature. Use ALL CAPS for the mouse model and compound and make sure to always use underscores `_` instead of spaces. When creating a new project folder, be sure to check first if you are unsure, because it is much harder to change that project folder name than anything else about the project.

As you can see in the [projects](/docs/projects) section, a certain amount of information is automatically connected between SCG and our other management tools. In order to keep projects straight, it is essential to know where your project goes and what it is called. Every SCG user has a `$HOME` folder. If you are demo-ing something, that is where you can try things out. The Longo Lab itself has a Lab folder, and in here, all data should be organized by project. 

## Data Processing

Stanford provides high end computing clusters [SGC]() and [Sherlock]() for this purpose, and while computing on your laptop is sometimes appropriate, it is encouraged to use the clusters whenever possible to (1) Facilitate the proper storage of your data, (2) facilitate managing and sharing your data with your collaborators and (3) not waste your time.

While cluster computing can be intimidating, SCG has made efforts to make this simpler with [OnDenmand]() graphical versions of common analytical software. Software that is associated with certain machines may not work in a cluster, but even in that case it is recommended to process the data on that machine and then transfer results to SCG.

{: .note-title }
> Code maintenance via GitHub
> 
> A very important reason to keep your analysis on SCG in addition your data is that all coding scripts are backed up to our Github organization page nightly. You are welcome to do your own github commits as you work to save a full history of your code, and if your are particularly willing, you can enforce version control too (for more on this, see the [style guide](/docs/style_guide) section).

## Project Management

Outlines, dashboards

{: .note-title }
> Project organization via GitHub
> 
> Here thar be workflow dashboards

## Project Communication
Papers, figures, Slack, email, making your code available... 

{: .note-title }
> Dashboards and code availability for your project
> 
> All of those private project repos can be flipped to public when your paper comes out. Making it really easy to auto generate your paper's "code availablity" section




