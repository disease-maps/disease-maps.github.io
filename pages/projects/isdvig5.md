---
title: ISD Vignette 5
layout: default
permalink: /isdvig5/
---

# Step-by-step guide to reproduce the application *"IL26 rescues the expression of TSLP and CCL20 in AD keratinocytes under dupilumab treatment"*


### 1. Obtaining the protein expression data

1.1. Download the protein expression data from the [Supplementary Table E2](https://www.frontiersin.org/api/v4/articles/565656/file/Data_Sheet_1.XLSX/565656_supplementary-materials_datasheets_1_xlsx/1) accompanying the study by [He et al 2020](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2020.0176jaiza rodrigues gonçalves botucatu8/full); in this study, inflammatory proteome expression profiles (based on a panel of pre-selected 353 inflammatory proteins) were measured via Olink proteomic assay in AD lesional and non-lesional skin samples taken from non-chronic patients before and after treatment with dupilumab.  


1.2. Collect only columns containing expression profiles data from lesional skin samples of patients after versus before dupilumab exposure. For this purpose, copy the columns A (Protein), H (“FCH LS Post-Rx versus Pre-Rx”) and J (“FDR LS Post-Rx versus Pre-Rx”) to a new sheet.

<!-- <img width="892" height="561" alt="image" src="https://github.com/user-attachments/assets/7c2a3907-7ffe-4796-bd10-9123c37bd651" /> -->

![vig3_1](https://github.com/user-attachments/assets/7c2a3907-7ffe-4796-bd10-9123c37bd651)

#### 1.3. Create two sheets, one containing all tested proteins (control) and another containing only differentially-expressed proteins (DEPs), i.e. with FDR < 0.05 and fold-change (FCH) > 1.5. 

##### 1.3.1. For the sheet containing all proteins, keep only the first column. Save this file as "AD_proteome_control.txt"

<!-- <img width="945" height="529" alt="image" src="https://github.com/user-attachments/assets/523620e7-1d69-4756-894d-bd308c1b158a" /> -->

![vig3_1](https://github.com/user-attachments/assets/523620e7-1d69-4756-894d-bd308c1b158a)


##### 1.3.2. In the other sheet, keep only the DEPs (FDR < 0.05 and FCH > 1.5, following authors' own criteria). Then remove the column "FDR LS Post-Rx versus Pre-Rx" and rename column "FCH LS Post-Rx versus Pre-Rx" to "value". Save the file as "AD_proteome.tsv". 

<!-- <img width="883" height="566" alt="image" src="https://github.com/user-attachments/assets/bdef2529-98a2-4333-98a3-ec59865dc7bc" /> -->

![vig3_1](https://github.com/user-attachments/assets/bdef2529-98a2-4333-98a3-ec59865dc7bc)



### 2. Preparing the data-containing files for integration

#### 2.1. Open the file "AD_proteome_control.tsv". Replace "Protein" with "identifier_hgnc_symbol" in column 1 and then add a new column named "color". Fill rows in column "color" with a [hex color code for your color of interest](https://www.color-hex.com/color/). Suggestion: #2986cc (blue). Save it as "AD_proteome_control.txt". This file is ready to be uploaded to the map.

<!-- <img width="938" height="533" alt="image" src="https://github.com/user-attachments/assets/0c13c6bf-2739-42ba-9b86-59d36fcc2fdb" /> -->

![vig3_1](https://github.com/user-attachments/assets/0c13c6bf-2739-42ba-9b86-59d36fcc2fdb)


#### 2.2. Open the file ""AD_proteome.tsv". Normalize FCH values to the [-1,1] range by truncating the FCH value to a maximum and minimum of, respectively, 3 and -3. Use your prefered method to do that, but, if you prefer, we offer you here a Python-based normalizer script that will create the normalized version of data ([Download it here](/pages/projects/minerva_normalize.zip)) as well as the file ready to be uploaded in the map.

##### 2.2.1. Install Python 3 in your operational system (Latest stable version for the latest versions of operation systems: [Windows](https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe) or [MacOS](https://www.python.org/ftp/python/3.13.5/python-3.13.5-macos11.pkg)). 
##### 2.2.2. After downloading the above zip file, unzip it in your local computer in your folder of preference. You see a python file named "minerva_normalize.py"
##### 2.2.3. In Windows, just double-click the file; in Linux, right-click it and select "Run as a program". In MacOS, open the Terminal, go to the folder where the python file is located and type "python3 minerva_normalize.py".
##### 2.2.4. Regardless of the system, a small window equal or similar to the pictureb below will appear. Click "Select file to Normalize" and select the file "AD_proteome.tsv"

<!-- <img width="552" height="279" alt="image" src="https://github.com/user-attachments/assets/ea276913-a4bf-4528-b01f-dfbd938adc20" /> -->

![vig3_1](https://github.com/user-attachments/assets/ea276913-a4bf-4528-b01f-dfbd938adc20)

##### 2.2.5. If successfull, the file "AD_proteome_normalized.txt", which is ready to be uploaded to the map, is generated.

<!-- <img width="415" height="211" alt="image" src="https://github.com/user-attachments/assets/5aa31bd2-865f-45d7-81c8-8f33f1315eb5" /> -->

![vig3_1](https://github.com/user-attachments/assets/5aa31bd2-865f-45d7-81c8-8f33f1315eb5)


### 3. Access and log in to the map

#### 3.1. Access the ISD map at the entry level via the link https://imi-biomap.elixir-luxembourg.org/. In the map, click the login icon in the left upper side of the screen. This is required to integrate data into the map.
 
<!-- <img width="1022" height="489" alt="image" src="https://github.com/user-attachments/assets/94b53f4d-7c65-4502-8b46-dbd53c658676" /> -->

![vig3_1](https://github.com/user-attachments/assets/94b53f4d-7c65-4502-8b46-dbd53c658676)


#### 3.2. Log in to the map preferentially by using your ORCID. 

<!-- <img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/acc57fb8-0e6f-485e-9921-8ccb3098994c" /> -->

![vig3_1](https://github.com/user-attachments/assets/acc57fb8-0e6f-485e-9921-8ccb3098994c)

#### 3.3. Once connected, just ignore the window "Select project" by clicking "X".

<!-- <img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/a6d4d362-b76b-42e1-a7d8-e5c627247c9e" /> -->

![vig3_1](https://github.com/user-attachments/assets/a6d4d362-b76b-42e1-a7d8-e5c627247c9e)

#### 3.4. Click the button "ATOPIC DERMATITIS" to go the AD intercellular communication map 

<!-- <img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/ee910213-6ec4-42f9-923c-0068bfe6e4df" /> -->

![vig3_1](https://github.com/user-attachments/assets/ee910213-6ec4-42f9-923c-0068bfe6e4df)


### 4. Create the overlays for integration

#### 4.1. The integration of data into the map is done via overlay creation. For this purpose, click the button "+ Overlays" above the intercellular communication map 

<!-- <img width="1017" height="491" alt="image" src="https://github.com/user-attachments/assets/a799d1a3-e138-4a29-b7c2-370be02b2386" /> -->

![vig3_1](https://github.com/user-attachments/assets/a799d1a3-e138-4a29-b7c2-370be02b2386)


#### 4.2. When the panel "Overlays" opens in the left part of the screen, go straight to the bottom and click "Add overlay" 

<!-- <img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/4bad673d-76fd-4398-a4d9-27e17bedff37" /> -->

![vig3_1](https://github.com/user-attachments/assets/4bad673d-76fd-4398-a4d9-27e17bedff37)

#### 4.3. In the panel "Add overlay", click "browse" to upload the file "AD_proteome_normalized.txt".

<!-- <img width="1019" height="491" alt="image" src="https://github.com/user-attachments/assets/9c48cccf-b9ce-4404-b18d-27e6c6f4826e" /> -->

![vig3_1](https://github.com/user-attachments/assets/9c48cccf-b9ce-4404-b18d-27e6c6f4826e)

#### 4.4. When you observe "AD_proteome_normalized.txt" instead of "browse", provide a name in the field "Name" (e.g., "AD proteome"). Go to the botton and click "Upload"

<!-- <img width="1018" height="491" alt="image" src="https://github.com/user-attachments/assets/9ac28fed-fbe3-467c-9826-864689f933b9" /> -->

![vig3_1](https://github.com/user-attachments/assets/9ac28fed-fbe3-467c-9826-864689f933b9)


#### 4.5. If you are successful, then you see the warning "User overlay added successfully". 

<!-- <img width="1017" height="491" alt="image" src="https://github.com/user-attachments/assets/d0a1a048-2306-4430-91f4-cdb12056b349" /> -->

![vig3_1](https://github.com/user-attachments/assets/d0a1a048-2306-4430-91f4-cdb12056b349)


#### 4.6. Create now an overlay for the AD proteome control following steps 4.1 to 4.4. Upload the file "AD_proteome_control.txt" and as overlay name "AD_proteome_control". If you are successful, then you see the warning "User overlay added successfully". 

<!-- <img width="1018" height="491" alt="image" src="https://github.com/user-attachments/assets/0222939d-b941-4ae7-842e-2054ddfa2ab0" /> -->

![vig3_1](https://github.com/user-attachments/assets/0222939d-b941-4ae7-842e-2054ddfa2ab0)



### 5. Integrating and exploring the data into the map

#### 5.1. Access DEPs, i.e., the overlay "AD proteome", and the tested proteins, i.e. the overlay "AD_proteome_control", matching the map via the panel "Overlays". Go to the botton and click "Without group". The overlay "AD proteome" and "AD_proteome_control", as well as other already existent overlays, appear. Click "View" in both overlays.

<!-- <img width="1021" height="490" alt="image" src="https://github.com/user-attachments/assets/cf7960ce-a60e-4ec8-a495-8c18b6dc2115" /> -->

![vig3_1](https://github.com/user-attachments/assets/cf7960ce-a60e-4ec8-a495-8c18b6dc2115)



#### 5.2. Tested proteins unaffected by dupilumab are painted only in blue (right half) and DEPs are painted in blue (right half) and in red-blue gradient (left half). In this gradient, the reder, the lower the FCH value and, the bluer, the higher the FCH value. Proteins in the map not considered in the original study keep the original color. 

<!-- <img width="1018" height="491" alt="image" src="https://github.com/user-attachments/assets/eaea7206-0f77-468c-87e1-e71386c25a3d" /> -->

![vig3_1](https://github.com/user-attachments/assets/eaea7206-0f77-468c-87e1-e71386c25a3d)


#### 5.3. In this particular application, we want to check which inflammatory proteins in KC are affected or unaffected by dupilumab. So, go to “Submaps” and then click “>” associated with the submap “Keratinocyte”.

<!-- <img width="1021" height="490" alt="image" src="https://github.com/user-attachments/assets/4f50970b-3cd3-466c-8e60-e5d536af3336" /> -->

![vig3_1](https://github.com/user-attachments/assets/4f50970b-3cd3-466c-8e60-e5d536af3336)


#### 5.4. A new tab ("Keratinocyte") showing the intracellular pathways of KC appears. Click the magnifier icon until the point you are able to see at least which proteins are painted. By navigating the map, it is possible to see some unaffected (right half in blue) and affected (right half in blue and left half in red-blue gradient) proteins, such as the nine secreted ones shown in the figure below. 

<!-- <img width="1849" height="500" alt="image" src="https://github.com/user-attachments/assets/a9b1fe12-2857-46c8-8aea-133eadae7106" /> -->

![vig3_1](https://github.com/user-attachments/assets/a9b1fe12-2857-46c8-8aea-133eadae7106)


#### 5.5. To check which unaffected proteins and DEPs are directly regulated by the dupilumab target, i.e., IL4/IL13 signaling pathway, click the connections pointing to the proteins. In the left side of the map, a panel showing information about the target gene/protein, including the source of the selected connection (in this case, "IL4/IL13 induced regulation of gene expression"), appears. Among our proteins of interest, only CXCL8 and TSLP are directly regulated by IL4/IL13 pathway; however, only CXCL8 is underexpressed while TSLP is unaffected.

<!-- <img width="963" height="519" alt="image" src="https://github.com/user-attachments/assets/4a4226bb-7956-4983-8642-b62ea60d4274" /> -->

![vig3_1](https://github.com/user-attachments/assets/4a4226bb-7956-4983-8642-b62ea60d4274)

#### 5.6. To check possible mechanisms involved in the unaltered TSLP expression, check the other connections pointing to CXCL8 and TSLP and discover their sources. While CXCL8 is also regulated by IFNG and IL26 signaling pathways, TSLP is additionally regulated by IL26, but not IFNG. This suggests that, for TSLP, IL26 signaling could compensate for the lack of IL4/IL13 signaling.



#### 5.7. IL17RA is also downregulated by dupilumab (A). By following the downstream connections, you reach the phenotype "IL17 induced regulation of gene expression" (B). From there, continue downstream until find some unaffected proteins or DEPs (B). You find six unaffected proteins: CCL20, IL33, CXCL9, CXCL10, CXCL11 and CSF3.

<!-- <img width="1000" height="485" alt="image" src="https://github.com/user-attachments/assets/6bd50fd7-454c-4b81-b58e-9b5d7a75f81d" /> -->

![vig3_1](https://github.com/user-attachments/assets/6bd50fd7-454c-4b81-b58e-9b5d7a75f81d)

<!-- <img width="1000" height="370" alt="image" src="https://github.com/user-attachments/assets/0e367f87-6b68-4512-9b27-c75f8aa0aa3b" /> -->

![vig3_1](https://github.com/user-attachments/assets/0e367f87-6b68-4512-9b27-c75f8aa0aa3b)

#### 5.8. Among the six unnafected proteins, only two - CCL20 and IL33 - are additionally regulated by other signaling pathways: IL26 for CCL20 and IL26 and IFNG for IL33. This suggests that IL26 signaling could compensate for the dupilumab-downregulated IL17 signaling pathway.




### 6. Hypothesis



