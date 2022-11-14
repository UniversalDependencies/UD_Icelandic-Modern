import os

# open a text file
def open_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    # blanket replace all None with "_" in the conllu
    contents = contents.replace("None", "_")
    return contents


# make directory if it doesnt exist
def make_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# write output to a file
def write_file(filename, contents):
    with open(filename, "w") as f:
        f.write(contents)


# get all sentences from a conllu file, split by empty lines
def get_sentences(filename):
    return open_file(filename).split("\n\n")


# get the texts in the original input files
def get_texts(filename):
    return open_file(filename).split("\n")


# gather filenames
def get_all_filenames():
    return os.listdir("to_fix")


# get the filenames that should be marked ESP
def get_edda_filenames():
    return os.listdir("originals/edda")


# check whether should be ESP or TGS
def check_if_esp(filename):
    if filename in edda_files:
        return True
    else:
        return False


# create the metadata as a whole and return as string
def create_metadata(sentence_index, sentence_text, filename, is_esp):
    speaker = "ESP" if is_esp else "TGS"
    return "\n".join(
        [
            f"# sent_id = RUV_{speaker}_2017_{os.path.splitext(filename)[0]},{str(sentence_index+1)}.",
            f"# X_ID = ID_MISSING",
            f"# text = {sentence_text}",
        ]
    )


# combine the metadata and the conllu sentence
def add_metadata_to_sentences(sentences, filename, is_esp, texts):
    return [
        create_metadata(i, texts[i], filename, is_esp) + "\n" + sentence
        for i, sentence in enumerate(sentences)
        if sentence != ""
    ]


if __name__ == "__main__":
    make_dir_if_not_exists("fixed")
    filenames = get_all_filenames()
    edda_files = get_edda_filenames()
    all_sents = []
    for filename in filenames:
        sentences = get_sentences("to_fix/" + filename)
        texts = get_texts("originals/" + filename)
        new_sentences = add_metadata_to_sentences(
            sentences, filename, check_if_esp(filename), texts
        )
        all_sents.extend(new_sentences)
    write_file("additions-with-metadata.conllu", "\n\n".join(all_sents))
