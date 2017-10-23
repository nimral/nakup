import os
import re
import json
import locale


locale.setlocale(locale.LC_ALL, "cs_CZ.UTF-8")


class S:
    """Surovina"""
    def __init__(self, co, kolik, jednotka):
        self.co = co
        self.kolik = kolik  # na člověka
        self.jednotka = jednotka
        self.poznamka = ""

    def __add__(self, other):
        if self.co != other.co:
            raise Exception(
                "Nekompatibilní suroviny: {} a {}"
                .format(self.co, other.co))
        if self.jednotka != other.jednotka:
            raise Exception(
                "Nekompatibilní jednotky: {} a {} ({})"
                .format(self.jednotka, other.jednotka, self.co))

        novy = S(self.co, self.kolik + other.kolik, self.jednotka)
        novy.poznamka = self.poznamka + ", " + other.poznamka
        return novy

    def __str__(self):
        kolik = self.kolik
        if int(kolik) == kolik:
            kolik = int(kolik)
        if type(kolik) != int:
            kolik = "{:.2f}".format(kolik)
        return r"{} {} {}".format(self.co, kolik, self.jednotka)

    def latex(self):
        kolik = self.kolik
        if int(kolik) == kolik:
            kolik = int(kolik)
        if type(kolik) != int:
            kolik = "{:.2f}".format(kolik)
        return r"{} {} {} {{\color{{gray}}({})}}\\".format(
            self.co.replace('%', r'\%'), kolik, self.jednotka, self.poznamka
        )

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return locale.strxfrm(self.co) < locale.strxfrm(other.co)


class Jidlo:
    def __init__(self, nazev, suroviny):
        self.nazev = nazev
        self.suroviny = suroviny

    def __repr__(self):
        return "<Jídlo: {}>".format(self.nazev)


# položky možno přejmenovat, ale změna čísla rozbije uložené rozřazení
cislovani_oblasti = {
    1: "Ovoce a zelenina",
    2: "Mléčné výrobky",
    3: "Mražené",
    4: "Maso",
    5: "Sypké, těstoviny, ...",
    6: "Pečení",
    7: "Konzervy",
    8: "Pečivo",
    9: "Koření",
    10: "Lahve",
    11: "Papírnictví",
    12: "Sladkosti",
    13: "Hygiena",
}


def seznam(jidelnicek, lidi, od, do=None):
    if do is not None:
        jidla = [v for k, v in jidelnicek.items() if k >= od and k < do]
    else:
        jidla = [jidelnicek[od]]

    co_koupit = {}
    for jidlo in jidla:
        for s in jidlo.suroviny:
            s2 = S(s.co, s.kolik * lidi, s.jednotka)
            kolik = s2.kolik
            if int(kolik) == kolik:
                kolik = int(kolik)
            if type(kolik) != int:
                kolik = "{:.2f}".format(kolik)
            s2.poznamka = "{}: {} {}".format(jidlo.nazev, kolik, s2.jednotka)
            if s2.co in co_koupit:
                co_koupit[s2.co] += s2
            else:
                co_koupit[s2.co] = s2
    return co_koupit


def roztrid_seznam(seznam):
    """Roztřídí nákupní seznam na předpokládané oblasti v obchodě

    Vrací slovník {"oblast": [Suroviny], ...}
    """

    # uložené roztřízení
    if os.path.isfile("roztrizene.json"):
        with open("roztrizene.json", "r") as fin:
            roztrizene = json.load(fin)
    else:
        roztrizene = {}

    oblasti = {}
    for co, s in seznam.items():
        if co not in roztrizene:
            for k, v in cislovani_oblasti.items():
                print(k, v)
            volba = ""
            while volba not in cislovani_oblasti:
                print("\nZvolte prosím, kam patří {}: ".format(co))
                volba = input().strip()
                try:
                    volba = int(volba)
                except Exception:
                    pass
            roztrizene[co] = volba

        oblasti.setdefault(cislovani_oblasti[roztrizene[co]], []).append(s)
    with open("roztrizene.json", "w") as fout:
        json.dump(roztrizene, fout, ensure_ascii=False)
    return oblasti


header = r'''\documentclass[a4paper]{article}
\usepackage[czech]{babel}
%\usepackage{a4wide}
\usepackage[top=1.9cm, bottom=1.9cm, left=2cm, right=2cm]{geometry}
\usepackage[utf8]{inputenc} % for unicode UTF-8
\usepackage[T1]{fontenc} % for searchable pdf
\usepackage{lmodern} % for searchable pdf
\usepackage{microtype}
\usepackage[usenames,dvipsnames,svgnames,table]{xcolor}
%\pagestyle{empty} % removes page numbers

\begin{document}
\setlength{\parindent}{0cm}
'''

footer = r'''
\end{document}
'''


def vytiskni_roztrizeny_seznam(oblasti, pdf_filename):
    """Vytvoří pdf s roztřízeným nákupním seznamem"""
    latex_filename = re.sub(r'pdf$', 'latex', pdf_filename)
    with open(latex_filename, "w") as fout:
        fout.write(header)

        for oblast, polozky in sorted(
                oblasti.items(), key=lambda x: locale.strxfrm(x[0])):
            fout.write("\n\n")
            fout.write(r'\textbf{%s}\\' % oblast)
            for s in sorted(polozky):
                fout.write(s.latex())

        fout.write(footer)
    os.system("pdflatex {}".format(latex_filename))
