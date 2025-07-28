---
layout: page
title: ISD Vignette 5
permalink: /isd-vig5/
---

# Step-by-step guide to reproduce the application *"IFNG rescues the expression of dupilumab-downregulated proteins in AD	"*


### 1. Obtaining the protein expression data

#### 1.1. Download the protein expression data from the [Supplementary Table E2](https://www.frontiersin.org/api/v4/articles/565656/file/Data_Sheet_1.XLSX/565656_supplementary-materials_datasheets_1_xlsx/1) accompanying the study by [He et al 2020](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2020.01768/full); in this study, inflammatory proteome expression profiles (based on a panel of pre-selected 353 inflammatory proteins) were measured via Olink proteomic assay in AD lesional and non-lesional skin samples taken from patients before and after treatment with dupilumab.  



#### 1.2. Collect only differentially expressed proteins (DEPs) calculated by comparing expression profiles extracted from lesional skin samples of patients before and after dupilumab exposure. For this purpose, copy the columns A (HGNC symbol of the proteins), H (“FCH LS Post-Rx versus Pre-Rx”) and J (“FDR LS Post-Rx versus Pre-Rx”) to a new sheet.

<img width="892" height="561" alt="image" src="https://github.com/user-attachments/assets/7c2a3907-7ffe-4796-bd10-9123c37bd651" />


#### 1.3. In the new sheet, keep only DEPs with FDR < 0.05 and fold-change (FCH) > 1.5 (following authors' own criteria). Then remove the column "FDR LS Post-Rx versus Pre-Rx". Save the file as "AD_proteome.tsv". 

<img width="890" height="562" alt="image" src="https://github.com/user-attachments/assets/f6f9262c-ba8b-44c3-976b-2360c3bd0cf7" />



### 2. Preparing the data-containing file for integration

#### 2.1. Normalize FCH values to the [-1,1] range by truncating the FCH value to a maximum and minimum of, respectively, 3 and -3. Use your prefered method to do that, but, if you prefer, we offer you here a Python-based normalizer that will create the normalized version of data ([Download here](/pages/projects/minerva_normalize.zip)) as well as the file ready to be uploaded in the map.

##### 2.1.1. Install Python 3 in your operational system (Latest stable version for the latest versions of operation systems: [Windows](https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe) or [MacOS](https://www.python.org/ftp/python/3.13.5/python-3.13.5-macos11.pkg)). 
##### 2.1.2. After downloading the above zip file, unzip it in your local computer in your fold of preference. You see a python file named "minerva_normalize.py"
##### 2.1.3. In Windows, just double-click the file; in Linux, right-click it and select "Run as a program". In MacOS, open the Terminal, go to the folder where the python file is located and type "python3 minerva_normalize.py".
##### 2.1.4. Regardless of the system, a small window equal or similar to the pictureb below will appear. Click "Select file to Normalize" and select the file "AD_proteome.tsv"

<img width="552" height="279" alt="image" src="https://github.com/user-attachments/assets/ea276913-a4bf-4528-b01f-dfbd938adc20" />

##### 2.1.5. If successfull, the file "AD_proteome_normalized.txt", which is ready to be uploaded to the map, is generated.

<img width="415" height="211" alt="image" src="https://github.com/user-attachments/assets/5aa31bd2-865f-45d7-81c8-8f33f1315eb5" />


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

#### 4.3. In the panel "Add overlay", click "browse" to upload the file "AD_proteome.txt".

<img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/9c48cccf-b9ce-4404-b18d-27e6c6f4826e" />

#### 4.4. When you observe "AD_proteome.txt" instead of "browse", provide a name in the field "Name" (e.g., "AD proteome"). Go to the botton and click "Upload"


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

