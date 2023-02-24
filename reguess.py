import re
import sys
from functools import reduce

regexp = r"(He|Li|Be|Ne|Na|Mg|Al|Si|Cl|Ar|Ca|Sc|Ti|Cr|Mn|Fe|Co|Ni|Cu|Zn|Ga|Ge|As|Se|Br|Kr|Rb|Sr|Zr|Nb|Mo|Tc|Ru|Rh|Pd|Ag|Cd|In|Sn|Sb|Te|Xe|Cs|Ba|Lu|Hf|Ta|Re|Os|Ir|Pt|Au|Hg|Tl|Pb|Bi|Po|At|Rn|Fr|Ra|Lr|Rf|Db|Sg|Bh|Hs|Mt|Ds|Rg|Cn|Nh|Fl|Mc|Lv|Ts|Og|La|Ce|Pr|Nd|Pm|Sm|Eu|Gd|Tb|Dy|Ho|Er|Tm|Yb|Ac|Th|Pa|Np|Pu|Am|Cm|Bk|Cf|Es|Fm|Md|No)|([HBCNOFPSKVYIWU])|(Ae|Ai|An|Ar|Au|Be|Br|Ca|Ch|Cp|Dn|Ds|Dw|Fb|Fm|Fr|Fs|Ic|Id|Lr|Md|Me|Pf|Pl|Pn|Pr|Ps|Pt|Rh|Ru|Sa|Sc|Sg|Sp|St|Xd)|([^aeiou][aeiou])|(.{1,2})"


def splitWord(Word):
    groups = re.findall(regexp, Word, re.I)
    return reduce(
        list.__add__,
        map(lambda x: [{x[r]: r + 1} for r in range(len(x)) if x[r] != ""], groups),
    )


def main():
    result = splitWord(sys.argv[1])
    print(result)


if __name__ == "__main__":
    main()
