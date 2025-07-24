---
layout: page
title: ISD Vignette 3
permalink: /isd-vig3/
---

# Step-by-step guide to reproduce the application X:

## SNPs in upstream IFNG regulators in Th1 cells favor upregulation of IFNG and drive resistance to dupilumab. 

### 1. Obtaining the genetic variant data

#### 1.1. Collecte genes harbouring variants (SNPs) associated with AD from the Open Targets database. First, access the [Open Targets Platform’s home page](https://platform.opentargets.org).

<img width="1808" height="874" alt="vig3_1" src="https://github.com/user-attachments/assets/ce132ffe-9ce6-484a-b8f6-d1566ab63597" />

#### 1.2. Then, use the Experimental Factor Ontology (EFO) identifier of AD (EFO_0000274) as query. As soon as you finish typing, "Atopic eczema" appears in the screen. Click over it.

<img width="1808" height="874" alt="vig3_2" src="https://github.com/user-attachments/assets/542881c3-f9fd-4de0-947c-4418af9e8556" />

#### 1.3. A page containing the retrieved results appears. Click "Export" and then "Download data"

<img width="1808" height="874" alt="vig3_3" src="https://github.com/user-attachments/assets/46623637-c248-414c-b0ba-0979b54872f4" />

#### 1.4. A new windows appears. Click "Advance Expert Options" and, in the field "Select association data type", select only "Genetic association"

<img width="1808" height="874" alt="vig3_4" src="https://github.com/user-attachments/assets/256fa0d3-6fa0-4474-9ca1-b2d69b52968e" />

#### 1.5. Finally, click "TSV" to download the file containing the AD-associated genes in a TSV format.

<img width="1816" height="875" alt="vig3_6" src="https://github.com/user-attachments/assets/4d21c01f-09fc-4519-b5b6-639ac0b152ce" />


### 2. Preparing the data-containing file for integration

#### 2.1. Open the downloaded TSV file in Excel or similar software. Copy the contents of column 1 (symbol) and paste them into a new spreadsheet. 

<img width="1323" height="744" alt="vig3_8" src="https://github.com/user-attachments/assets/bb6c175d-0a28-4208-853c-772df5d83808" />


#### 2.2. Create a header: name the column 1 as "identifier_hgnc_symbol" and for column 2 as "color". The list of genes should start in row 2.

<img width="1844" height="1021" alt="vig3_9" src="https://github.com/user-attachments/assets/bfb0d026-235c-4cbb-870a-fcde56fc7b66" />


#### 2.3. Fill out the rows in column "color" with a [hexadecimal code for your color of interest](https://www.w3schools.com/html/html_colors_hex.asp). Suggestion: #EB540. Save this file as "AD_genetic.tsv"

<img width="1844" height="1021" alt="vig3_10" src="https://github.com/user-attachments/assets/44b0d09f-79aa-4776-a46c-6c8007ed7d80" />






### 3. Access the map and login using your ORCID

To access the individual, i.e., AD or PsO, intercellular communication maps, please click on the button with disease name above each part of the diagram.  

 ![step2](https://github.com/user-attachments/assets/3187aaaf-da58-41f7-97dd-c51387d516e6)

Clicking on the “ATOPIC DERMATITIS” button, you will be directed to the AD map. 

![step3](https://github.com/user-attachments/assets/9d284197-04e1-47b4-a53a-b3a1498a4b8b)


### 4. Create an overlay for integration
You can explore the map by navigating it similarly as you do in Google Maps. Use the buttons on the lower right corner to zoom in, zoom out and center the map content.
 
![step4](https://github.com/user-attachments/assets/cc0e362b-a196-46b6-974b-640eb1ac9e63)


### 5. Integrating data into the map

Click the “Overlays” button to visualise i) genes harboring AD- or PsO-specific SNPs , ii) differentially expressed genes and proteins with their normalized log fold change (LFC) values and iii) AD- and PsO-linked biological processes discussed in the paper. The left panel will display the above-mentioned list. Click “View” to visualise an overlay of interest, e.g., the overlay “Omics: Differentially expressed proteins from dupilumab vs untreated lesional skin He et al (2020)”.

![step10](https://github.com/user-attachments/assets/46f2fd28-92d7-45d9-b457-837251327752)


After clicking “View”, the elements present in selected overlays containing datasets with differential expressed genes or proteins along with their normalized LFC values – in this case, for example, the overlay “Omics: Differentially expressed proteins from dupilumab vs untreated lesional skin He et al (2020)”, are highlighted in a gradient color according to their normalized LFC values as shown in the horizontal bar at the bottom of the panel “Overalys”. If you want to remove the highlights, click “Hide”.

 ![step11](https://github.com/user-attachments/assets/c95687ab-408b-4a56-8989-53f512340bf1)


If the selected overlay contains a dataset with gene symbols along with a fixed color, e.g., orange, as it happens for the overlay “Omics: Genes harboring AD-associated SNPs from Open Targets Genetics database”, you see, after clicking “View”, the corresponding genes highlighted in orange in this map. The color is shown in the horizontal bar at the bottom of “Overalys”. If you want to remove the highlights, click “Hide”.

![step12](https://github.com/user-attachments/assets/02627fea-4146-4378-987c-fdbcac221df1)

### Access the Th1 cells submap


### Check the positions of the highlighted proteins in relation to IFNG

