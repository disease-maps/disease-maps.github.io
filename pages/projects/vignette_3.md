---
layout: page
title: ISD Vignette 3
permalink: /isd-vig3/
---

# Step-by-step guide to reproduce the applications

<h2 id="genetic1"></h2>

## SNPs in upstream IFNG regulators in Th1 cells favor upregulation of IFNG and drive resistance to dupilumab. 

### 1. Obtaining the genetic variant data

#### 1.1. Collect genes harbouring variants (SNPs) associated with AD from the Open Targets database. First, access the [Open Targets Platform’s home page](https://platform.opentargets.org).

<img width="1808" height="874" alt="vig3_1" src="https://github.com/user-attachments/assets/ce132ffe-9ce6-484a-b8f6-d1566ab63597" />

#### 1.2. Then, use the Experimental Factor Ontology (EFO) identifier of AD (EFO_0000274) as query. As soon as you finish typing, "Atopic eczema" appears in the screen. Click it.

<img width="1808" height="874" alt="vig3_2" src="https://github.com/user-attachments/assets/542881c3-f9fd-4de0-947c-4418af9e8556" />

#### 1.3. A page containing the retrieved results appears. Go to "Columns options" and selected the following sources of genetic data: GWAS associations, ClinVar and Uniprot Curated Variants

<img width="1851" height="958" alt="image" src="https://github.com/user-attachments/assets/8372cfe6-96a8-40ab-8da6-2ee988badaf2" />


#### 1.4. Click "Export" and then "Download data"

<img width="1808" height="874" alt="vig3_3" src="https://github.com/user-attachments/assets/46623637-c248-414c-b0ba-0979b54872f4" />

#### 1.5. A new windows appears. Click "Advance Expert Options" and, in the field "Select association data type", select only "Genetic association"

<img width="1808" height="874" alt="vig3_4" src="https://github.com/user-attachments/assets/256fa0d3-6fa0-4474-9ca1-b2d69b52968e" />

#### 1.6. Finally, click "TSV" to download the file containing the AD-associated genes in a TSV format. Make sure that the option "Include custom controls" is selected.

<img width="1851" height="958" alt="image" src="https://github.com/user-attachments/assets/914e7e8c-811e-4b9c-94e9-ce26104f4675" />


### 2. Preparing the data-containing file for integration

#### 2.1. Open the downloaded TSV file in Excel or similar software. Copy the contents of column 1 (symbol) and paste them into a new spreadsheet. 

<img width="899" height="556" alt="image" src="https://github.com/user-attachments/assets/ab9de500-1588-4ee6-9512-07fae0dbf615" />



#### 2.2. Create a header: name the column 1 as "identifier_hgnc_symbol" and for column 2 as "color". The list of genes should start in row 2.

<img width="1852" height="999" alt="image" src="https://github.com/user-attachments/assets/0b2ea923-6801-46f8-b4b4-3a45c798cba2" />


#### 2.3. Fill rows in column "color" with a [hex color code for your color of interest](https://www.color-hex.com/color/). Suggestion: #f6b26b (orange). Save this file as "AD_genetic.txt"

<img width="1850" height="970" alt="image" src="https://github.com/user-attachments/assets/960a366e-f290-4801-9482-ab118c898a1e" />



### 3. Access and log in to the map

#### 3.1. Access the ISD map at the entry level via the link https://imi-biomap.elixir-luxembourg.org/. In the map, click the login icon in the left upper side of the screen. This is required to integrate data into the map.
 
<img width="1022" height="489" alt="image" src="https://github.com/user-attachments/assets/94b53f4d-7c65-4502-8b46-dbd53c658676" />


#### 3.2. Log in to the map preferentially by using your ORCID. 

<img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/acc57fb8-0e6f-485e-9921-8ccb3098994c" />

#### 3.3. Once connected, just ignore the window "Select project" by clicking "X".

<img width="1849" height="890" alt="image" src="https://github.com/user-attachments/assets/a6d4d362-b76b-42e1-a7d8-e5c627247c9e" />

#### 3.4. Click the button "ATOPIC DERMATITIS" to go the AD intercellular communication map 

<img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/ee910213-6ec4-42f9-923c-0068bfe6e4df" />


### 4. Create the overlay for integration

#### 4.1. The integration of data into the map is done via overlay creation. For this purpose, click the button "+ Overlays" above the intercellular communication map 

<img width="1017" height="491" alt="image" src="https://github.com/user-attachments/assets/a799d1a3-e138-4a29-b7c2-370be02b2386" />


#### 4.2. When the panel "Overlays" opens in the left part of the screen, go straight to the bottom and click "Add overlay" 

<img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/4bad673d-76fd-4398-a4d9-27e17bedff37" />

#### 4.3. In the panel "Add overlay", click "browse" to upload the file "AD_genetic.tsv".

<img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/9c48cccf-b9ce-4404-b18d-27e6c6f4826e" />


### 5. Integrating data into the map

Click the “Overlays” button to visualise i) genes harboring AD- or PsO-specific SNPs , ii) differentially expressed genes and proteins with their normalized log fold change (LFC) values and iii) AD- and PsO-linked biological processes discussed in the paper. The left panel will display the above-mentioned list. Click “View” to visualise an overlay of interest, e.g., the overlay “Omics: Differentially expressed proteins from dupilumab vs untreated lesional skin He et al (2020)”.

![step10](https://github.com/user-attachments/assets/46f2fd28-92d7-45d9-b457-837251327752)


After clicking “View”, the elements present in selected overlays containing datasets with differential expressed genes or proteins along with their normalized LFC values – in this case, for example, the overlay “Omics: Differentially expressed proteins from dupilumab vs untreated lesional skin He et al (2020)”, are highlighted in a gradient color according to their normalized LFC values as shown in the horizontal bar at the bottom of the panel “Overalys”. If you want to remove the highlights, click “Hide”.

 ![step11](https://github.com/user-attachments/assets/c95687ab-408b-4a56-8989-53f512340bf1)


If the selected overlay contains a dataset with gene symbols along with a fixed color, e.g., orange, as it happens for the overlay “Omics: Genes harboring AD-associated SNPs from Open Targets Genetics database”, you see, after clicking “View”, the corresponding genes highlighted in orange in this map. The color is shown in the horizontal bar at the bottom of “Overalys”. If you want to remove the highlights, click “Hide”.

![step12](https://github.com/user-attachments/assets/02627fea-4146-4378-987c-fdbcac221df1)

### Access the Th1 cells submap


### Check the positions of the highlighted proteins in relation to IFNG

