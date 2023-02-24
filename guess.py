# -*- coding: utf-8 -*-

import json

PeriodicTable = """
H                                                     He
Li Be                                  B  C  N  O  F  Ne
Na Mg                                  Al Si P  S  Cl Ar
K  Ca    Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
Rb Sr    Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
Cs Ba    Lu Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
Fr Ra    Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

      La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb
      Ac Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No
"""
elements = list(map(str.lower, PeriodicTable.split()))

AdobeProducts = {
    "Ae": "After Effects",
    "Ai": "Illustrator",
    "An": "Animate",
    "Ar": "Aero",
    "Au": "Audition",
    "Be": "Behance",
    "Br": "Bridge",
    "Ca": "Capture",
    "Cf": "ColdFusion",
    "Ch": "Character Animator",
    "Co": "Content Server",
    "Cp": "Captivate",
    "Dn": "Dimension",
    "Ds": "Substance 3D Designer",
    "Dw": "Dreamweaver",
    "Fb": "Flash Builder",
    "Fm": "FrameMaker",
    "Fr": "Fresco",
    "Fs": "Fuse",
    "Ic": "InCopy",
    "Id": "InDesign",
    "Lc": "LiveCycle",
    "Lr": "Lightroom",
    "Md": "Substance 3D Modeler",
    "Me": "Media Encoder",
    "Pf": "Portfolio",
    "Pl": "Prelude",
    "Pn": "Presenter",
    "Pr": "Premiere",
    "Ps": "Photoshop",
    "Pt": "Substance 3D Painter",
    "Rh": "RoboHelp",
    "Ru": "Premiere Rush",
    "Sa": "Substance 3D Sampler",
    "Sc": "Scout",
    "Sg": "Substance 3D Stager",
    "Sp": "Spark",
    "St": "Stock",
    "Xd": "XD",
}
# elements = list(map(str.lower, AdobeProducts.keys()))

result = []


def guess(word):
    wordarray = word
    if len(wordarray) == 0:
        return True
    if wordarray[:2] in elements:
        result.append(wordarray[:2])
        elements.remove(wordarray[:2])
        if guess(wordarray[2:]) is False:
            result.pop()
            elements.append(wordarray[:2])
            if wordarray[:1] in elements:
                result.append(wordarray[:1])
                elements.remove(wordarray[:1])
                if guess(wordarray[1:]) is False:
                    result.pop()
                    elements.append(wordarray[:1])
                    return False
    elif wordarray[:1] in elements:
        result.append(wordarray[:1])
        elements.remove(wordarray[:1])
        if guess(wordarray[1:]) is False:
            result.pop()
            elements.append(wordarray[:1])
            if wordarray[:2] in elements:
                result.append(wordarray[:2])
                elements.remove(wordarray[:2])
                if guess(wordarray[2:]) is False:
                    result.pop()
                    elements.append(wordarray[:2])
                    return False
    else:
        return False


def main(word):
    guess(word.lower())
    if "".join(result) == word.lower():
        return True
    else:
        return False


words = json.load(open("words_dictionary.json"))
with open("result.txt", "w") as f:
    for x in words.keys():
        result = []
        elements = list(map(str.lower, PeriodicTable.split()))
        # elements = list(map(str.lower, AdobeProducts.keys()))
        if main(x) and len(result) > 1:
            f.write(f"{len(result)},{x},{result}\n")
