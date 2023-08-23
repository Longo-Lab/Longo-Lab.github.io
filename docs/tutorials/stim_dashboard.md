---
layout: stim
title: Stimulation dashboard
parent: Tutorials
nav_order: 2
---

# Stimulation dashboard
{: .no_toc }

For our [projects](/docs/projects) that applied theta-burst stimulation (TBS) treatment, we include a link to a **Stimulation dashboard**. This page provides a tutorial on how to navigate the dashboard and interpret the results.

{: .info-title }
> Try it out
>
> Open a stimulation dashboard to follow along the tutorial.

If you haven't already, review the [**DE dashboard** tutorial](de_dashboard.html) first, as it covers many of the shared methods and topics.

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

## Genes table

At the bottom half of the dashboard, under the <span class="tab-name">Genes list</span> tab, there is a table of genes used in the analysis. The <span class="tab-name">Summary table</span> tab contains summary and meta data. See the [DE dashboard](de_dashboard.html#genes-table) for more information about the genes table.

### Stimulation analysis

**Long-term potentiation (LTP)** is defined as the persistent strengthening of synapses following high-frequency stimulation. It is particularly important for learning and memory, thus often studied using hippocampal slices of the brain.

Our projects use TBS treatment in attempt to induce LTP activity. It is found that TBS can successfully induce LTP in _wildtype vehicle (WtV)_ and _drug-treated transgenic (TgD)_ mice, but not _transgenic vehicle (TgV)_ mice. This suggests that the drugs help to restore the ability to maintain LTP.

The figure below summarizes the effects of TBS:

<img src="/assets/images/stim-analysis.png" style="border:1px solid #dfdfdf;border-radius:0.25rem;" />

### Categorization

To determine which genes are relevant to inducing LTP activity, we can compare the stimulation effect of each gene in the transgenic vehicle mice (which did not induce LTP) to its effect in the wildtype vehicle mice (which successfully induced LTP). Genes whose log fold change (LFC) differ between the two groups are interesting, as we want to identify genes whose expression becomes more up or down-regulated as a result of LTP.

To visualize this, we can plot the LFC for stimulation effect in WtV mice on the x-axis against the difference in LFC between TgV and WtV on the y-axis. This allows us to define the following 4 categories of genes corresponding to each of the 4 quadrants. Use the animation below to explore how this is derived.

- **LTP-dependent gain**:
  - <span style="color:#7f8538;">Up in WtV and down in TgV</span>
  - <span style="color:#b1cf5f;">Up in WtV and also up in TgV but to a lesser extent</span>
- **LTP-dependent loss**:
  - <span style="color:#b34342;">Down in WtV and up in TgV</span>
  - <span style="color:#f59d9e;">Down in WtV and also down in TgV but to a lesser extent</span>
- **Shared gain**:
  - <span style="color:#f4b940;">Up in WtV and also up in TgV but to a greater extent</span>
- **Shared loss**:
  - <span style="color:#5ea4a1;">Down in WtV and also down in TgV but to a greater extent</span>

<div id="main">
  <div id="plot"></div>
  <div id="menu">
    <a class="btn btn-primary" data-value="tgv">WtV vs. TgV</a>
    <a class="btn btn-secondary" data-value="tgv_wtv">WtV vs. (TgV - WtV)</a>
  </div>
</div>

As seen above, the dashed line at `y = x` in the WtV vs. TgV plot represents cases where the gene LFC would be equal in both groups. The activity-dependent genes can be defined as genes that deviate away from that line, specifically ones that have a greater effect in the WtV group than TgV group.

The same comparison can be done between the transgenic vehicle mice (which did not induce LTP) and drug-treated transgenic mice (which successfully restored LTP), as seen in the <span class="tab-name">L2FC correlation</span> tabs [below](#l2fc-correlation-plot).

To determine the gene categories, the genes are first filtered using a LFC threshold and significance threshold (p-adj < 0.05), where genes are either significant in the WtV and TgD (LTP) groups or TgV (no LTP) group. See the <span class="tab-name">Summary table</span> tab for the specific LFC threshold used and whether the shrunken or unshrunken LFC is used.

## Analysis results

The main analysis results are located in the top half of the dashboard. A short description of each type of result and how to interpret them can be found below.

### Modules enrichment plot

The first 5 tabs (<span class="tab-name">Treat-AD</span>, <span class="tab-name">Tmt-AD</span>, <span class="tab-name">Mostafavi, et al.</span>, <span class="tab-name">Milind, et al.</span>, <span class="tab-name">Wan, et al.</span>) show the Fisher's exact enrichment of each of the [modules](de_dashboard.html#modules) with our DE dataset.

Each column in the plot is a module and each row is a subset of genes in our dataset, as defined by being up or down in stimulation effect in the wildtype vehicle, transgenic vehicle, and drug-treated transgenic mice. The same LFC and significance thresholds used for determining our [gene categories](#categorization) are applied here (see <span class="tab-name">Summary table</span> tab). See the [DE dashboard](de_dashboard.html#modules-enrichment-plot) for more information about the plot and how to interpret it.

### TREAT-AD correlation plot

The <span class="tab-name">Treat-AD correlation</span> tab shows the correlation between human AD expression data and our DE dataset for each TREAT-AD biodomain. See the [DE dashboard](de_dashboard.html#treat-ad-correlation-plot) for more information about the plot and how to interpret it.

### L2FC correlation plot

The <span class="tab-name">L2FC correlation</span> tabs show the correlation between the stimulation effect in various groups in our DE dataset. Either the shrunken or unshrunken LFC for each gene is plotted, and only genes meeting the LFC criteria are included in the plot, as specified in the <span class="tab-name">Summary table</span> tab. Further, if unshrunken LFC is used, an additional significance filter (p-adj < 0.05) is applied to exclude potential noise.

Each point in the plot represents a gene. The LFC for stimulation effect in WtV (or TgD) is plotted on the x-axis and LFC for stimulation effect in TgV - WtV (or TgV - TgD) is plotted on the y-axis. The correlation coefficient and corresponding p-value are shown at the bottom left of the plot. Review the [gene categorizations](#categorization) for more information on how to interpret the plot.

### gProfiler results

The next 4 tabs show the [gProfiler](https://biit.cs.ut.ee/gprofiler/gost) enrichment results in both graphical and tabular format, separately for each of the 4 [gene categorizations](#categorization). The number of genes in each category can be seen in the <span class="tab-name">Summary table</span> tab. See the [DE dashboard](de_dashboard.html#gprofiler-results) for more information about the gProfiler results and how to interpret them.

### GO terms enrichment plot

The <span class="tab-name">GO terms enrichment</span> tabs show the top 20 up and down-regulated GO terms in each experimental group, separately for the _Biological Process (BP)_, _Molecular Function (MF)_, and _Cellular Component (CC)_ subdivisions of Gene Ontology.

The same LFC and significance thresholds used for determining our [gene categories](#categorization) are applied here (see <span class="tab-name">Summary table</span> tab).
