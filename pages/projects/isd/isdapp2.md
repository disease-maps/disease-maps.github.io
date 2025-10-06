---
layout: default
title: ISD Application
permalink: /isdapp2/
---

# Applications of the ISD map

Here we demonstrate the ISD map can be a hypothesis-generating resource via the discovery of potential mechanistic downstream effects of selected AD- or PsO-related genes of interest. For this purpose, we either analysed the network structure of the map itself or analysed the outcomes of omics data integration into the map.

## Analysis of the network structure

<h2 id="net"></h2>

### Discovering possible compensatory pathways explaining poor response to dupilumab
*Step-by-step guide to reproduce the analysis here!*

The direct analysis of the network structure per se may provide biological insights related to a disease of interest. To find compensatory pathways that could explain poor response of dupilumab, a widely used IL4R antagonist to treat moderate-to-severe AD, we analysed the network structure of the AD submap at both intercellular communication ([AD main map](https://imi-biomap.elixir-luxembourg.org/minerva/index.html?id=ADmaps_10-02-25)) and intracellular ([KCs](https://imi-biomap.elixir-luxembourg.org/minerva/index.html?id=ADmaps_10-02-25&perfectMatch=false&modelId=386&backgroundId=610&x=5164&y=2665.785714285714&z=4)) and ([Th2 cells](https://imi-biomap.elixir-luxembourg.org/minerva/index.html?id=ADmaps_10-02-25&perfectMatch=false&modelId=387&backgroundId=610&x=2305.5&y=1687.8888888888887&z=4)) levels.
We could identify alternative pathways that explain, at least partially, the relatively low rate of remission following dupilumab treatment. In KCs, for instance, many genes involved in skin barrier homeostasis are downregulated not only by IL4/IL13 pathways, but also by IFNG, IL22, TSLP, IL-17A and IL25 signalling pathways. So, the presence of these cytokines in skin could compensate for the inhibitory action of dupilumab on IL4R.

<!-- ![kc_ad_hypo](https://github.com/user-attachments/assets/e3199474-0c0b-4fbd-986c-4d57d517c3f0) -->

![](../images/projects/isdimages/keratinocyte_dipulimab.png)


## Integration of genetic variation data into the map 
We integrated AD- and PsO-related genetic variation data (obtained from the Open Targets database) and, after analyzing the positions of the affected genes in the map, more specifically their encoded proteins, we could formulate the hypotheses shown below.

<h2 id="genet1"></h2>

### SNPs in upstream IFNG regulators in Th1 cells favor upregulation of IFNG and drive resistance to dupilumab.
[Step-by-step guide to reproduce the analysis here!](/isdvig3/)

We collected genes harbouring variants (SNPs) associated with AD from the Open Targets Genetics database and then mapped them to the ISD map ([see these genes (in orange) in the map](https://imi-biomap.elixir-luxembourg.org/minerva/index.html?id=ADmaps_10-02-25&perfectMatch=false&modelId=384&backgroundId=610&x=2820&y=1623&z=5&overlaysId=1367)). After integration of these AD-associated genes to the map, we sough to investigate their influence at the mechanistic level. To this end, we manually inspected the pathways of the ISD map for proteins encoded by the matched disease-associated genes that directly influence other proteins. As discussed previously, IFNG seems to partially compensate for IL4R inhibition by positively stimulating the expression of several AD-promoting genes stimulated by IL4R in KCs. As IFNG is mainly produced by Th1 cells, we checked the Th1 cell map for the presence of proteins encoded by AD-associated genes that could somehow influence IFNG expression. Interestingly, there are five proteins encoded by AD-associated genes (IL18RAP, IL18R1, TRAF6, CARD11 and NFKBIA) upstream to the IFNG expression. We hypothesise that SNPs in these genes could favour IFNG expression in Th1 cells and, therefore, counteract the action of dupilumab, i.e., IL4R inhibition. 



![ad_hypo_2](https://github.com/user-attachments/assets/0a2b962c-ea8a-42b7-85d2-286386ffa8de)

<h2 id="genet2"></h2>

### SNPs in upstream apoptosis regulators in psoriatic KCs drive their resistance to cytokine-induced apoptosis.
*Step-by-step guide to reproduce the analysis here!*

We collected genes harbouring variants (SNPs) associated with PsO from the Open Targets Genetics database and then mapped them to the ISD map ([see these genes (in green) in the map](https://imi-biomap.elixir-luxembourg.org/minerva/index.html?id=PsOmap&perfectMatch=false&modelId=432&backgroundId=674&x=4131&y=5323&z=4.639352169813215&overlaysId=1462)). After integration of these PsO-associated genes to the map, we sough to investigate their influence at the mechanistic level, specifically in psoriatic KCs. In PsO, KCs are relatively resistant to cytokine-induced apoptosis. This resistance could be assigned, at least partially, to the presence of several proteins encoded by PsO-associated genes in apoptosis-regulating pathways. In fact, by exploring the map, we can see at least six proteins encoded by PsO-associated genes in these pathways: IFNG, INFGR2, TNFRSF1A, ESRRA, IRF1 and SOCS1. The most prominent pathway would be the one triggered by IFNG via IFNGR2 and IRF1 culminating in the expression of SOCS proteins. Remarkably, all proteins in this apoptosis-regulating pathway are encoded by PsO-associated genes and the underlying SNPs could favour the inhibition of apoptosis in KC (see figure below). 


![pso_hypo](https://github.com/user-attachments/assets/2af14268-39b2-4595-8d5c-5cb3496fcf5e)


The above examples show that, through the integration of Open Target Genetics data with ISD map, we could determine the contextual relevance for AD- and PsO-associated genes and check if they fit into the existing molecular and cellular understanding of AD and PsO. Moreover, we were also able to formulate two hypotheses: resistance to dupilumab due to enhanced expression of IFNG in Th1 cells favoured by SNPs in upstream IFNG regulators and resistance to cytokine-induced apoptosis in psoriatic KCs due to altered upstream apoptosis regulators. The figure below depicts these hypotheses.


![pso_ad_ot](https://github.com/user-attachments/assets/1dc9ebf3-dc5b-4d50-a371-c43096fbd8da)




## Integration of transcriptomics and proteomics data into the map
We integrated AD- and PsO-related omics data (obtained from biomedical literature and Gene Expression Omnibus database) and, after analyzing the positions of the differentially expressed genes and proteins in the map, we could formulate the hypotheses shown below.

<h2 id="dup"></h2>


### IL26 rescues the expression of TSLP, CCL20 and IL33 in AD keratinocytes under dupilumab treatment
[Step-by-step guide to reproduce the analysis here!](/isdvig5/)

We collected differentially expressed proteins (DEPs) from the study by [He et al. (2020)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2020.01768/full) in which proteome expression profiles were measured in AD lesional and non-lesional stratum corneum samples taken from patients before and after treatment with dupilumab. From this study, we considered only DEPs calculated by comparing expression profiles of 353 inflammatory proteins extracted from lesional stratum corneum samples of patients before and after dupilumab exposure. Of the 132 dupilumab-induced differentially expressed inflammatory proteins (Dup-DEIPs), 20 could be found in the AD map ([see these proteins in the map here](https://imi-biomap.elixir-luxembourg.org/minerva/index.html?id=ADmaps_10-02-25&perfectMatch=false&modelId=384&backgroundId=610&x=2373&y=2225&z=4.123391479177037&overlaysId=1365)).

We sought to check the KCs intracellular activity for finding which and how these Dup-DEIPs are distributed in KCs intracellular pathways. Of the 34 inflammatory proteins in KCs, nine (IL1RL1, IL17RA, IKBKB, CASP3, CASP8, CXCL8, CCL17, TNF and MMP9) are Dup-DEIPs, all being downregulated by dupilumab. We first checked which of these Dup-DEIPs are regulated by IL4/IL13 signalling. Of these nine proteins, only CXCL8 is a IL4/IL13 target and, as expected, it is downregulated. While CXCL8 is downregulated by dupilumab, the expression of TSLP, another IL4/IL13-induced inflammatory protein, seems not to be affected; TSLP is also regulated by IFNG signalling according to the map, so the TSLP expression could be rescued by IFNG in the absence of an active IL4R. IL17RA is downregulated by dupilumab and, therefore, we would also expect a downregulation of IL17RA signalling inflammatory target proteins. However, the DEP data provide no evidence that either of its inflammatory targets in KCs, namely CCL20, CSF3 and IL33, are affected by dupilumab. Among these proteins, it is possible to see that IL33, as TSLP, is also regulated by IFNG. So, IL33 expression could also be rescued by IFNG. 




