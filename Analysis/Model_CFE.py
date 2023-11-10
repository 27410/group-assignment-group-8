# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:46:18 2023

@author: Driton
"""

from cobra.io import read_sbml_model
from cobra import Reaction, Metabolite


iMM904=read_sbml_model("data/iMM904.xml")

#AMOR =amorphadiene
amorphadiene = Metabolite(id = 'AMOR', compartment='c', name='amorphadiene', formula='C15H24')

#AAOH= artemisinic alcohol
artemisinic_alcohol= Metabolite(id = 'AAOH', compartment='c', name='artemisinic_alcohol', formula='C15H24O')

#AAld=artemisinic_aldehyde
artemisinic_aldehyde= Metabolite(id = 'AAld', compartment='c', name='artemisinic_aldehyde', formula='C15H22O')
#AA=artemisinic_acid
artemisinic_acid= Metabolite(id = 'AA', compartment='c', name='artemisinic_acid', formula='C15H22O2')

#From the nature article, they have added a homolougues Cyb5 enzymatic reaction.
# We will look apart from this since it is not a part of the heterologues pathway.
#FMNH2=Metabolite(id = 'FMNH', compartment='c', name='FMNH2', formula='C17H21N4O9P')
#FMN3=Metabolite(id = 'FMN', compartment='c', name='FMN3', formula='C17H18N4O9P')




cytochrome_P450_enzyme_oxidation= Reaction('CYP71AV1')
CPR1_Oxidation=Reaction('CPR')

CPR_CYP = Reaction("CPR1_CYP71AV1")

# We will look apart from this since it is not a part of the heterologues pathway.
#CYB5_oxidation=Reaction('CYB5')

Amorpha_synthase=Reaction('ADS')

Alcohol_dehydrogenase_1=Reaction('ADH1')

Aldehyde_dehydrogenase_1=Reaction('ALDH1')

#insert metabolic equasions

Amorpha_synthase.add_metabolites(({iMM904.metabolites.frdp_c:-1,amorphadiene:1}))

CPR_CYP.add_metabolites(({amorphadiene: -1,iMM904.metabolites.o2_c: -1,iMM904.metabolites.nadph_c:-1,iMM904.metabolites.h_c: -1,iMM904.metabolites.h2o_c: 1,iMM904.metabolites.nadp_c:1,artemisinic_alcohol:1}))

Alcohol_dehydrogenase_1.add_metabolites(({artemisinic_alcohol:-1,iMM904.metabolites.nad_c:-1,iMM904.metabolites.nadh_c:1,iMM904.metabolites.h_c:1,artemisinic_aldehyde:1}))

Aldehyde_dehydrogenase_1.add_metabolites(({artemisinic_aldehyde:-1,iMM904.metabolites.h2o_c:-1,iMM904.metabolites.nadp_c:-1,artemisinic_acid:1,iMM904.metabolites.h_c:1,iMM904.metabolites.nadph_c:1}))




#insert in model
iMM904.add_reactions([Amorpha_synthase])
iMM904.add_reactions([CPR_CYP])
iMM904.add_reactions([Alcohol_dehydrogenase_1])
iMM904.add_reactions([Aldehyde_dehydrogenase_1])


print(Amorpha_synthase)
print(CPR_CYP)
print(Alcohol_dehydrogenase_1)
print(Aldehyde_dehydrogenase_1)






