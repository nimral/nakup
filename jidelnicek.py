"""Příklad definice jídelníčku a generování nákupního seznamu"""
from nakup import Jidlo, S, seznam, roztrid_seznam, vytiskni_roztrizeny_seznam

lidi = 24 + 11  # účastníků + orgů
bezlepci = 2

so1, ne1, po, ut, st, ct, pa, so2, ne2 = range(9)
snidane, svacina1, polevka, druhe, svacina2, vecere = range(6)

ks = "ks"
kg = "kg"
l = "l"

jidelnicek = {
    (so1, vecere): Jidlo(
        "obložené bagety",
        [
            S("bagety", 1, ks),
            S("máslo", 0.05, kg),
            S("šunka", 0.04, kg),
            S("fr. hořčice", 1 / 30, ks),
            S("sýr", 0.04, kg),
            S("rajčata", 0.2, kg),
            S("listový salát", 2 / 30, ks),
        ]
    ),
    (ne1, snidane): Jidlo(
        "Chleba s pomáslem",
        [
            S("chleba", 1 / 10, "boch."),
            S("pomazánkové máslo", 1 / 4, ks),
            S("papriky", 0.05, kg),
            S("okurky", 0.05, kg),
        ]
    ),
    (ne1, svacina1): Jidlo(
        "Jablko", [S("jablka", 1, ks)]
    ),
    (ne1, polevka): Jidlo(
        "Zeleninová polévka",
        [
            S("olej", 0.3 / lidi, l),
            S("cibule", 0.05 / 4, kg),
            S("stroužek česneku", 2 / 4, ks),
            S("mrkev", 0.1 / 4, kg),
            S("celer", 0.1 / 4, kg),
            S("petržel", 0.1 / 4, kg),
            S("zeleninový bujón v kostce", 0.001, kg),
            S("ovesné vločky (jemné)", 0.005, kg),
            S("brambory", 0.033, kg),
            S("mražený hrášek", 0.1 / 4, kg),
            S("vajíčka", 1.5 / 4, ks),
            S("sůl", 0.001, kg),
            S("květák", 1 / lidi, ks),
        ]
    ),
    (ne1, druhe): Jidlo(
        "Šulánky s mákem",
        [
            S("mletý mák", 0.1 / 2.81, kg),
            S("hrubá mouka", 0.25 / 2.81, kg),
            S("vejce", 1 / 2.81, ks),
            S("máslo", 0.03 / 2.81, kg),
            S("tvaroh (polotučný v kostce)", 0.25 / 2.81, kg),
            S("sůl", 0.002 / 2.81, kg),
            S("mléko", 1 / 30, l),
        ]
    ),
    (ne1, svacina2): Jidlo(
        "Zelenina",
        [S("papriky", 0.1, kg)]
    ),
    (ne1, vecere): Jidlo(
        "Kyselica",
        [
            S("kysané zelí", 0.5 / 6, kg),
            S("klobásky", 0.33, ks),
            S("brambory", 0.05, kg),
            S("šlehačka", 0.15 / 6, l),
            S("hladká mouka", 0.01, kg),
            S("nové koření (raději mleté)", 0.01 / lidi, kg),
            S("pepř", 0.005 / lidi, kg),
            S("bobkový list", 1 / lidi, ks),
            S("majoránka", 0.001, kg),
            S("stroužek česneku", 2 / 6, ks),
            S("chleba", 1 / 10, "boch."),
            S("bezlepkový chleba", 0.05 / lidi, kg),
            S("cibule", 0.033, kg),
        ]
    ),
    (po, snidane): Jidlo(
        "Jáhlová kaše",
        [
            S("jáhly", 0.1, kg),
            S("mléko", 0.2, l),
            S("cukr", 0.05, kg),
            S("kakao", 0.005, kg),
        ]
    ),
    (po, svacina1): Jidlo(
        "Ovoce",
        [
            S("banány", 1, ks),
        ]
    ),
    (po, polevka): Jidlo(
        "Vývar",
        [
            S("maso s kostí", 3 / lidi, kg),
            S("mrkev", 0.75 / lidi, kg),
            S("petržel", 0.5 / lidi, kg),
            S("celer", 0.5 / lidi, kg),
            S("cibule", 0.5 / lidi, kg),
            S("(čerstvá zelená petržel)", 1 / lidi, ks),
            S("pepř (celý)", 0.01 / lidi, kg),
            S("polohrubá mouka", 0.2 / lidi, kg),
            S("vajíčka", 8 / lidi, ks),
        ]
    ),
    (po, druhe): Jidlo(
        "Dalbát",
        [
            S("červená čočka", 0.2, kg),
            S("basmati rýže", 0.2, kg),
            S("cibule", 0.05, kg),
            S("zázvor", 0.02, kg),
            S("chilli", 0.0015, kg),
        ]
    ),
    (po, svacina2): Jidlo(
        "Mrkev / Párek v rohlíku",
        [
            S("párek", 1, ks),
            S("mrkev", 0.05, kg),
            S("rohlík", 1, ks),
            S("kečup", 1, ks),
        ]
    ),
    (po, vecere): Jidlo(
        "Pohanka se špenátem",
        [
            S("pohanka", 0.075, kg),
            S("špenát sekaný", 0.2, kg),
            S("cibule", 0.05, kg),
            S("citron", 0.1, ks),
            S("sůl", 0.001, kg),
            S("pepř", 0.01 / lidi, kg),
            S("chilli", 0.0015, kg),
            S("oregano", 0.0015, kg),
            S("balkánský sýr", 0.03, kg),
        ]
    ),
    (ut, snidane): Jidlo(
        "Ovesná kaše",
        [
            S("ovesné vločky (jemné)", 0.5 / 8, kg),
            S("banány", 1, ks),
            S("kakao", 0.003, kg),
            S("mléko", 0.3, l),
            S("cukr", 0.003, kg),
        ]
    ),
    (ut, svacina1): Jidlo(
        "Mandarinka",
        [S("mandarinka", 1, ks)]
    ),
    (ut, polevka): Jidlo(
        "Dýňová polévka",
        [
            S("máslová dýně (bude-li)", 1 / 5, ks),
            S("cibule", 0.03, kg),
            S("cukr moučka", 0.05, kg),
            S("šlehačka", 0.2 / 5, l),
            S("zeleninový bujón v kostce", 0.001, kg),
            S("zázvor", 0.005, kg),
        ]
    ),
    (ut, druhe): Jidlo(
        "Kuřecí perkelt",
        [
            S(
                "6 horních kousků kuřecích stehen/3 kuřecí stehna v kuse "
                "(=horní i spodní díl)",
                1 / 3, ks
            ),
            S("cibule", 0.2 / 3, kg),
            S("olej", 2 / 3, l),
            S("sladká mletá paprika", 0.01 / 3, kg),
            S("rajčatový protlak", 0.02 / 3, kg),
            S("papriky", 0.1, kg),
            S("chilli", 0.01 / 3, kg),
        ]
    ),
    (ut, svacina2): Jidlo(
        "Šopský salát",
        [
            S("rajčata", 0.04, kg),
            S("okurky", 0.04, kg),
            S("papriky", 0.04, kg),
            S("balkánský sýr", 0.02, kg),
            S("olivový olej", 1 / lidi, ks),
            S("balsamico", 1 / lidi, ks),
        ]
    ),
    (ut, vecere): Jidlo(
        "Fazole s chlebem",
        [
            S("fazole (žíhané)", 0.5 / 5, kg),
            S("olej", 0.01, l),
            S("cibule", 0.01, kg),
            S("rajčata krájená v plechovce", 2 / 4, ks),
            S("zeleninový bujón v kostce", 0.001, kg),
            S("sůl", 0.002, kg),
            S("mletý cukr", 0.002, kg),
            S("rozmarýn", 0.001, kg),
            S("klobásky", 1/2, ks),
            S("chleba", 1 / 10, "boch."),
            S("bezlepkový chleba", 0.05 / lidi, kg),
        ]
    ),
    (st, snidane): Jidlo(
        "Roztroušená snídaně",
        [
            S("chleba", 1 / 10, "boch."),
            S("máslo", 0.025, kg),
            S("marmeláda", 0.5 / lidi, kg),
        ]
    ),
    (st, druhe): Jidlo(
        "výlet",
        [
            S("jablka", 1, ks),
            S("Perníček", 1, ks),
        ]
    ),
    (st, svacina2): Jidlo(
        "výlet",
        [
            S("bagety velké", 1, ks),
            S("rajčata", 0.033, kg),
            S("máslo", 5 * 0.25 / lidi, kg),
            S("mozzarella", 0.4, ks),
            S("šunka", 0.01, kg),
            S("listový salát", 1 / lidi, ks),
            S("gouda", 0.01, kg),
            S("bezlepkový chleba", 0.2 / lidi, kg)
        ]
    ),
    (st, vecere): Jidlo(
        "chili con carne",
        [
            S("fazole v rajčatové omáčce (plechovka)", 4 / lidi, kg),
            S("fazole černé (plechovka)", 4 / lidi, kg),
            S("kukuřice", 5 / lidi, ks),
            S("chleba", 3 / lidi, "boch."),
            S("chili omáčka", 1 / lidi, l),
            S("cibule", 1 / lidi, kg),
            S("mleté maso", 4 / lidi, kg),
            S("olej", 3 / lidi, l),
            S("bezlepkový chleba", 2 * 0.12 / lidi, kg),
        ]
    ),
    (ct, snidane): Jidlo(
        "jogurt",
        [
            S("jogurt bílý 300 g", 18 / lidi, ks),
            S("cornflaky", 1 / lidi, kg),
            S("granko", 1 / lidi, ks),
            S("cukr moučka", 1 / lidi, kg),
            S("marmeláda", 0.5 / lidi, kg),
        ]
    ),
    (ct, svacina1): Jidlo(
        "jablko",
        [
            S("jablka", 1, ks),
        ]
    ),
    (ct, polevka): Jidlo(
        "česnečka",
        [
            S("zeleninový bujón v kostce", 0.001, kg),
            S("cibule", 0.5 / lidi, kg),
            S("česnek", 2.5 / lidi, "hlávky"),
            S("eidam", 0.75 / lidi, kg),
            S("kuličky do polévky", 1.8 / lidi, kg),
            S("krupice", 1 / lidi, ks),
        ]
    ),
    (ct, druhe): Jidlo(
        "bramboráky",
        [
            S("brambory", 12 / lidi, kg),
            S("polohrubá mouka", 2 / lidi, kg),
            S("vejce", 16 / lidi, ks),
            S("kečup", 1 / lidi, ks),
            S("zakysaná smetana", 4 / lidi, ks),
            S("česnek", 0.5 / lidi, "hlávky"),
        ]
    ),
    (ct, svacina2): Jidlo(
        "tzatziky",
        [
            S("okurky", 2.5 / lidi, kg),
            S("jogurt bílý 300 g", 5 / lidi, ks),
            S("česnek", 0.5 / lidi, "hlávky"),
            S("chleba", 2 / lidi, "boch."),
        ]
    ),
    (ct, vecere): Jidlo(
        "dukátové buchtičky",
        [
            S("dukátové buchtičky", 4 / lidi, kg),
            S("vanilkový pudink", 20 / lidi, ks),
            S("cukr moučka", 1 / lidi, kg),
            S("mléko", 11 / lidi, l),
        ]
    ),
    (pa, snidane): Jidlo(
        "vánočka",
        [
            S("vánočka", 8 / lidi, ks),
            S("máslo", 0.5 / lidi, kg),
            S("marmeláda", 0.5 / lidi, kg),
            S("mléko", 8 / lidi, l),
            S("granko", 1 / lidi, ks),
        ]
    ),
    (pa, svacina1): Jidlo(
        "mrkev",
        [
            S("mrkev", 5 / lidi, kg),
        ]
    ),
    (pa, polevka): Jidlo(
        "bramboračka",
        [
            S("česnek", 0.33 / 4, "hlávky"),
            S("mrkev", 0.2 / 4, kg),
            S("brambory", 0.15, kg),
            S("celer", 1 / lidi, kg),
            S("petržel", 0.03, kg),
            S("cibule", 0.1 / 4, kg)
        ]
    ),
    (pa, druhe): Jidlo(
        "bram. kned. špen. mas.",
        [
            S("bramborový knedlík", 5.25 / lidi, kg),
            S(
                "uzené maso (bez nutnosti dalšího tepelného opracování)",
                3 / lidi, kg
            ),
            S("špenát mražený", 6 / lidi, kg),
            S("cibule", 3.6 / lidi, kg),
            S("smetana 12%", 2 / lidi, l),
            S("česnek", 1.5 / lidi, "hlávky"),
        ]
    ),
    (pa, svacina2): Jidlo(
        "buchta",
        [
            S("vejce", 10 / lidi, ks),
            S("mléko", 1 / lidi, l),
            S("cukr krupice", 1 / lidi, kg),
            S("vanilkový pudink", 2 / lidi, ks),
            S("tvaroh", 2 / lidi, "balení"),
            S("vanilkový cukr", 2 / lidi, "balíčky"),
            S("olej", 0.3 / lidi, l),
            S("kakao", 0.3 / lidi, kg),
            S("polohrubá mouka", 1 / lidi, kg),
            S("prášek do pečiva", 2 / lidi, "balíčky"),
        ]
    ),
    (pa, vecere): Jidlo(
        "těstoviny",
        [
            S("cestoviny široké rezance", 6 / lidi, kg),
            S("cestoviny klinky", 2 / lidi, kg),
            S("kysané zelí", 2 / lidi, kg),
            S("cibule", 0.5 / lidi, kg),
            S("mletý mák", 1 / lidi, kg),
            S("povidla", 1 / lidi, kg),
            S("máslo", 0.5 / lidi, kg),
            S("cukr moučka", 1 / lidi, kg),
            S("bezlepkové těstoviny", 0.5 / lidi, kg),
        ]
    ),
    (so2, snidane): Jidlo(
        "brynzová pomazánka",
        [
            S("chleba", 3 / lidi, "boch."),
            S("rostlinné máslo", 0.4 / lidi, kg),
            S("brynza", 0.4 / lidi, kg),
            S("cibule", 0.15 / lidi, kg),
            S("bezlepkový chleba", 0.24 / lidi, kg),
        ]
    ),
    (so2, polevka): Jidlo(
        "čínská sladko kyselá",
        [
            S("kuřecí bujón", 12 / lidi, l),
            S("mrkev", 0.6 / lidi, kg),
            S("petržel", 0.6 / lidi, kg),
            S("pórek", 2.5 / lidi, ks),
            S("červená paprika", 0.3 / lidi, kg),
            S("celer", 0.3 / lidi, kg),
            S("cibule", 0.5 / lidi, kg),
            S("ocet", 2 / lidi, l),
            S("solamil (nemusí být)", 1 / lidi, "balení"),
            S("chili omáčka", 1 / lidi, l),
            S("vejce", 16 / lidi, ks),
        ]
    ),
    (so2, druhe): Jidlo(
        "hovězí s těstovinami a rajč. om.",
        [
            S("hovězí maso", 6 / lidi, kg),
            S("těstoviny kolínka", 7.5 / lidi, kg),
            S("rajčatový protlak", 1 / lidi, kg),
            S("cibule", 1 / lidi, kg),
            S("máslo", 0.2 / lidi, kg),
            S("bezlepkové těstoviny", 0.5 / lidi, kg),
        ]
    ),
}


jidelnicek2 = {
    (ne1, druhe): Jidlo(
        "Šulánky s mákem",
        [
            S("mletý mák", 0.1 / 2.81, kg),
            S("hrubá mouka", 0.25 / 2.81 / lidi * (lidi - bezlepci), kg),
            S(
                "pohanková mouka (nebo jiná bezlepková; "
                "když nebude, tak bezlepkové těstoviny)",
                0.25 / 2.81 / lidi * 2,
                kg
            ),
            S("vejce", 1 / 2.81, ks),
            S("máslo", 0.03 / 2.81, kg),
            S("tvaroh (polotučný v kostce)", 0.25 / 2.81, kg),
            S("sůl", 0.002 / 2.81, kg),
            S("mléko", 1 / 30, l),
        ]
    ),
    (ut, polevka): Jidlo(
        "Dýňová polévka",
        [
            S("máslová nebo hokaido dýně", 0.6 / 4, kg),
            S("cibule", 0.03, kg),
            S("cukr moučka", 0.05, kg),
            S("šlehačka", 0.2 / 5, l),
            S("zeleninový bujón v kostce", 0.001, kg),
            S("zázvor", 0.005, kg),
            S("chleba", 0.02 / lidi * (lidi - bezlepci), kg),
            S("olej", 0.25 / lidi, l),
        ]
    ),
}


if __name__ == "__main__":
    rs = roztrid_seznam(seznam(jidelnicek, lidi, (so1, snidane), (ne2, vecere)))
    vytiskni_roztrizeny_seznam(rs, "seznam.pdf")
