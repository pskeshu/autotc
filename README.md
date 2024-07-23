# AutoTC - Automated Tissue Culture
Experiment planner!

## FrozenVial
Representation of a vial with frozen cells based on 
- cells that it contains
- date the vial was frozen
- composition of media

## Flask
Represenation of a flask based on
- the type of flask
- when it was seeded
- the media that it contains
- the cells that it houses
- the concentration of seeding

## Media
Representation of the media includes
- name of the media
- Percentage of FBS, if any
- Presence of antibiotics, if any

## Cell
Representation of the cell that is cultured
- name of the cell/cell line
- whether the cell is adherant or in suspension
- the average doubling time of the cell/cell line

## User Story
From a FrozenVial, two Flasks are thawed out in 1:2 ratio on 22/07/2024/11.15.
Show me everything I have done so far.
How confluent are my flasks?
When do I split Flasks next?
I have split my Flasks further.
I have transfected my Flask.