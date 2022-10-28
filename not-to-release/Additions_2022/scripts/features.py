"""

A script for converting various token information into UD features, both for Icelandic and 
Faroese text, for the respective token.
The conversion builds on information from existing tags if a third-party tagger (such as ABLTagger) 
is not used. If so, the tagger's output is converted to the proper format.

"""

import re
import json
import string
import requests

from collections import defaultdict

from rules import UD_map, OTB_map, Icepahc_feats, abbr_map, lex_class_map


def decode_escaped(string, lemma=False):
    """
    Fixes various punctuations (-, /, ') that are escaped in corpus data
    Also fixes most abbrevations in corpus data using abbrevations rules dictionar
    """
    if re.search(r"[<>]", string):
        """Tokens processed"""
        if re.search(r"</?dash/?>", string):
            string = re.sub(r"</?dash/?>", "-", string)
        if re.search(r"</?slash/?>", string):
            string = re.sub(r"</?slash/?>", "/", string)
        if re.search(r"</?apostrophe/?>", string):
            string = re.sub(r"</?apostrophe/?>", "'", string)
        return string
    if string in abbr_map.keys():
        string = re.sub(abbr_map[string][0], abbr_map[string][1], string)

        return string
    else:
        return string


class Features:
    """ """

    def __init__(self, tag):
        self.features = defaultdict(list)
        self.methods = {
            "n": self._noun_features,
            "l": self._adjective_features,
            "f": self._pronoun_features,
            "g": self._determiner_features,
            "t": self._numeral_features,
            "s": self._verb_features,
            "a": self._adverb_features,
            "e": self._other_features,
            "x": self._other_features,
        }
        self.methods.get(tag[0], lambda x: "x")(tag)

    def _noun_features(self, tag):
        if "-" in tag:
            tag, tag_extra = tag.split("-")
        self.features["Gender"] = OTB_map["Gender"][tag[1]]
        self.features["Number"] = OTB_map["Number"][tag[2]]
        self.features["Case"] = OTB_map["Case"][tag[3]]
        if len(tag) > 4:
            self.features["Definite"] = OTB_map["Definite"][tag[4]]
        else:
            self.features["Definite"] = OTB_map["Definite"][None]
        return self

    def _adjective_features(self, tag):
        self.features["Gender"] = OTB_map["Gender"][tag[1]]
        self.features["Number"] = OTB_map["Number"][tag[2]]
        self.features["Case"] = OTB_map["Case"][tag[3]]
        self.features["Definite"] = OTB_map["Definite"][tag[4]]
        self.features["Degree"] = OTB_map["Degree"][tag[5]]
        return self

    def _pronoun_features(self, tag):
        self.features["PronType"] = OTB_map["PronType"][tag[1]]
        if tag[2] in {"1", "2"}:
            self.features["Person"] = OTB_map["Person"][tag[2]]
        else:
            self.features["Gender"] = OTB_map["Gender"][tag[2]]
        self.features["Number"] = OTB_map["Number"][tag[3]]
        self.features["Case"] = OTB_map["Case"][tag[4]]
        return self

    def _determiner_features(self, tag):
        self.features["Gender"] = OTB_map["Gender"][tag[1]]
        self.features["Number"] = OTB_map["Number"][tag[2]]
        self.features["Case"] = OTB_map["Case"][tag[3]]
        return self

    def _numeral_features(self, tag):
        self.features["NumType"] = OTB_map["NumType"][tag[1]]
        if len(tag) > 2:
            self.features["Gender"] = OTB_map["Gender"][tag[2]]
            self.features["Number"] = OTB_map["Number"][tag[3]]
            self.features["Case"] = OTB_map["Case"][tag[4]]
        return self

    def _verb_features(self, tag):
        if tag[1] not in {"s", "þ", "l", "n"}:
            self.features["Mood"] = OTB_map["Mood"][tag[1]]
            self.features["Voice"] = OTB_map["Voice"][tag[2]]
            self.features["Person"] = OTB_map["Person"][tag[3]]
            self.features["Number"] = OTB_map["Number"][tag[4]]
            self.features["Tense"] = OTB_map["Tense"][tag[5]]
            self.features["VerbForm"] = OTB_map["VerbForm"][""]
        elif tag[1] in {"þ", "l"}:
            self.features["VerbForm"] = OTB_map["VerbForm"][tag[1]]
            self.features["Voice"] = OTB_map["Voice"][tag[2]]
            if tag[1] == "þ":
                self.features["Gender"] = OTB_map["Gender"][tag[3]]
                self.features["Number"] = OTB_map["Number"][tag[4]]
                self.features["Case"] = OTB_map["Case"][tag[5]]
        else:
            self.features["VerbForm"] = OTB_map["VerbForm"][tag[1]]
            self.features["Voice"] = OTB_map["Voice"][tag[2]]
        return self

    def _adverb_features(self, tag):
        if tag[-1] in {"m", "e"}:
            if len(tag) == 2:
                return self
            else:
                self.features["Degree"] = OTB_map["Degree"][tag[-1]]
        return self

    def _other_features(self, tag):
        if tag[0] == "e":
            self.features["Foreign"] = "Yes"

    def _get_features(self, tag):
        self.methods.get(tag[0], lambda x: "x")(tag)
        self.features.setAll_features()
        return self

    # Here follow methods for finding a word's UD-tag from its IcePaHC tag

    @staticmethod
    def get_UD_tag(tag):
        """ """
        if "-" in tag:
            tag = tag.split("-")[0]
        try:
            tag = UD_map[tag]
            return tag
        except:
            # raise
            if re.search(r"(DO|DA|RD|RA)", tag[0:2]):
                tag = "VERB"  # ATH. merkt sem sögn í bili
                return tag
            elif re.search(r"(BE|BA|HV|HA|MD|MA)", tag[0:2]):
                tag = "AUX"
                return tag
            elif tag == "CONJ":
                tag = "CCONJ"
                return tag
            elif tag in string.punctuation:
                tag = "PUNCT"
                return tag
            else:
                tag = UD_map.get(tag[0], "X")
                return tag

    @staticmethod
    def tagged_sent(sent):
        """
        Calls tagging API from http://malvinnsla.arnastofnun.is/about_en

        Arguments:
            dgraph: UniversalDependencyGraph
        Returns:
            type: .

        """
        try:
            url = "http://malvinnsla.arnastofnun.is"
            payload = {"text": decode_escaped(sent), "lemma": "on"}
            headers = {}
            res = requests.post(url, data=payload, headers=headers)
            tagged = json.loads(res.text)
            return {
                pair["word"]: (pair["tag"], pair["lemma"])
                for pair in [j for i in tagged["paragraphs"][0]["sentences"] for j in i]
            }
        except:
            raise FeatureExtractionError(
                "Tags could not be retrieved. Possibly no internet connection"
            )

    # @staticmethod
    # def tagged_corpus(sent_list):
    #     try:
    #         url = 'http://malvinnsla.arnastofnun.is'
    #         payload = {'text':sent, 'lemma':'on'}
    #         headers = {}
    #         res = requests.post(url, data=payload, headers=headers)
    #         tagged = json.loads(res.text)
    #         return {pair['word']:(pair['tag'],pair['lemma']) for pair in tagged['paragraphs'][0]['sentences'][0]}
    #     except:
    #         raise FeatureExtractionError('Tags could not be retrieved. Possibly no internet connection')


class FeatureExtractionError(Exception):
    """docstring for ."""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "FeatureExtractionError: {0}".format(self.message)
        else:
            return "FeatureExtractionError has been raised"


class ICE_Features:
    def __init__(self, tag):
        self.tag = tag
        self.features = {}

    def _noun_features(self, tag):
        if "-" in tag:
            tag, case = tag.split("-")
            try:
                self.features["Case"] = Icepahc_feats["NOUN"]["Case"][case]
            except KeyError:
                print(tag)
                raise
        self.features["Number"] = Icepahc_feats["NOUN"]["Number"][tag]
        if "$" in tag:
            self.features["Definite"] = Icepahc_feats["NOUN"]["Definite"]["$"]
        else:
            self.features["Definite"] = Icepahc_feats["NOUN"]["Definite"][""]
        return self.features

    def _adjective_features(self, tag):
        if "-" in tag:
            tag, case = tag.split("-")
            self.features["Case"] = Icepahc_feats["ADJ"]["Case"][case]
        if len(tag) > 3:
            if tag.startswith("W") and len(tag) > 4:
                self.features["Degree"] = Icepahc_feats["ADJ"]["Degree"][tag[4]]
            elif not tag.startswith("W"):
                self.features["Degree"] = Icepahc_feats["ADJ"]["Degree"][tag[3]]
        else:
            self.features["Degree"] = Icepahc_feats["ADJ"]["Degree"]["P"]
        return self.features

    def _pronoun_features(self, tag):
        if "-" in tag:
            case = tag.split("-")[1]
            if case not in {"1", "2", "3", "4", "5", "6", "TTT"}:
                try:
                    self.features["Case"] = Icepahc_feats["Case"][case]
                except KeyError:
                    print(tag)
                    raise
            return self.features
        if tag.startswith("OTHERS"):
            self.features["Number"] = Icepahc_feats["PRON"]["Number"]["S"]
        elif tag.startswith("OTHER"):
            self.features["Number"] = Icepahc_feats["PRON"]["Number"][""]

    def _determiner_features(self, tag):
        if "-" in tag:
            tag, case = tag.split("-")
            if case != "ADV":
                self.features["Case"] = Icepahc_feats["Case"][case]
            # if tag == "D":
            #    self.features["PronType"] = "Art"
            elif tag == "ONES":
                self.features["Number"] = Icepahc_feats["DET"]["Number"]["S"]
            elif tag.startswith("Q"):
                if tag.startswith("Q"):
                    self.features["Degree"] = Icepahc_feats["DET"]["Degree"][""]
                else:
                    self.features["Degree"] = Icepahc_feats["DET"]["Degree"][tag]
            else:
                self.features["Number"] = Icepahc_feats["DET"]["Number"][""]
        else:
            # if tag == "D":
            #    self.features["PronType"] = "Art"
            if tag == "ONES":
                self.features["Number"] = Icepahc_feats["DET"]["Number"]["S"]
            elif tag.startswith("Q"):
                if tag.startswith("Q"):
                    self.features["Degree"] = Icepahc_feats["DET"]["Degree"][""]
                else:
                    self.features["Degree"] = Icepahc_feats["DET"]["Degree"][tag]
            else:
                self.features["Number"] = Icepahc_feats["DET"]["Number"][""]
        return self.features

    def _numeral_features(self, tag):
        if "-" in tag:
            case = tag.split("-")[1]
            tag = tag.split("-")[0]
            if case != "1":
                self.features["Case"] = Icepahc_feats["Case"][case]
        return self.features

    def _verb_features(self, tag):
        if "-" in tag:
            case = tag.split("-")[1]
            tag = tag.split("-")[0]
            if case not in {"TTT", "3", "1", "2", "4"}:
                try:
                    self.features["Case"] = Icepahc_feats["Case"][case]
                except KeyError:
                    print(tag, case)
                    raise
        if len(tag) < 3:
            self.features["VerbForm"] = Icepahc_feats["VERB"]["VerbForm"]["inf"]
        elif len(tag) == 4:
            self.features["Tense"] = Icepahc_feats["VERB"]["Tense"][tag[2]]
            if tag != "VBDP":
                self.features["Mood"] = Icepahc_feats["VERB"]["Mood"][tag[3]]
        elif len(tag) == 3:
            try:
                self.features["VerbForm"] = Icepahc_feats["VERB"]["VerbForm"][tag[2]]
            except:
                print(tag)
                raise
            if tag[2] == "N":
                self.features["Tense"] = Icepahc_feats["VERB"]["Tense"]["D"]
            elif tag[2] == "G":
                self.features["Tense"] = Icepahc_feats["VERB"]["Tense"]["P"]
            if tag[2] == "I":
                self.features["Mood"] = Icepahc_feats["VERB"]["Mood"]["IMP"]
        return self.features

    def _adverb_features(self, tag):
        if "-" in tag:
            case = tag.split("-")[1]
            tag = tag.split("-")[0]
            if case not in {"1", "2", "3", "5", "10", "XXX"}:
                try:
                    self.features["Case"] = Icepahc_feats["ADV"]["Case"][case]
                except KeyError:
                    print(tag)
                    raise
            if len(tag) > 3 and tag not in {"ALSO", "WADV", "WADVP"}:
                try:
                    self.features["Degree"] = Icepahc_feats["ADV"]["Degree"][tag[3]]
                except KeyError:
                    print(tag)
                    raise
            else:
                self.features["Degree"] = Icepahc_feats["ADV"]["Degree"]["P"]
        else:
            if len(tag) > 3 and tag not in {"ALSO", "WADV"}:
                try:
                    self.features["Degree"] = Icepahc_feats["ADV"]["Degree"][tag[3]]
                except KeyError:
                    print(tag)
                    raise
            else:
                self.features["Degree"] = Icepahc_feats["ADV"]["Degree"]["P"]
        return self.features

    def _foreign_features(self, tag):
        self.features["Foreign"] = "Yes"
        return self.features

    def _es_features(self, tag):
        self.features["Gender"] = "Neut"
        self.features["Case"] = "Nom"
        self.features["Number"] = "Sing"
        return self.features

    def _other_features(self, tag):
        return self.features

    def get_features(self):
        word = self.tag[0:3]
        verbal_prefixes = [
            "VB",
            "VA",
            "BE",
            "BA",
            "DO",
            "DA",
            "HV",
            "HA",
            "MD",
            "RD",
            "RA",
        ]
        det_prefixes = ["D", "WD", "Q", "QR"]
        if word == "ADJ" or self.tag.startswith("WADJ"):
            return self._adjective_features(self.tag)
        elif word in {"PRO", "SUC", "WPR", "OTH"}:
            return self._pronoun_features(self.tag)
        elif word == "NUM":
            return self._numeral_features(self.tag)
        elif word.startswith("N") and word != "NEG" and word[0:2] != "NP":
            return self._noun_features(self.tag)
        elif word.startswith(tuple(verbal_prefixes)):
            return self._verb_features(self.tag)
        elif word.startswith(tuple(det_prefixes)) or word == "ONE":
            return self._determiner_features(self.tag)
        elif word in {"ADV", "WAD", "ALSO"} or word.startswith("FP"):
            return self._adverb_features(self.tag)
        elif word.startswith("FW"):
            return self._foreign_features(self.tag)
        elif word.startswith("ES"):
            return self._es_features(self.tag)
        else:
            return self._other_features(self.tag)
