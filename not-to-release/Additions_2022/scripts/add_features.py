import pyconll

from features import Features, ICE_Features

# a function to write the output to a file
def write_to_conllu(conllu_file, conll):
    with open(conllu_file, 'w', encoding='utf-8') as f:    
        for sentence in conll:
            print(sentence.conll())
            f.write(sentence.conll())
            f.write('\n\n')

# a function to make all values in a dictionary a set of strings, if dictionary has items
def make_sets(d):
    for k, v in d.items():
        # print(k,v)
        if v:
            d[k] = set((v,))
        
    return d

# a function to add info to a misc column in a conllu file token
def make_misc_column(token, tag, sentence):
    misc = {}
    misc['IFD_tag'] = set((tag,))
    
    if len(sentence) != int(token.id) and sentence[str(int(token.id)+1)].upos == 'PUNCT':
        misc['SpaceAfter'] = set(('No',))
    return filter_none_values(misc)

# a function to filter out None values in a dictionary
def filter_none_values(d):
    return {k: v for k, v in d.items() if v is not None}

if __name__ == '__main__':
    
    # load the conllu file
    conll = pyconll.load_from_file("additions-with-metadata.conllu")

    sent_num = len(conll)
    runner = 0
    # loop through the sentences
    for sentence in conll:
        runner += 1
        # the Features module used to tag the sentence as a whole 
        # (Note: ABLTagger 2018 is used to tag the sentences)
        tag_dict = Features.tagged_sent(sentence.text)
        for token in sentence:
            ifd_tag = tag_dict.get(token.form, "x")[0]
            # the ICE_Features module used when ABLTagger 2018 is not able to tag a token
            if ifd_tag == "x":
                feats = ICE_Features(token.xpos).get_features()
            else:
                feats = Features(ifd_tag).features
            # overwrite the original features
            token.feats = filter_none_values(make_sets(dict(feats)))
            # overwrite the original misc column
            token.misc = make_misc_column(token, ifd_tag, sentence)
            
        #     print(token.id, token.form, token.lemma, token.upos, token.xpos, token.feats, token.head, token.deprel, token.deps, token.misc)
        # input()
        
        # print the progress
        print(f"Processed sentence {runner} of {sent_num}", end='\r')
    
    # write the new conllu file
    write_to_conllu("additions-with-features.conllu", conll)