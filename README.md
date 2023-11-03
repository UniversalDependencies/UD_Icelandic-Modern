# Summary

UD_Icelandic-Modern is a conversion of the [modern additions](https://github.com/antonkarl/icecorpus/tree/master/finished/additions2019) to the Icelandic Parsed Historical Corpus (IcePaHC) to the Universal Dependencies scheme.


# Introduction

The conversion was done using [UDConverter](https://github.com/thorunna/UDConverter).

Note that the treebank data in versions 2.8-2.10 is flawed in that various sentences are duplicated, resulting in an overlap between train / dev / test. This issue has been fixed as of version 2.11.

The modern additions to the Icelandic Parsed Historical Corpus (IcePaHC) is a corpus which includes texts from the 21st century, NOT found in [IcePaHC](https://repository.clarin.is/repository/xmlui/handle/20.500.12537/62). These texts were originally manually parsed according to the Penn Parsed Corpora of Historical English (PPCHE) annotation scheme as used for IcePaHC. These parsed texts were then automatically converted to the Universal Dependencies scheme to create UD_Icelandic-Modern. The corpus consists of 80,395 tokens in total. The texts are unprepared parliament speeches by four Icelandic members of parliament in the period 2011–2015 and sports news texts from two reporters at the Icelandic National Broadcasting Service (RÚV) from 2016 and – as of version 2.11 – from 2017. These 21st-century additions are not found in [IcePaHC](https://repository.clarin.is/repository/xmlui/handle/20.500.12537/62) (which, however, contains two narrative texts from the 21st century).

Each sentence ID (`sent_id`) in UD_Icelandic-Modern carries the following information:

`ALTHINGI_BO_2015_G-33-4647803,.1`

- Text origin (`ALTHINGI`)
- Speaker (`BO`)
- Publication year of the text (`2015`)
- Name of original file (`G-33-4647803`)
- Sentence index within file (`.1`)

Along with sentence IDs within the UD corpus, each sentence contains an `X_ID` flag, indicating the original sentence(s) in IcePaHC. This is useful as some sentences in the UD scheme have more than one original sentence in IcePaHC. As sentence IDs are currently not represented in the modern-text IcePaHC, this flag is left blank, as `ID_MISSING` for each original sentence.


## Manually corrected portion

A subset of the UD corpus has been manually corrected after the automatic conversion, 15,151 words in total. The portion corrected belonged to the following files, as shown in each sentence's ID:
- `ALTHINGI_BO_2013`
  - All files
- `ALTHINGI_BO_2014`
  -  All files
- `ALTHINGI_HHG_2013`
  - Files G-33-4492074, G-33-4497471, G-33-4500256, G-33-4525575, G-33-4528305, G-33-4534200, G-33-4542329
- `ALTHINGI_SJS_2013`
  -  Files G-33-4493268, G-33-4496708, G-33-4496709, G-33-4496710, G-33-4500290, G-33-4500291, G-33-4503791, G-33-4510804, G-33-4517845, G-33-4517846, G-33-4524841, G-33-4528340, G-33-4542311, G-33-4542313, G-33-4545749, G-33-4545750, G-33-4545751, G-33-4556342, G-33-4556344, G-33-4563267, G-33-4565680

## Data split

**Training data**

61,817 words in total

- `ALTHINGI_BO_2013` - 16 sentences
- `ALTHINGI_BO_2014` - 174 sentences
- `ALTHINGI_BO_2015` - 284 sentences
- `ALTHINGI_HHG_2013` - 621 sentences
- `ALTHINGI_SJS_2013` - 658 sentences
- `ALTHINGI_TKG_2011` - 449 sentences
- `RUV_ESP_2016` - 238 sentences
- `RUV_TGS_2016` - 263 sentences

**Development data**

8,431 words in total

- `ALTHINGI_BO_2013` - 16 sentences
- `ALTHINGI_BO_2014` - 43 sentences
- `ALTHINGI_BO_2015` - 32 sentences
- `ALTHINGI_HHG_2013` - 54 sentences
- `ALTHINGI_SJS_2013` - 75 sentences
- `ALTHINGI_TKG_2011` - 53 sentences
- `RUV_ESP_2016` - 66 sentences
- `RUV_TGS_2016` - 55 sentences

**Testing data**

10,147 words in total

- `ALTHINGI_BO_2013` - 14 sentences
- `ALTHINGI_BO_2014` - 46 sentences
- `ALTHINGI_BO_2015` - 34 sentences
- `ALTHINGI_HHG_2013` - 45 sentences
- `ALTHINGI_SJS_2013` - 67 sentences
- `ALTHINGI_TKG_2011` - 41 sentences
- `RUV_ESP_2016` - 38 sentences
- `RUV_ESP_2017` - 43 sentences
- `RUV_TGS_2016` - 76 sentences
- `RUV_TGS_2017` - 34 sentences


# Acknowledgments

This project was funded by The Strategic Research and Development Programme for Language Technology, grant no. 180020-5301.

The modern additions to the Icelandic Parsed Historical Corpus (IcePaHC) are available [here](https://github.com/antonkarl/icecorpus/tree/master/finished/additions2019).

Morphological features were generated using ABLTagger, a PoS tagger for Icelandic, developed by Steinþór Steingrímsson, Örvar Kárason and Hrafn Loftsson and available [here](https://github.com/steinst/ABLTagger).


# Changelog

* 2023-11-15 v2.13
  * A few feature fixes.
* 2023-05-15 v2.12
  * Deprels for 'en', 'meðan' and 'uns' changed from `case` to `mark`.
  * Some systematic discrepancies between UPOS and universal features/IFD tags fixed.
  * Some lemma fixes.
* 2022-11-15 v2.11
  * Duplicate sentences removed.
  * Texts labeled `RUV_TGS_2017` and `RUV_ESP_2017` added to testing data; these were parsed with [COMBO-based UD Parser 22.10](https://repository.clarin.is/repository/xmlui/handle/20.500.12537/272) and the output subsequently corrected.
  * Validation errors fixed (too many subjects).
  * Deprels for 'þegar', 'ef', 'nema', 'þótt' and 'þó' changed from `case` to `mark`.
  * Some lemma fixes.

* 2021-05-15 v2.8
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.8
License: CC BY-SA 4.0
Includes text: yes
Genre: nonfiction news
Lemmas: converted from manual
UPOS: converted from manual
XPOS: manual native
Features: converted from manual
Relations: converted from manual
Contributors: Rúnarsson, Kristján; Arnardóttir, Þórunn; Hafsteinsson, Hinrik; Barkarson, Starkaður; Jónsdóttir, Hildur; Steingrímsson, Steinþór; Sigurðsson, Einar Freyr
Contributing: elsewhere
Contact: krunars@gmail.com, thar@hi.is, hinrik.hafst@gmail.com, starkadur.barkarson@arnastofnun.is, hildur.jonsdottir@gmail.com, steinthor.steingrimsson@arnastofnun.is, einar.freyr.sigurdsson@arnastofnun.is
===============================================================================
</pre>
