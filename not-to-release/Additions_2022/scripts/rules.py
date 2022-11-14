UD_map = {
    # ipsd_tag : UD_tag
    "N": "NOUN",  # generalized nouns tagged as NOUN
    "D": "DET",  # generalized determiners tagged as DET (determiner)
    "ONE": "DET",  # ath. áður taggað sem NUM
    "ONES": "DET",
    "P": "ADP",  # generalized prepositions tagged as ADP
    "RP": "ADP",  # specifiers of P/complements of P - Ath. flokka sem eitthvað annað?
    "RPX": "ADP",
    "FOR": "ADP",
    "Q": "DET",  # quantifiers tagged as DET - áður: quantifiers tagged as ADJ - ATH ÞETTA ÞARF AÐ ENDURSKOÐA
    "C": "SCONJ",  # complimentizer tagged as SCONJ (subordinate conjunction)
    "V": "VERB",
    "DO": "VERB",  #'gera', do, tagged as verb
    "HV": "AUX",  #'have' tagged as auxiliary verb
    "MD": "AUX",  # modal verbs tagged as auxiliary
    "RD": "VERB",  #'verða', become, tagged as verb
    "W": "DET",  # WH-determiner tagged as DET (determiner)
    "R": "VERB",  # All forms of "verða" tagged as VERB
    "TO": "PART",  # Infinitive marker tagged as PART (particle)
    "FP": "PART",  # focus particles marked as PART
    "NPR": "PROPN",  # proper nouns tagged as PROPN
    "NPRS": "PROPN",
    "PRO": "PRON",
    # 'WQ' : 'PRON',  #interrogative pronoun
    "WQ": "SCONJ",
    "WPRO": "PRON",  # wh-pronouns
    "SUCH": "PRON",
    "ES": "PRON",  # expletive tagged as PRON
    "MAN": "PRON",
    "MANS": "PRON",
    "NUM": "NUM",
    "ADJ": "ADJ",  # Adjectives tagged as ADV
    "ADJR": "ADJ",  # Comparative adjectives tagged as ADV
    "ADJS": "ADJ",  # Superlative adjectives tagged as ADV
    "WADJ": "ADJ",
    "ADV": "ADV",  # Adverbs tagged as ADV
    "WADV": "ADV",  # TODO: ath. betur - bara spor?
    "NEG": "ADV",
    "ADVR": "ADV",  # Comparative adverbs tagged as ADV
    "ADVS": "ADV",  # Superlative adverbs tagged as ADV
    "ALSO": "ADV",
    "OTHER": "PRON",
    "OTHERS": "PRON",
    "INTJ": "INTJ",  # interjection
    "FW": "X",
    "LS": "NUM",  # list marker tagged as numeral
    "X": "X",
}

OTB_map = {
    "Gender": {"k": "Masc", "v": "Fem", "h": "Neut", "x": None},
    "Number": {"f": "Plur", "e": "Sing"},  # noun, plural number  # noun singular number
    "PronType": {
        "p": "Prs",  # personal
        "e": "Prs",  # posessive (tagged as personal)
        # 'a' : 'Rcp',   #reciprocal
        "s": "Int",  # interrogative
        "t": "Rel",  # relative
        "a": "Dem",  # demonstrative
        "b": "Dem",
        "o": "Ind",  # indefinite
    },
    "Tense": {"n": "Pres", "þ": "Past", "NF": None},  # present tense  # past tense
    "Person": {"1": "1", "2": "2", "3": "3"},
    "Case": {
        "n": "Nom",  # nominative case
        "o": "Acc",  # accusative case
        "þ": "Dat",  # dative case
        "e": "Gen",  # dative case
        None: "Nom",
    },
    "Mood": {
        "n": "infinitive",
        "b": "Imp",  # imperative
        "f": "Ind",  # indicative
        "v": "Sub",  # subjunctive
        "I": "Ind",  # indicative (IcePaHC POS-tag)
        "S": "Sub",  # subjunctive (IcePaHC POS-tag)
        "OSKH": None,  # TEMP
    },
    "VerbForm": {
        "": "Fin",  # finite verb
        "n": "Inf",  # infinitive verb
        "l": "Part",  # participle
        "þ": "Part",  # participle
        "s": "Sup",
    },
    "Voice": {
        "g": "Act",  # active voice
        "m": "Mid",  # middle voice
        "pass": "Pass",  # passive voice
    },
    "Definite": {
        "s": "Ind",  # adjectives
        "v": "Def",  # adjectives
        "g": "Def",  # nouns
        "o": None,  # 'ÓBEYGT', TODO: check if output 100% correct
        None: "Ind",
    },
    "Degree": {"f": "Pos", "m": "Cmp", "e": "Sup"},  # adjectives  # adjectives  # nouns
    "NumType": {
        "f": "Card",  # Cardinal number
        "a": "Card",
        "o": "Ord",  # FIX Ordinal number (not in OTB tag)
        "p": "Frac",  # Fraction
    },
}

Icepahc_feats = {
    "Case": {"N": "Nom", "A": "Acc", "D": "Dat", "G": "Gen"},
    "NOUN": {
        "Case": {
            "N": "Nom",  # nominative case
            "A": "Acc",  # accusative case
            "D": "Dat",  # dative case
            "G": "Gen",  # genitive case
        },
        "Number": {
            "NS": "Plur",  # noun, plural number
            "N": "Sing",
            "NPR": "Sing",  # noun singular number
            "NPRS": "Plur",  # proper noun plural
        },
        "Definite": {"$": "Def", "": "Ind"},  # TODO: remove def from dict
    },
    "PRON": {  # Case, Gender, Number, PronType
        "Number": {
            "S": "Plur",  # noun, plural number
            "": "Sing",  # noun singular number
        },
        "Case": {
            "N": "Nom",  # nominative case
            "A": "Acc",  # accusative case
            "D": "Dat",  # dative case
            "G": "Gen",  # genitive case
        },
    },
    "DET": {
        "Number": {"": "Sing", "S": "Plur"},
        "Degree": {"": "Pos", "R": "Cmp", "S": "Sup"},
    },
    "ADJ": {
        "Case": {"N": "Nom", "A": "Acc", "D": "Dat", "G": "Gen"},
        "Degree": {
            "P": "Pos",  # first degree
            "R": "Cmp",  # second Degree
            "S": "Sup",  # third degree
        },
    },
    "ADV": {
        "Degree": {
            "P": "Pos",  # first degree
            "R": "Cmp",  # second Degree
            "S": "Sup",  # third degree
        },
        "Case": {"N": "Nom", "A": "Acc", "D": "Dat", "G": "Gen"},
    },
    "VERB": {
        "Mood": {
            "IMP": "Imp",  # imperative
            "I": "Ind",  # indicative (IcePaHC POS-tag)
            "S": "Sub",  # subjunctive (IcePaHC POS-tag)
        },
        "Tense": {"P": "Pres", "D": "Past"},
        "VerbForm": {
            "": "Fin",  # finite verb
            "inf": "Inf",  # infinitive verb
            "I": "Inf",
            "N": "Part",  # participle
            "G": "Part",
        },
    },
}

abbr_map = {
    # abbr : token, lemma, lemma(true)
    "o.": (r"o\.", "og", "og", "og"),
    "s.": (r"s\.", "svo", "svo", ""),
    "frv.": (r"frv\.", "framvegis", "framvegis", ""),
    "t.": (r"t\.", "til", "til", ""),
    "t.": (r"t\.", "til", "t", ""),
    "d.": (r"d\.", "dæmis", "dæmi", ""),
    "fl.": (r"fl\.", "fleira", "margur", ""),
    "t.$": (r"t\.\$", "til", "t", "til"),
    "$d.": (r"\$d\.", "dæmis", "d", "dæmi"),
    "þ.$": (r"þ\.\$", "það", "þú", "þú"),
    "$e.": (r"\$e\.", "er", "vera", ""),
    "$e.$": (r"\$e\.\$", "er", "vera", ""),
    "$a.$": (r"\$a\.\$", "að", "a\.", "að"),
    "$s.": (r"\$s\.", "segja", "s", "segja"),
    "a$": (r"a$", "að", "að", "að"),
    "$m$": (r"\$m$", "minnsta", "lítill", ""),
    # '$k' : (r'\$k', 'kosti', 'kostur', ''), # NOTE: Not needed!
    "m.$": (r"m\.\$", "meðal", "m", "meðal"),
    "$a.": (r"\$a\.", "annars", "annar", ""),
    "m.$": (r"m\.\$", "meira", "m", "meira"),
    "$a.$": (r"\$a\.\$", "að", "a\.", "að"),
    "$s.": (r"\$s\.", "segja", "s", "segja"),
    "t.$": (r"t\.\$", "til", "til", ""),
    "$d.": (r"\$d\.", "dæmis", "dæmis", ""),
}

lex_class_map = {
    "a": ("ADP", "ADV", "ADJ"),
    "c": ("CCONJ", "SCONJ", "PART"),
    "e": ("OTHER"),
    "f": ("PRON", "DET"),
    "g": ("DET"),
    "l": ("ADJ", "DET", "ADV"),
    "n": ("NOUN", "PROPN"),
    "s": ("VERB", "AUX"),
    "t": ("NUM", "ADJ"),
    "x": ("X", "SYM", "INTJ"),
}
