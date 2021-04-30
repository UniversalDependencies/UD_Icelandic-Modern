# Summary

UD_Icelandic-Modern is a conversion of the modern additions to the Icelandic Parsed Historical Corpus (IcePaHC) to the Universal Dependencies scheme.

The conversion was done using [UDConverter](https://github.com/thorunna/UDConverter).


# Introduction

The modern additions to the Icelandic Parsed Historical Corpus (IcePaHC) is a 92,939 word corpus which includes texts from the 21st century. These texts were originally manually parsed according to the Penn Parsed Corpora of Historical English (PPCHE) annotation scheme, as used in IcePaHC. These parsed texts were then automatically converted to the Universal Dependencies scheme to create UD_Icelandic-Modern. The texts are unprepared parliament speeches by four Icelandic members of parliament in the period 2011–2015 and sports news text from two reporters at the Icelandic National Broadcasting Service (RÚV) from 2016.

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

72,917 words in total

- `ALTHINGI_BO_2013` - 16 sentences
- `ALTHINGI_BO_2014` - 174 sentences
- `ALTHINGI_BO_2015` - 284 sentences
- `ALTHINGI_HHG_2013` - 1215 sentences
- `ALTHINGI_SJS_2013` - 1458 sentences
- `ALTHINGI_TKG_2011` - 992 sentences
- `RUV_ESP_2016` - 580 sentences
- `RUV_TGS_2016` - 657 sentences

**Development data**

10,007 words in total

  - `ALTHINGI_BO_2013` - 16 sentences
  - `ALTHINGI_BO_2014` - 43 sentences
  - `ALTHINGI_BO_2015` - 284 sentences
  - `ALTHINGI_HHG_2013` - 192 sentences
  - `ALTHINGI_SJS_2013` - 75 sentences
  - `ALTHINGI_TKG_2011` - 53 sentences
  - `RUV_ESP_2016` - 66 sentences
  - `RUV_TGS_2016` - 55 sentences


**Testing data**

10,015 words in total

- `ALTHINGI_BO_2013` - 60
- `ALTHINGI_BO_2014` - 309
- `ALTHINGI_BO_2015` - 132
- `ALTHINGI_HHG_2013` - 45
- `ALTHINGI_SJS_2013` - 67
- `ALTHINGI_TKG_2011` - 41
- `RUV_ESP_2016` - 38
- `RUV_TGS_2016` - 76


# Acknowledgments

This project was funded by The Strategic Research and Development Programme for Language Technology, grant no. 180020-5301.

The modern additions to the Icelandic Parsed Historical Corpus (IcePaHC) are available [here](https://github.com/antonkarl/icecorpus/tree/master/finished/additions2019).

Morphological features were generated using ABLTagger, a PoS tagger for Icelandic, developed by Steinþór Steingrímsson, Örvar Kárason and Hrafn Loftsson and available [here](https://github.com/steinst/ABLTagger).


# Changelog

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
