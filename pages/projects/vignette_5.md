---
layout: page
title: ISD Vignette 5
permalink: /isd-vig5/
---

# Step-by-step guide to reproduce the application *"IFNG rescues the expression of dupilumab-downregulated proteins in AD	"*


### 1. Obtaining the protein expression data

#### 1.1. Collect genes harbouring variants (SNPs) associated with AD from the Open Targets database. First, access the [Open Targets Platform’s home page](https://platform.opentargets.org).


#### 1.2. Then, use the Experimental Factor Ontology (EFO) identifier of AD (EFO_0000274) as query. As soon as you finish typing, "Atopic eczema" appears in the screen. Click it.


#### 1.3. A page containing the retrieved results appears. Go to "Columns options" and selected the following sources of genetic data: GWAS associations, ClinVar and Uniprot Curated Variants



#### 1.4. Click "Export" and then "Download data"


#### 1.5. A new windows appears. Click "Advance Expert Options" and, in the field "Select association data type", select only "Genetic association"


#### 1.6. Finally, click "TSV" to download the file containing the AD-associated genes in a TSV format. Make sure that the option "Include custom controls" is selected.



### 2. Preparing the data-containing file for integration

#### 2.1. Open the downloaded TSV file in Excel or similar software. Copy the contents of column 1 (symbol) and paste them into a new spreadsheet. 




#### 2.2. Create a header: name the column 1 as "identifier_hgnc_symbol" and for column 2 as "color". The list of genes should start in row 2.



#### 2.3. Fill rows in column "color" with a [hex color code for your color of interest](https://www.color-hex.com/color/). Suggestion: #f6b26b (orange). Save this file as "AD_genetic.txt"




### 3. Access and log in to the map

#### 3.1. Access the ISD map at the entry level via the link https://imi-biomap.elixir-luxembourg.org/. In the map, click the login icon in the left upper side of the screen. This is required to integrate data into the map.
 
<img width="1022" height="489" alt="image" src="https://github.com/user-attachments/assets/94b53f4d-7c65-4502-8b46-dbd53c658676" />


#### 3.2. Log in to the map preferentially by using your ORCID. 

<img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/acc57fb8-0e6f-485e-9921-8ccb3098994c" />

#### 3.3. Once connected, just ignore the window "Select project" by clicking "X".

<img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/a6d4d362-b76b-42e1-a7d8-e5c627247c9e" />

#### 3.4. Click the button "ATOPIC DERMATITIS" to go the AD intercellular communication map 

<img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/ee910213-6ec4-42f9-923c-0068bfe6e4df" />


### 4. Create the overlay for integration

#### 4.1. The integration of data into the map is done via overlay creation. For this purpose, click the button "+ Overlays" above the intercellular communication map 

<img width="1017" height="491" alt="image" src="https://github.com/user-attachments/assets/a799d1a3-e138-4a29-b7c2-370be02b2386" />


#### 4.2. When the panel "Overlays" opens in the left part of the screen, go straight to the bottom and click "Add overlay" 

<img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/4bad673d-76fd-4398-a4d9-27e17bedff37" />

#### 4.3. In the panel "Add overlay", click "browse" to upload the file "AD_proteome.tsv".

<img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/9c48cccf-b9ce-4404-b18d-27e6c6f4826e" />

#### 4.4. When you observe "AD_proteome.tsv" instead of "browse", provide a name in the field "Name" (e.g., "AD proteome"). Go to the botton and click "Upload"


#### 4.5. When you observe the warning "User overlay added successfully", click "<" close to "Add overlays" to go back to the "Overlay" panel and initiate the explorations as shown in next steps.


### 5. Integrating and exploring the data into the map

#### 5.1. Access the dupilumab-induced differentially expressed AD skin inflammatory proteome data, i.e., the overlay "AD proteome", via the panel "Overlays". Go to the botton and click "Without group". The overlay "AD proteome" and other already existent overlays appear.


#### 5.2. Click "View" and the dupilumab-induced differentially expressed AD skin inflammatory proteins mapped to the map will be painted in COLOR. 


#### 5.3. In this particular application, we want to check the KCs intracellular activity for finding which and how these dupilumab-induced differentially expressed inflammatory proteins are distributed in KCs intracellular pathways. Go to “Submaps” and then click “>” associated with the submap “Keratinocyte”.



#### 5.4. A new tab ("Keratinocyte") showing the intracellular pathways of KC appears. It is possible to see some proteins painted in COLOR. To take a further look at them, click the magnifier icon until the point you are able to read the gene symbols in the elements.



  #### 5.5. By navigating the map at the zoom level of your convenience, you can see that there are XXX.


#### 5.6. XXX

### 6. Hypothesis

XXX. 

