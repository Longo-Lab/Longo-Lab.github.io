#!/usr/bin/env python3
"""Build cell_types_v2.json for the snRNAseq annotation tutorial dendrogram.

The figure renders the Allen Institute whole mouse brain taxonomy
(CCN20230722, Yao et al. 2023) as neighborhood -> class. Subclass is
deliberately not a level here: there are 339 of them, which cannot be
labelled legibly in a radial layout at any width that fits the page.
Subclass detail lives in overall.name_schema.csv and wmb_dot() instead.

Inputs (copy down from SCG):
  /labs/flongo/reference/single-cell/overall.name_schema.csv
  /labs/flongo/reference/single-cell/allen_brain_atlas/wmb_gene_table.csv.gz

Usage:
  python3 generate_cell_types_v2.py <schema_csv> <gene_table_csv_gz> <out_json>
"""

import csv
import gzip
import json
import sys
from collections import Counter, OrderedDict

# Teaching order from the lab's annotation lectures, with the colour assigned
# to each neighbourhood. These same colours become the leaf ramp, so classes
# shade by the neighbourhood they sit in.
NEIGHBORHOODS = OrderedDict([
    ("Pallium-Glut", ("Pallium, glutamatergic", "#1f6f3f")),
    ("Subpallium-GABA", ("Subpallium, GABAergic", "#7e57a2")),
    ("HY-EA-Glut-GABA", ("Hypothalamus & extended amygdala", "#c8952e")),
    ("TH-EPI-Glut", ("Thalamus & epithalamus, glutamatergic", "#2f7fa8")),
    ("MB-HB-Glut-Sero-Dopa", ("Midbrain & hindbrain, Glut/Sero/Dopa", "#3aa39a")),
    ("MB-HB-CB-GABA", ("Midbrain, hindbrain & cerebellum, GABAergic", "#b1040e")),
    ("NN-IMN-GC", ("Non-neuronal, immature neurons & granule cells", "#c8703e")),
])

# How many aggregated marker genes to show per class on hover.
N_MARKERS = 6


def load_rows(schema_csv):
    with open(schema_csv, newline="") as fh:
        rows = list(csv.DictReader(fh))
    # Artifact rows are annotation labels, not real taxonomy - they are
    # documented in the artifacts table on the page, not in the figure.
    return [r for r in rows if r["neighborhood"] != "Artifact"]


def load_subclass_markers(gene_table):
    """subclass label -> ordered list of 'overall' marker genes."""
    markers = {}
    with gzip.open(gene_table, "rt", newline="") as fh:
        for r in csv.DictReader(fh):
            if r["tier"] == "subclass" and r["label"] == "overall":
                markers.setdefault(r["type"], []).append(r["gene"])
    return markers


def class_markers(subclasses, sub_markers):
    """The gene table has no class tier, so aggregate up from subclasses:
    rank genes by how many of the class's subclasses carry them."""
    counts = Counter()
    for sc in subclasses:
        for gene in sub_markers.get(sc, []):
            counts[gene] += 1
    # Ties broken alphabetically so output is deterministic.
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return ", ".join(g for g, _ in ranked[:N_MARKERS])


def class_sort_key(label):
    """'01 IT-ET Glut' -> (1, '01 IT-ET Glut'); keeps 06a next to 06."""
    head = label.split(" ", 1)[0]
    digits = "".join(c for c in head if c.isdigit())
    return (int(digits) if digits else 999, head, label)


def build(schema_csv, gene_table, out_json):
    rows = load_rows(schema_csv)
    sub_markers = load_subclass_markers(gene_table)

    # A subclass may list two neighbourhoods (they are not strictly
    # hierarchical); the first is the primary one. Class -> primary
    # neighbourhood is 1:1, which is what makes this tree well formed.
    tree = {n: {} for n in NEIGHBORHOODS}
    for r in rows:
        nb = r["neighborhood"].split(";")[0]
        if nb not in tree:
            raise SystemExit("unexpected neighborhood: %r" % nb)
        tree[nb].setdefault(r["class_id_label"], set()).add(r["subclass_id_label"])

    children = []
    for nb, (full_name, color) in NEIGHBORHOODS.items():
        classes = []
        for cls in sorted(tree[nb], key=class_sort_key):
            node = {"name": cls}
            markers = class_markers(tree[nb][cls], sub_markers)
            if markers:
                node["markers"] = markers
            classes.append(node)
        children.append({
            "name": nb,
            "full_name": full_name,
            "color": color,
            "children": classes,
        })

    data = {
        "name": "root",
        "levels": ["neighborhood", "class"],
        # Class labels run to ~15 characters, so this needs a bigger canvas
        # and a much deeper label margin than the v1.0 taxonomy did.
        "size": 860,
        "margin": 155,
        "ramp": [c for _, c in NEIGHBORHOODS.values()],
        "children": children,
    }

    with open(out_json, "w") as fh:
        json.dump(data, fh, indent=2)
        fh.write("\n")

    n_cls = sum(len(c["children"]) for c in children)
    print("wrote %s: %d neighborhoods, %d classes"
          % (out_json, len(children), n_cls))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    build(*sys.argv[1:])
