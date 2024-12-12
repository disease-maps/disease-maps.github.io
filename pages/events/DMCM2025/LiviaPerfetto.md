---
title: DMCM2025 Programme
layout: default
permalink: /DMCM2025/LiviaPerfetto/
---

<img src="/images/places/DMCM2025.png"/>

[[back to the DMCM2025 Programme]](https://disease-maps.github.io/DMCM2025/programme/)

<table>
  <tr>
    <td style="width: 140px;">
      <img src="/images/teamhq/LiviaPerfetto.png" width="135"/></td>
    <td> 
      <a href="https://sites.google.com/view/perfettolab/home?authuser=0" target="_blank"><b>Livia Perfetto</b></a>, Professor at Universita degli Studi di Roma La Sapienza, Dipartimento di Biologia e Biotecnologie Charles Darwin: Roma, Lazio, Italy.
    </td>
  </tr> 
</table>

### About 

"My background is on Cellular and molecular Biology; however I’ve always been a self-taught bioinformatician. I obtained my PhD at the University of Rome “Tor Vergata” in 2014, working in Prof. Cesareni’s group, my PhD thesis focused on strategies to exploit scientific data curation to interpret biological processes (Mining and integrating literature information). I continued to work in Cesareni Lab for three more years, where I coordinated the development of SIGNOR, a new resource to support experimental investigation of signalling networks. In 2017 I moved to EBI, where I was a database curator in IntAct and Complex Portal databases. In November 2020 I started a new position as bioinformatician and database curator funded by the Human Technopole (Milan) in the framework of a collaboration with the department of Biology at the University of Rome “Tor Vergata”. In 2022 I became group leader and assistant Professor at La Sapienza University in Rome. The group I coordinate is characterized by interdisciplinarity and is made up by the strong cross-talk between a database and a bioinformatics unit. The database unit is devoted to the development, the curation and the maintenance of the SIGNOR database, whereas the main area of interest of the bioinformatics unit consists in set up of algorithms and computational pipelines that use the existing knowledge annotated in SIGNOR to support the interpretation and the contextualization of -omic data."

### Toward *PatientProfiler*, a network-based approach to support personalized medicine

Deciphering the intricate mechanisms underlying reprogramming in cancer cells is a crucial challenge in oncology as it holds the key to advancing our ability to diagnose and treat cancer patients. For this reason, comprehensive and patient-specific multi-omic characterization of tumor specimens has become increasingly common in clinical practice. Despite these efforts, no effective approach for identifying the molecular mechanisms dysregulated at patient-resolution level has been developed, nor have these advances been effectively employed to define personalized therapeutic regimens. The main shortcoming is the absence of a robust computational framework to exploit such information by integrating and interpreting the available multi-dimensional data to drive translational solutions.

To fill this gap, we developed *PatientProfiler*, a computational pipeline that leverages causal interaction data, annotated in our in-house manually-curated resource, SIGNOR, to address how the genetic and molecular background of individual patients contributes to the establishment of a malignant phenotype. *PatientProfiler* is an open-source, R-based package composed of several functions that allow for multi-omic data analysis and standardization, generation of patient-specific mechanistic models of signal transduction, and extraction of network-based prognostic biomarkers.

To benchmark the tool, we retrieved genomic, transcriptomic, (phospho)proteomic and clinical data derived from 122 treatment-naïve breast cancer biopsies, available at the CPTAC portal. Thanks to this approach, we have identified patient-specific mechanistic models (one patient, one network) that recapitulate dysregulated signaling pathways in breast cancer. This collection of models provides valuable insights into the underlying mechanisms of tumorigenesis and disease progression. Moreover, in depth topological exploration of these networks has allowed us to define seven communities (subnetworks), each associated with a unique transcriptomic signature and a distinct prognostic value.

In summary, our work demonstrates that *PatientProfiler* is a tool for patient-specific network analysis, advancing personalized medicine by identifying actionable biomarkers and supporting tailored therapeutic strategies. CopyRetryClaude does not have the ability to run the code it generates yet.




