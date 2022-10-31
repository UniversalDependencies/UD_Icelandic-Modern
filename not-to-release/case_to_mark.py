import pyconll

dev = "../is_modern-ud-dev.conllu"
test = "../is_modern-ud-test.conllu"
train = "../is_modern-ud-train.conllu"

corpus = pyconll.load_from_file(test)

for sentence in corpus:
    for token in sentence:
        if (
            token.lemma in {"þegar", "ef", "nema", "þótt", "þó"}
            and token.upos == "ADP"
            and token.deprel == "case"
        ):
            if sentence[token.head].deprel != "root":
                sentence[token.head].deprel = "advcl"
            token.deprel = "mark"
            token.upos = "SCONJ"

with open(test, "w", encoding="utf-8") as f:
    for sentence in corpus:
        f.write("# sent_id = ")
        f.write(sentence.meta_value("sent_id"))
        f.write("\n")
        sentence.remove_meta("sent_id")
        if sentence.meta_present("X_ID"):
            f.write("# X_ID = ")
            f.write(sentence.meta_value("X_ID"))
            sentence.remove_meta("X_ID")
        elif sentence.meta_present("X_IDs"):
            f.write("# X_IDs = ")
            f.write(sentence.meta_value("X_IDs"))
            sentence.remove_meta("X_IDs")
        f.write("\n")
        f.write(sentence.conll())
        f.write("\n\n")
