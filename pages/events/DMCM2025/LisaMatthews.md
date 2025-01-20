---
title: DMCM2025 Programme
layout: default
permalink: /DMCM2025/LisaMatthews/
---

<img src="/images/places/DMCM2025.png"/>

[[back to the DMCM2025 Programme]](https://disease-maps.github.io/DMCM2025/programme/)

<table>
  <tr>
    <td style="width: 140px;">
      <img src="/images/teamhq/LisaMatthews.png" width="135"/></td>
    <td> 
      <a href="https://reactome.org/about/team" target="_blank"><b>Lisa Matthews</b></a>, Managing Editor of Reactome, NYU Grossman School of Medicine, New York, United States of America.
    </td>
  </tr> 
</table>

### About 

"I earned my Ph.D. in Genetics at Cornell University in the lab of Dr. Ken Kempheus, where my research focused on early embryonic development in Caenorhabditis elegans. I completed postdoctoral training in the lab of Dr. Marc Vidal at Harvard Medical School and the Dana-Farber Cancer Institute, where I identified and characterized conserved protein interaction networks in Saccharomyces cerevisiae and C. elegans. In 2000, I joined the bioinformatics team at Proteome, an early commercial human and model organism protein databases. In 2003, I transitioned to the role of scientific curator at Reactome under Dr. Lincoln Stein at Cold Spring Harbor Laboratory. For the past 15 years, I have served as the managing editor of Reactome at the NYU Grossman School of Medicine.
"

### Leveraging Large Language Models for Enhanced Biocuration and User Interaction in Reactome: A Pathway Towards Community-Driven Knowledge Enrichment

Authors: Lisa Matthews (1), Deidre Beavers (2), Helia Mohammadi (3,9), Adam Wright (3), Marija Milacic (3), Patrick Conley (2), Chuqiao Gong (4), Marc Gillespie (3,6), Johannes Griss (4,5), Robin Haw (3), Bijay Jassal (3,10), Nancy T Li (3), Bruce May (3), Robert Petryszak (2), Eliot Ragueneau (4), Karen Rothfels (3), Cristoffer Sevilla (4), Veronica Shamovsky (1), Ralf Stephan (3,7), Krishna Tiwari (4), Thawfeek Varusai (4,8), Joel Weiser (3), Henning Hermjakob (4), Peter D’Eustachio (1), Guanming Wu (2), Lincoln Stein (3,9)


Affiliations:
1 NYU Grossman School of Medicine, New York, NY 10016, USA
2 Oregon Health and Science University, Portland, OR 97239, USA
3 Ontario Institute for Cancer Research, Toronto, ON M5G0A3, Canada
4 European Molecular Biology Laboratory, European Bioinformatics Institute (EMBL-EBI), Wellcome Genome Campus, Hinxton, Cambridgeshire CB10 1SD, UK
5 Department of Dermatology, Medical University of Vienna, 1090 Vienna, Austria
6 College of Pharmacy and Health Sciences, St. John’s University, Queens, NY 11439, USA
7 Institute for Globally Distributed Open Research and Education (IGDORE)
8 Open Targets, Wellcome Genome Campus, Hinxton, Cambridgeshire CB10 1SD, UK
9 Department of Molecular Genetics, University of Toronto, Toronto, ON M5S 1A1, Canada
10 AstraZeneca PLC, 1 Francis Crick Ave, Cambridge Biomedical Campus, Cambridge CB2 0AA, UK

Reactome is the most comprehensive open-source repository of human biological pathways and has been recognized as both an ELIXIR and Global Core Biodata Resource. While its primary focus is normal human cellular processes, Reactome also encompasses infectious disease pathways and disease processes associated with genetic variations. Additionally, it extends its high-quality, manually curated human pathways to key model organisms through orthology-based projections.

While manual curation is the gold standard approach for ensuring accurate and reliable pathway annotation, scaling this process to accommodate the rapidly growing volume of scientific literature poses substantial resource and workflow challenges. To address these challenges, we are developing novel tools and automated procedures aimed at streamlining the curation process and accelerating data integration.

One key initiative is the design of a web-based curation tool that incorporates Large Language Models (LLMs)-based AI technologies, guided by Reactome’s data schema and curation requirements, to significantly facilitate steps that are major bottlenecks for the curation workflow. We have adopted retrieval-augmented generation (RAG) technology and developed a robust workflow that curates un-annotated genes into existing Reactome pathways. Leveraging our prior work with the NIH IDG program, the workflow can identify potential pathways for a query gene, search PubMed for supportive literature evidence, create text summaries based on collected PubMed abstracts and Reactome pathway annotation using LLM, and extract functional relationships between the query gene and biological concepts from the full text PDF papers as potential curation materials. This LLM-based workflow will be combined with improved orthology-based methods and applied in viral curation to rapidly generate prototype host-pathogen interface pathways for representative species of key pathogen classes.

Reactome has also developed a conversational chatbot that facilitates user interactions toward improving the accessibility and comprehension of Reactome content. The chatbot is designed to provide a natural, interactive user experience and more intuitive navigation through Reactome's extensive database. Through this interface, users can query complex pathway information and receive rich, informative responses that encourage deeper engagement with the knowledgebase. Future endeavors involve integrating LLMs into the chatbot for data analysis, empowering users with diverse technical backgrounds to perform sophisticated analyses using Reactome's tools. Integration of multi-source data retrieval systems and the incorporation of gene analysis tools are expected to enhance the platform's utility and interactivity, thereby streamlining the user experience and facilitating the exploration and understanding of complex biological datasets. Our LLM-integrated approaches will improve user engagement and lay the groundwork for improved curation workflows, potentially offering a means for community curation practices