---
title: ISD Vignette 6
layout: default
permalink: /isdvig6/
---

# Boolean network and simulation

We used Probabilistic Boolean Modelling (PBM) to simulate the effects of IFNG on sensory perception of itching post-treatment with dupilumab, i.e., inhibition of IL4R. For this purpose, we first converted the individual KC map in the AD map into a Boolean network (BN) in an automated fashion using CaSQ tool (PMID: 32403123). Then we considered the following pathways in the converted BN for our simulations: i) IL4R -> TSLP -> sensory perception of itching, (ii) IL4R -> KLK5 -> sensory perception of itching, (iii) IL4R -> KLK7 -> sensory perception of itching, (iv) IFNG -> TSLP -> sensory perception of itching, (v) IFNG -| KLK5 -> sensory perception of itching and (vi) IFNG -| KLK7 -> sensory perception of itching. The PBM approach uses a series of random walks to determine the probability of components within the model (PMID:35782730). This approach integrates qualities of both discrete and continuous Markov processes within a Monte Carlo framework (PMID: 37325771). To establish a foundational baseline for our simulations, we parameterized initial state probabilities of ON/OFF. This step is critical as it sets the starting point for the model, reflecting the pre-simulation status of molecular interactions. The equation for updating the state probabilities is given by:
![isd6_0](../pages/projects/isd/images/isd6_0.png) 
where Pt+1(s) is the probability of state s at the next time point and P(s′∣s) is the transition probability from a previous state s′ to the current state s.

Graphical analysis

Sensory Perception of Itch under Different Conditions:
Orange Line (IFNG OFF, IL-4 OFF - Dupilumab): Indicates a significant reduction in itch over time.
Blue Line (IFNG ON, IL-4 OFF - Dupilumab): Shows a less pronounced reduction in itch compared to the IFNG OFF scenario.

![vig6_1](../pages/projects/isd/images/vig6_1.png)

When IFNG is expressed (IFNG ON) in the presence of dupilumab (IL4 OFF), we observe an increase in TSLP levels, a decrease in KLK5 and KLK7 levels and a reduction of around 50% in the activity level of sensory perception of itch.

![vig6_2](../pages/projects/isd/images/vig6_2.png)

When IFNG is not expressed (IFNG OFF) in the presence of dupilumab (IL4 OFF), we observe a decrease in TSLP levels, an increase in KLK5 and KLK7 levels and a reduction of around 70% in the activity level of sensory perception of itch.

![vig6_3](../pages/projects/isd/images/vig6_3.png)
