---
title: Disease Maps Course
layout: default
permalink: /markopolo/course/
---

# MARKOPOLO Disease Maps Course

An intensive two-week workshop on the <a href="https://disease-maps.io/" target="_blank">Disease Maps</a> concept and <a href="https://sbgn.github.io/" target="_blank">Systems Biology Graphical Notation (SBGN)</a>, organised at the <a href="https://www.lih.lu/en/research-scope/research-department/department-of-cancer-research/multiomics-data-science/" target="_blank">Luxembourg Institute of Health (LIH)</a> within the EU-funded <a href="https://markersofpollution-markopolo.eu/" target="_blank">MARKOPOLO</a> project.

## Course content

**Part 1. SBGN diagrams**  
Learning the SBGN Process Description and Activity Flow languages by redrawing example diagrams in CellDesigner and yEd Graph Editor. Deliverables: diagram files in xml and graphml formats.

**Part 2. Disease map development**  
Study-a-thon dedicated to the ExposomeMap-PM project. Deliverables: pathways for extending the ExposomeMap-PM, brief textual descriptions with supporting references.

## Software

<a href="https://www.celldesigner.org/" target="_blank">CellDesigner</a>, an editor developed by the Systems Biology Institute for building process diagrams and computational models, one of the most widely used tools for this type of diagramming. It has the best compatibility with the MINERVA Platform and is used as the main tool within this course.

<a href="https://www.yworks.com/products/yed" target="_blank">yEd Graph Editor</a>, freely available software developed by yWorks. A dedicated SBGN palette is available <a href="https://doi.org/10.1093/bib/bby099" target="_blank">(Siebenhaller et al, 2020)</a>. Intuitive for drawing diagrams. Additionally, the experience of drawing in yEd is transferable and can be used for creating any type of diagrams for publications.

<a href="https://newteditor.org/" target="_blank">Newt Editor</a>, a web-based tool developed for SBGN diagrams <a href="https://doi.org/10.1093/bioinformatics/btaa850" target="_blank">(Balci et al, 2021)</a>. It has automatic layout algorithms, advanced complexity management, conversion to and from CellDesigner and many other features. No installation required.

## Example 1. Glycolysis regulation via bifunctional enzyme

A brief tutorial on drawing the glycolysis regulation diagram in CellDesigner.

<iframe width="640" height="360" src="https://www.youtube.com/embed/I0B3QE3Njzs" frameborder="0" allowfullscreen></iframe>

<br>

This 5-min video demonstrates how to draw the glycolysis regulation example diagram in CellDesingner step by step. The original diagram is available at the <a href="https://metabolismregulation.github.io/" target="_blank">Metabolism Regulation Atlas</a>. 

<img src="/pages/projects/markopolo/images/glycolysis-yed.png" alt="glycolysis-cd" width="600"/>

**Figure 1.** The glycolysis regulation diagram drawn in yEd Graph Editor.

<br>

<img src="/pages/projects/markopolo/images/glycolysis-cd.png" alt="glycolysis-cd" width="600"/>

**Figure 2.** The glycolysis regulation diagram drawn in CellDesigner.

<br>


## Example 2. iNOS pathway

<img src="/pages/projects/markopolo/images/inos-yed.png" alt="inos-yed"/>

**Figure 3.** The iNOS pathway drawn in yEd Graph Editor.

<br>

<img src="/pages/projects/markopolo/images/inos-cd.png" alt="inos-cd"/>

**Figure 4.** The iNOS pathway drawn in CellDesigner.

<br>

## Activity Flow vs. Process Description

<img src="/pages/projects/markopolo/images/guide-fig2.jpg" alt="guide-fig2"/>

**Figure 5.** An example that compares two representations in CellDesigner that correspond to Activity Flow (Reduced Notation palette in CellDesigner) and Process Description (default palette in CellDesigner). The two diagrams represent the same biological events but in two conceptually different languages. **(A).** The Process Description representation of the RAF-MEK-ERK signalling: the process of MEK1/2 phosphorylation is catalysed by RAF1 and the process of ERK1/2 phosphorylation is catalysed by the phosphorylated MEK1/2. **(B).** The Activity Flow representation of the RAF-MEK-ERK signalling: the activity of RAF1 stimulates the activity of MEK1/2 (MAP2K1 and MAP2K2 in official HGNC names), and the activity of MEK1/2 stimulates the activity of ERK1/2 (MAPK3 and MAPK1 in official HGNC names) <a href="https://doi.org/10.3389/fbinf.2023.1197310" target="_blank">(Mazein et al, 2023)</a>.

## Resources

<a href="https://disease-maps.io/guidelines/" target="_blank">Disease maps development guide</a>

<a href="https://doi.org/10.3389/fbinf.2023.1197310" target="_blank">Guidelines paper</a>

<a href="https://sbgn.github.io/learning" target="_blank">SBGN learning</a>

<a href="https://sbgn.github.io/learnerscards" target="_blank">SBGN learner's reference cards</a>

<a href="https://sbgnbricks.github.io/pd/" target="_blank">SBGN Bricks</a>

<a href="https://sbgn.github.io/specifications" target="_blank">SBGN PD specification</a>

<a href="https://metabolismregulation.github.io/gallery/" target="_blank">Metabolism Regulation Atlas</a>

<a href="https://disease-maps.io/sbgnincd/" target="_blank">Drawing SBGN PD in CellDesigner</a>
