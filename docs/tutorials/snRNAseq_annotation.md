---
layout: annot
title: snRNAseq annotation
parent: Tutorials
nav_order: 3
---

# snRNAseq annotation
{: .no_toc }

For our single-nucleus RNA sequencing [projects](/docs/projects), we use an iterative clustering process to annotate the cell types. This page provides a walkthrough of our methods and a tutorial on how to perform the manual annotations.

{: .info-title }
> Important
>
> We use Seurat v4 for this tutorial.

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

## Iterative clustering

The workflow begins with [pre-processing](#sample-pre-processing) the sequencing data from each sample before combining them into a single overall Seurat object. [Automated annotation](#reference-mapping) is first used in attempt to identify and label cell types based on reference data. The Seurat object is then iteratively [integrated and clustered](#integration-and-clustering) at the overall, class, neighborhood, and subclass levels, where [manual annotation](#manual-annotation) is performed at each round to try and verify the cell types.

### Sample pre-processing

The samples are first processed using the [Cell Ranger pipelines](https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/using/count) from 10x Genomics to generate counts data.

[SoupX](https://cran.r-project.org/web/packages/SoupX/index.html) is then used to remove contamination from the data, and [DoubletFinder](https://github.com/chris-mcginnis-ucsf/DoubletFinder) is used to remove heterotypic duplicates.

### Reference mapping

[Reference mapping](https://satijalab.org/seurat/articles/integration_mapping.html) is the process of transferring cell type information from a reference dataset to our query dataset.

We use the following data sources as reference:

- Neuronal cell types from [Allen Brain Atlas](https://portal.brain-map.org/atlases-and-data/rnaseq)
- Non-neuronal cell types from [Ximerakis, et al. (2019)](https://pubmed.ncbi.nlm.nih.gov/31551601/)

### Integration and clustering

For most of our projects, we have data from both wildtype and transgenic mice, as well as drug treated and vehicle mice. In order to concurrently annotate data across these different experimental groups, we must first properly align these datasets in a process known as [integration](https://satijalab.org/seurat/articles/integration_introduction).

To do this, the Seurat object is split by experimental group, normalized, and recombined through integration. Specifically, we use [SCTransform](https://satijalab.org/seurat/articles/sctransform_vignette.html) as the normalization method to better correct for conditional differences without removing biological effects.

Integration is performed at the overall, class, and neighborhood levels, but not the subclass level as there are often too few cells in those groups. Instead, SCTransform is performed directly on the entire subclass. Finally, the cells are re-clustered at each level and their identity is evaluated via [manual annotation](#manual-annotation).

## Manual annotation

While [automated annotation](#reference-mapping) can be a good start, it is shown that manual verification is still necessary in order to produce the best results for cell type annotations ([Clarke, 2021](https://www.nature.com/articles/s41596-021-00534-0)). 

The following sections provide a guide for what to look for when performing manual annotations. Generally, each [cluster](#integration-and-clustering) can be assigned to a single cell type classification; however, if there continues to be chimeric contamination at the subclass level, [further subclustering](#further-subclustering) may be needed in order to separate the distinct groups of cells.

### Predicted cell types

A good place to start when annotating a cluster is to look at the predicted cell type of the cells that make up the cluster, as determined during the [automated annotation](#reference-mapping). Note that each prediction is accompanied by a confidence score indicating how reliable it is, which can be useful to keep in mind.

### Gene markers

One of the more definitive ways to verify the identity of a cluster is by looking at what genes they express. Most cell types have a unique combination of marker genes that set them apart from other types.

Use the following interactive figure to explore broad marker genes for each cell type:

<div id="plot"></div>

We use marker genes from the following sources:

1. A taxonomy of transcriptomic cell types across the isocortex and hippocampal formation ([Yao, 2021](https://pubmed.ncbi.nlm.nih.gov/34004146/))
  - [Whole cortex & hippocampus - 10x genomics (2020) with 10x-smart-seq taxonomy (2021)](https://celltypes.brain-map.org/rnaseq/mouse_ctx-hpf_10x) from [Allen Brain Map](https://portal.brain-map.org/atlases-and-data/rnaseq)
1. Single-cell transcriptomic profiling of the aging mouse brain ([Ximerakis, 2019](https://pubmed.ncbi.nlm.nih.gov/31551601/))
1. Integrative single-cell analysis of transcriptional and epigenetic states in the human adult brain ([Lake, 2018](https://pubmed.ncbi.nlm.nih.gov/29227469/))
1. The TREM2-APOE Pathway Drives the Transcriptional Phenotype of Dysfunctional Microglia in Neurodegenerative Diseases ([Krasemann, 2017](https://pubmed.ncbi.nlm.nih.gov/28930663/))
1. Disease-associated oligodendrocyte responses across neurodegenerative diseases ([Pandey, 2022](https://pubmed.ncbi.nlm.nih.gov/36001972/))
1. A human brain vascular atlas reveals diverse mediators of Alzheimer's risk ([Yang, 2022](https://pubmed.ncbi.nlm.nih.gov/35165441/))

<div class="tabset">
  <div class="active" data-tab="gabaergic">GABAergic</div>
  <div data-tab="glutamatergic">Glutamatergic</div>
  <div data-tab="non-neuronal">Non-Neuronal</div>
</div>

<div id="gabaergic" class="tab active" markdown="1">

{: .note-title }
> Note
>
> The **GABAergic** class contains the **CGE** and **MGE** neighborhoods.

Caudal ganglionic eminence (CGE)
{: .label .label-purple }

[![](/assets/images/yao_gab_CGE.jpg)](https://pubmed.ncbi.nlm.nih.gov/34004146/)

Medial ganglionic eminence (MGE)
{: .label .label-purple }

[![](/assets/images/yao_gab_MGE.jpg)](https://pubmed.ncbi.nlm.nih.gov/34004146/)

</div>

<div id="glutamatergic" class="tab" markdown="1">

{: .note-title }
> Note
>
> The **Glutamatergic** class contains the **L2/3 IT**, **L4/5/6 IT Car3**, **NP/CT/L6b**, and **PT** neighborhoods.

Layer 2/3 intratelencephalic neurons (L2/3 IT)
{: .label .label-green }

[![](/assets/images/yao_glu_L23.jpg)](https://pubmed.ncbi.nlm.nih.gov/34004146/)

Layer 4/5/6 intratelencephalic & Car3 neurons (L4/5/6 IT Car3)
{: .label .label-green }

[![](/assets/images/yao_glu_L23456.jpg)](https://pubmed.ncbi.nlm.nih.gov/34004146/)

Near-projecting/Corticothalamic/Layer 6b neurons (NP/CT/L6b)
{: .label .label-green }

[![](/assets/images/yao_glu_npctl6b.jpg)](https://pubmed.ncbi.nlm.nih.gov/34004146/)

Pyramidal tract neurons (PT)
{: .label .label-green }

[![](/assets/images/yao_glu_pt.jpg)](https://pubmed.ncbi.nlm.nih.gov/34004146/)

</div>

<div id="non-neuronal" class="tab" markdown="1">

{: .note-title }
> Note
>
> The **Non-Neuronal** class contains the **Astro**, **Epend**, **Immun**, **Oligo**, **OPC**, **Vascu** neighborhoods.

Astrocyte (Astro)
{: .label .label-red }

![](/assets/images/astro.jpg)

Ependymal cells (Epend)
{: .label .label-red }

TBD

Immune cells (Immun)
{: .label .label-red }

![](/assets/images/micro.jpg)

Oligodendrocyte (Oligo)
{: .label .label-red }

Oligodendrocyte precursor cells (OPC)
{: .label .label-red }

[![](/assets/images/olg_opc.jpg)](https://pubmed.ncbi.nlm.nih.gov/36001972/)
[![](/assets/images/olg_daos.jpg)](https://pubmed.ncbi.nlm.nih.gov/36001972/)

Vasculature cells (Vascu)
{: .label .label-red }

[![](/assets/images/yang_peri.png)](https://pubmed.ncbi.nlm.nih.gov/35165441/)
[![](/assets/images/yang_endo_peri.jpg)](https://pubmed.ncbi.nlm.nih.gov/35165441/)
[![](/assets/images/yang_fib.png)](https://pubmed.ncbi.nlm.nih.gov/35165441/)
[![](/assets/images/yang_vine.jpg)](https://pubmed.ncbi.nlm.nih.gov/35165441/)

</div>


### Gene set enrichment

In addition to looking at individual marker genes, we can also look at the set of top genes a cluster expresses and what terms are enriched from them to help shed some light on the identity of the cluster. [gprofiler2](https://biit.cs.ut.ee/gprofiler/gost) and [Enrichr](https://maayanlab.cloud/Enrichr/) are two tools that take a list of genes as input and outputs enriched terms from multiple sources. Among others, gProfiler outputs Gene Ontology terms, biological pathways, regulatory motifs of transcription factors, and Enrichr outputs various pathways, ontologies, diseases/drugs, and cell types.

### Low quality and dying cells

Something else to look out for are low quality or dying cells, which will be discarded after each round of annotation. Very low gene count and high mitochondrial fraction is a red flag for an artefact group. 

Dying cells will also often have very few unique genes. In addition, they may be [enriched](#gene-set-enrichment) for apoptosis, ubiquitination, and cell death, with some key markers being _Ubb_, _Cmss1_, _Cst3_, and _Hspa8_. You may see housekeeping genes _Actb_ and _Gadph_, signifying that the cell type specific genes for these clusters are not very specific. They will also show a lack of good marker genes or markers for multiple sets. While these could be disease relevant (more cells dying in one group versus another), you also cannot entirely rule out they are dying cells from the experimental preparation/treatment, or are cellular detritus from lysing cells ([SoupX](#sample-pre-processing) tries to help with this), or other experimental artifacts. Thus, since their chimeric nature messes with clustering, we set them aside for our annotations, and will look back at experimental group membership later (in which case a proper cell death assay may need to be run).

### Cluster consistency

Another thing to consider is the consistency of the cluster. We can visualize the cells of a cluster in the overall UMAP to determine its location in the bigger picture. This can help place the cluster in the context of the surrounding annotated cell types and give us a better idea of what the cluster is similar to.

Additionally, we can see how tightly or spread out the cells of the cluster is. If there is heavy spreading across the UMAP, the cluster can potentially be a chimeric cell type group, which will be discarded after each round of annotation. Chimeric clusters will have markers from multiple major groups, and the automated annotation will give inconsistent results.

### Further subclustering

At the subclass level, if the cluster continues to harbor chimeric contamination, deeper subclustering may be needed to remove the bad cells.
