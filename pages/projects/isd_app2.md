---
layout: page
title: ISD Application
permalink: /isd-app-2/
---

# Applications of the ISD map

Here we demonstrate the ISD map can be a hypothesis-generating resource via the discovery of potential mechanistic downstream effects of selected AD- or PsO-related genes of interest. For this purpose, we either analysed the network structure of the map itself or analysed the outcomes of omics data integration into the map.

## Analysis of the network structure

<h2 id="net"></h2>

### Discovering possible compensatory pathways explaining poor response to dupilumab
The direct analysis of the network structure per se may provide biological insights related to a disease of interest. To find compensatory pathways that could explain poor response of dupilumab, a widely used IL4R antagonist to treat moderate-to-severe AD, we analysed the network structure of the AD submap at both intercellular communication and intracellular (KCs and Th2 cells) levels.
We could identify alternative pathways that explain, at least partially, the relatively low rate of remission following dupilumab treatment. In KCs, for instance, many genes involved in skin barrier homeostasis are downregulated not only by IL4/IL13 pathways, but also by IFNG, IL22, TSLP, IL-17A and IL25 signalling pathways. So, the presence of these cytokines in skin could compensate for the inhibitory action of dupilumab on IL4R.

![kc_ad_hypo](https://github.com/user-attachments/assets/e3199474-0c0b-4fbd-986c-4d57d517c3f0)

## Integration of genetic variation data into the map 


<h2 id="genet1"></h2>

### Could SNPs in upstream IFNG regulators in Th1 cells favor upregulation of IFNG and drive resistance to dupilumab?
We collected genes harbouring variants (SNPs) associated with AD from the Open Targets Genetics database and then mapped them to the ISD map ([see these genes (in orange) in the map](https://imi-biomap.elixir-luxembourg.org/minerva/index.html?id=ADmaps_10-02-25&perfectMatch=false&modelId=384&backgroundId=610&x=2820&y=1623&z=5&overlaysId=1367)). After integration of these AD-associated genes to the map, we sough to investigate their influence at the mechanistic level. To this end, we manually inspected the pathways of the ISD map for proteins encoded by the matched disease-associated genes that directly influence other proteins. As discussed previously, IFNG seems to partially compensate for IL4R inhibition by positively stimulating the expression of several AD-promoting genes stimulated by IL4R in KCs. As IFNG is mainly produced by Th1 cells, we checked the Th1 cell map for the presence of proteins encoded by AD-associated genes that could somehow influence IFNG expression. Interestingly, there are five proteins encoded by AD-associated genes (IL18RAP, IL18R1, TRAF6, CARD11 and NFKBIA) upstream to the IFNG expression. We hypothesise that SNPs in these genes could favour IFNG expression in Th1 cells and, therefore, counteract the action of dupilumab, i.e., IL4R inhibition. 



![ad_hypo_2](https://github.com/user-attachments/assets/0a2b962c-ea8a-42b7-85d2-286386ffa8de)

<h2 id="genet2"></h2>

## Could SNPs in upstream apoptosis regulators in psoriatic KCs drive their resistance to cytokine-induced apoptosis?.
We collected genes harbouring variants (SNPs) associated with PsO from the Open Targets Genetics database and then mapped them to the ISD map ([see these genes (in green) in the map](https://imi-biomap.elixir-luxembourg.org/minerva/index.html?id=PsO_map&perfectMatch=false&modelId=389&backgroundId=612&x=6509&y=1929&z=5.242334845066072&overlaysId=1369)). After integration of these PsO-associated genes to the map, we sough to investigate their influence at the mechanistic level, specifically in psoriatic KCs. In PsO, KCs are relatively resistant to cytokine-induced apoptosis. This resistance could be assigned, at least partially, to the presence of several proteins encoded by PsO-associated genes in apoptosis-regulating pathways. In fact, by exploring the map, we can see at least six proteins encoded by PsO-associated genes in these pathways: IFNG, INFGR2, TNFRSF1A, ESRRA, IRF1 and SOCS1. The most prominent pathway would be the one triggered by IFNG via IFNGR2 and IRF1 culminating in the expression of SOCS proteins. Remarkably, all proteins in this apoptosis-regulating pathway are encoded by PsO-associated genes and the underlying SNPs could favour the inhibition of apoptosis in KC (see figure below). 


![pso_hypo](https://github.com/user-attachments/assets/2af14268-39b2-4595-8d5c-5cb3496fcf5e)


The above examples show that, through the integration of Open Target Genetics data with ISD map, we could determine the contextual relevance for AD- and PsO-associated genes and check if they fit into the existing molecular and cellular understanding of AD and PsO. Moreover, we were also able to formulate two hypotheses: resistance to dupilumab due to enhanced expression of IFNG in Th1 cells favoured by SNPs in upstream IFNG regulators and resistance to cytokine-induced apoptosis in psoriatic KCs due to altered upstream apoptosis regulators. The figure below depicts these hypotheses.


![pso_ad_ot](https://github.com/user-attachments/assets/1dc9ebf3-dc5b-4d50-a371-c43096fbd8da)




## Integration of transcriptomics and proteomics data into the map
To show that the ISD map can be useful for supporting the discovery of potential AD- and PsO-related molecular mechanisms affected by genes or proteins that are prioritised via omics studies, we show here four use cases: (i) Integration of AD-associated genes from the Open Targets Genetics database (16) with the AD map, (ii) integration of PsO-associated genes from the Open Targets Genetics database with the PsO map, (iii) integration of differentially expressed proteins (DEPs) from protein expression profiles with the AD map and (iv) integration of differentially expressed genes (DEGs) from gene expression profiles with the PsO map.	



## Suggesting mechanistic consequences of altered gene and protein expression profiles
We collected differentially expressed proteins (DEPs) from the study by He et al. (2020) (18) in which proteome expression profiles were measured in AD lesional and non-lesional stratum corneum samples taken from patients before and after treatment with dupilumab. From this study, we considered only DEPs calculated by comparing expression profiles of 353 inflammatory proteins extracted from lesional stratum corneum samples of patients before and after dupilumab exposure. Of the 132 dupilumab-induced differentially expressed inflammatory proteins (Dup-DEIPs), 20 could be found in the AD map (see these proteins in the map here). First, we performed an enrichment analysis to check if any intra- or intercellular activity was enriched in Dup-DEIPs in lesional stratum corneum. Only the intercellular activity of KCs (adjusted p-value = 0.0003) is significantly enriched in Dup-DEIPs. This is rather expected as stratum corneum is comprised virtually only by KCs. But, intriguingly, the intracellular activity of KCs is not significantly enriched; this can be explained by the fact that He and colleagues considered only a panel of inflammatory proteins for measuring expression; the intracellular pathways of KCs in the AD map contain 145 proteins and only 34 of them are classified as inflammatory. 

Despite this limitation, we sought to check the KCs intracellular activity for finding which and how these Dup-DEIPs are distributed in KCs intracellular pathways. Of the 34 inflammatory proteins in KCs, nine (IL1RL1, IL17RA, IKBKB, CASP3, CASP8, CXCL8, CCL17, TNF and MMP9) are Dup-DEIPs, all being downregulated by dupilumab. We first checked which of these Dup-DEIPs are regulated by IL4/IL13 signalling. Of these nine proteins, only CXCL8 is a IL4/IL13 target and, as expected, it is downregulated. While CXCL8 is downregulated by dupilumab, the expression of TSLP, another IL4/IL13-induced inflammatory protein, seems not to be affected; TSLP is also regulated by IFNG signalling according to the map, so the TSLP expression could be rescued by IFNG in the absence of an active IL4R. IL17RA is downregulated by dupilumab and, therefore, we would also expect a downregulation of IL17RA signalling inflammatory target proteins. However, the DEP data provide no evidence that either of its inflammatory targets in KCs, namely CCL20, CSF3 and IL33, are affected by dupilumab. This suggests alternative pathways — such as IFNG for IL33, IL26 for CCL20 and an unknown pathway for CSF3 — that rescue the expression of these proteins. Finally, it is possible to realize that, via this integration with proteomic data, molecular connections between IL4R and the above-mentioned Dup-DEIPs — except for CXCL8 — are still missing in the AD map. This can be due to either AD knowledge not yet captured by biocurators or a real knowledge gap concerning such connections.

We collected DEGs from a meta-analysis derived (MAD) transcriptome of psoriasis comparing lesional and non-lesional skin samples published by Tian et al. in 2012 (19). From this study, we integrated into the map differentially expressed genes (DEGs) belonging to the set built by combining the results of five microarray data sets (MAD5) where the transcriptome profiles of lesional and non-lesional psoriatic skins were compared. Of 1116 DEGs, 63 mapped to proteins in the PsO map (see these genes in the map here). By performing an enrichment analysis to check which intra- or intercellular activity are enriched in DEGs, we found that both inter- (adjusted p-value < 0.0001) and intracellular activities of KC (adjusted p-value < 0.0001) are enriched in DEGs, as well as intercellular activity of neutrophils (adjusted p-value = 0.0003). These findings are not surprising and serve the purpose of reinforcing the vital roles these cells play for psoriasis progression. The significant enrichment in melanocyte activity (adjusted p-value = 0.0410) and the lack of enrichment in Th17 cell activity are more surprising. While Abdel-Naser et al. (2016) showed that lesional psoriatic skin has an increased activity and number of epidermal melanocytes, the number of Th17 cells might not be different between non-lesional and lesional skin (20). This may at first appear inconsistent with the experimental evidence that IL17A is upregulated in lesional skin, but by inspecting the PsO map we can observe that IL17A is also produced by neutrophils, ILC3 cells, gamma-delta T cells, mast cells and Tc17 cells in addition to Th17 cells. As IL17A positively influences KC expression of mainly inflammatory proteins, we sought to verify whether IL17A downstream signalling and target proteins in KCs were also upregulated. Indeed, some of the IL17A downstream signalling proteins, e.g., STAT1 and STAT3, and target proteins, e.g., S100A8, CXCL1 and CXCL8, are upregulated. Interestingly, MALT1 and CARD14, signalling proteins that boost the NFKB signalling pathway — a pathway that is an important drive for IL17A signalling — are also upregulated (Figure 3B).

The above examples show that, through the integration of omics data with ISD map, we could (1) formulate hypotheses, i.e., IFNG rescues expression of dupilumab-downregulated proteins, and (2) identify gaps in the map or even in the AD-related knowledge itself that warrants further experimental investigation.
