--- 
title: ISD 
layout: default 
permalink: /isd/
--- 

# The Inflammatory Skin Disease Map (ISD) pages  


## Technical information

**Development status:** Available for exploration online  
**Online access and exploration:** [https://imi-biomap.elixir-luxembourg.org](https://imi-biomap.elixir-luxembourg.org)  
**Disease IDs | Psoriasis:** [DOID:8893](https://disease-ontology.org/?id=DOID:8893), [MESH:D011565](https://id.nlm.nih.gov/mesh/D011565.html), [MONDO:0005083](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0005083)   
**Disease IDs | Atopic dermatitis:** [DOID:3310](https://disease-ontology.org/?id=DOID:3310), [MESH:D003876](https://www.ncbi.nlm.nih.gov/mesh/D003876), [MONDO:0004980](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0004980)  
**Sustainable support:** [LCSB](http://wwwen.uni.lu/lcsb), [MINERVA Platform](https://minerva.pages.uni.lu/)   
**Construction tool:** [CellDesigner](https://www.celldesigner.org/)  
**Funding:** [IMI2 BIOMAP No 821511](https://www.imi.europa.eu/projects-results/project-factsheets/biomap), [BIOMAP](https://biomap-imi.eu/)  
**License:** [Creative Commons Attribution 4.0 International (CC BY 4.0) License](https://creativecommons.org/licenses/by/4.0/)  
**Publication:** [Preprint](https://www.biorxiv.org/content/10.1101/2025.02.28.640747v1])  
**Contact:** Marcio Luis Acencio (marcio.acencio(at)gmail.com), Oxana Lopata (oxana.lopata(at)uni.lu) and Marek Ostaszewski(marek.ostaszewski(at).uni.lu), University of Luxembourg     


## Brief introduction  

The ISD map is a network of atopic dermatitis (AD)- and psoriasis (PsO)-specific causal molecular interactions represented as computable diagrams. It is available as a set of interactive diagrams, similar to canonical pathway databases, but focused on AD and PsO mechanisms. The ISD map can be used for data interpretation, hypothesis generation and simulation modelling. 


| Access the map | Learn how to navigate and explore the map |
| :---: | :---: |
|[![Access and explore the map](/images/projects/openinminerva1.png)](https://imi-biomap.elixir-luxembourg.org/)| [![Access and explore the map](/images/projects/quick1.jpeg)](/isd-guide/)|


## Structure of the ISD map

The map is comprised by three layers: a [side-by-side layer](https://imi-biomap.elixir-luxembourg.org/) that is the entry point for the ISD map and contains the key molecules and cells associated with AD and PsO, the intercellular communication views depicting how [AD](https://imi-biomap.elixir-luxembourg.org/minerva/index.html?id=ADmaps_10-02-2) and [PsO](https://imi-biomap.elixir-luxembourg.org/minerva/index.html?id=PsO_map)-relevant cell types interact, and the intracellular pathways layer illustrating signalling networks within some selected cells.  

### AD map

| Side-by-side layer | Intercellular communication layer | Intracellular pathways layer |
| :---: | :---: | :---: |
| [![](/images/projects/adtop500.png)](https://imi-biomap.elixir-luxembourg.org/minerva/index.html?id=ISD_entry_level&perfectMatch=true&modelId=400&backgroundId=626&x=3741&y=1170&z=5.334467744964014) | [![](/images/projects/adcell500.png)](https://imi-biomap.elixir-luxembourg.org/minerva/index.html?id=ADmaps_10-02-25&perfectMatch=false&modelId=384&backgroundId=610&x=2973&y=2480.4999999989786&z=4) | BLA |

### PsO map

| Side-by-side layer | Intercellular communication layer | Intracellular pathways layer |
| :---: | :---: | :---: |
|[![](/images/projects/psotop500.png)](https://imi-biomap.elixir-luxembourg.org/minerva/index.html?id=ISD_entry_level&perfectMatch=true&modelId=400&backgroundId=626&x=1242&y=1135&z=5.334467744964014) | [![](/images/projects/pso_cell_500.png)](https://imi-biomap.elixir-luxembourg.org/minerva/index.html?id=PsomapGlyphs3&perfectMatch=false&modelId=412&backgroundId=660&x=4118&y=7693&z=2.9547257721237843) | BLA |



## Applications of the ISD map

To demonstrate how the map can be used, we offer here some applications along with a step-by-step guide to reproduce the analysis:

<table border="1">
  <tr>
    <th>Application</th>
    <th>How to reproduce the analysis</th>
  </tr>
  <tr>
    <td> Analysis of the network structure </td>
  </tr>
   <tr>
    <td><a href="/isd-app-2/#bio" target="_blank"> Possible molecular mechanisms affected by candidate biomarkers for PsO systemic treatment response </a </td>
    <td>Step-by-step guide</td>
  </tr>
  <tr>
    <td><a href="/isd-app-2/#net" target="_blank">Discovering possible compensatory pathways explaining poor response to dupilumab</a></td>
    <td>Step-by-step guide</td>
  </tr>
  <tr>
    <td> Integration of genetic variation data into the map </td>
  </tr>
    <tr>
    <td><a href="/isd-app-2/#genet1" target="_blank">SNPs in upstream IFNG regulators in Th1 cells favor upregulation of IFNG and drive resistance to dupilumab</a></td>
    <td><a href="/isd-vig3" target="_blank">Step-by-step guide</a></td>
  </tr>
 <tr>
    <td><a href="/isd-app-2/#genet2" target="_blank"> SNPs in upstream apoptosis regulators in psoriatic KCs drive their resistance to cytokine-induced apoptosis.</a></td>
    <td>Step-by-step guide</td>
  </tr>
  <tr>
    <td> Integration of transcriptomics and proteomics data into the map </td>  
  </tr>
  <tr>
    <td><a href="/isd-app-2/#dup" target="_blank"> IFNG rescues the expression of dupilumab-downregulated proteins in AD </a></td>
    <td><a href="/isd-vig5" target="_blank">Step-by-step guide</a></td>
  </tr>
</table>

## Supplementary information

<table border="1">
  <tr>
    <th>Supplementary Information</th>
    <th>Description</th>
  </tr>
  <tr>
    <td> <a href="/isd-app1/" target="_blank"> The biology embedded in the map </a></td>
    <td> Brief description of AD- and PsO-related molecular mechanisms present in the map </td>
    </tr>
  <tr>
    <td> <a href="/isd-met/" target="_blank"> How was the map constructed?</a> </td>
    <td> Description of procedures and tools used to build the map </td>  
  </tr>
</table>



