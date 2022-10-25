import pyconll

# a function to write the output to a file
def write_to_conllu(conllu_file, conll):
    with open(conllu_file, 'w', encoding='utf-8') as f:    
        for sentence in conll:
            # print(sentence.conll())
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
def make_misc_column(token, sentence):
    NO_SPACE_AFTER = "„-/("
    NO_SPACE_BEFORE = "-%/,.“”):?!"
    misc = {}
    
    # check for known tokens that should not have a space before
    if len(sentence) != int(token.id) and sentence[str(int(token.id)+1)].form in NO_SPACE_BEFORE:
        misc['SpaceAfter'] = set(('No',))
    # check for known tokens that should not have a space after
    if token.form in NO_SPACE_AFTER:
        misc['SpaceAfter'] = set(('No',))
    if token.form == '-' and ' - ' in sentence.text:
        misc = {}
    if len(sentence) != int(token.id) and sentence[str(int(token.id)+1)].form == '-' and ' - ' in sentence.text:
        misc = {}
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
        for token in sentence:
            token.misc = make_misc_column(token, sentence)
            
        #     print(token.id, token.form, token.lemma, token.upos, token.xpos, token.feats, token.head, token.deprel, token.deps, token.misc)
        # input()
        
        # print the progress
        print(f"Processed sentence {runner} of {sent_num}", end='\r')
    
    # write the new conllu file
    write_to_conllu("additions-with-misc.conllu", conll)