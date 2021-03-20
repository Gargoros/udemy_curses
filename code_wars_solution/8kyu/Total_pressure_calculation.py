# Given the molecular mass of two molecules M1M_1M1​ and M2M_2M2​, 
# their masses present m1m_1m1​ and m2m_2m2​ in a vessel of volume VVV at a specific temperature TTT, 
# find the total pressure PtotalP_{total}Ptotal​ exerted by the molecules. 
# Formula to calculate the pressure is:
# Ptotal=(m1M1+m2M2)RTV\LARGE P_{total} = {{({{m_1} \over {M_1}} + {{m_2} \over {M_2}}) R T} 
# \over V}Ptotal​=V(M1​m1​​+M2​m2​​)RT​
# Input

# Six values : m1m_1m1​, m2m_2m2​, M1M_1M1​, M2M_2M2​, VVV, TTT

# Units are:

#    For m1m_1m1​ and m2m_2m2​: grams (ggg)
#    For M1M_1M1​, M2M_2M2​:  g⋅mol−1\ g \cdot mol^{-1} g⋅mol−1
#    For VVV:  dm3\ dm^3 dm3
#    For TTT:  °C\ \degree C °C

# Output

# One value: PtotalP_{total}Ptotal​, in units of atmatmatm.
# Notes

# Remember: Temperature is given in Celsius while SI unit is Kelvin (KKK).  
# 0°C=273.15K\ 0\degree C = 273.15K 0°C=273.15K

# The gas constant  R=0.082dm3⋅atm⋅K−1⋅mol−1\ R = 0.082dm^3 
# \cdot atm \cdot K^{-1} 
# \cdot mol^{-1} R=0.082dm3⋅atm⋅K−1⋅mol−1

def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    K_temp = 273.15 + temp
    R = 0.082
    sum_m = given_mass1 / molar_mass1 + given_mass2 / molar_mass2
    P_total = sum_m * R * K_temp / volume
    return P_total

    