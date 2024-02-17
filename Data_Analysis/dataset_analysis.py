import argparse
import re
from mcq_utils import get_vocabulary
from mcq_parameters import datapaths, dataset_names
from mcq_processors import processors
from mcq_write_documents import write_documents

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "task_name",
        default=None,
        type=str,
        help="The name of the task to train selected in the list: " + ", ".join(processors.keys()))

    args = parser.parse_args()
    args.task_name = args.task_name.lower()
    if args.task_name not in processors:
        raise ValueError("Task not found: %s" % (args.task_name)) 
    processor = processors[args.task_name]()
    datapath = datapaths[args.task_name]
    data = processor.get_all_examples(datapath, False)

    print("\tData Collected: Passage, Query, Options")
    if args.task_name not in ["recipeqa"]:
        questions = data["questions"]
        passages  = data["passages"]
        options   = data["answers"]
    else:
        passages  = data["passages"]
        questions = questions["textual_cloze"]
        options   = data["answers"]
       
    print("\tData Average Length an Vocabulary Size")
    avg_p, avg_q, avg_o = 0,0,0
    vocab_p, vocab_q, vocab_o = [],[],[]
    vocabulary = set()
    
    if len(passages) > 0:
        avg_p, vocab_p = get_vocabulary(passages)
        vocabulary.update(vocab_p)
        print("Vocab P size:", len(vocab_p))

    if len(questions) > 0:
        avg_q, vocab_q = get_vocabulary(questions)
        vocabulary.update(vocab_q)
        print("Vocab Q size:", len(vocab_q))

    if len(options) > 0:
        avg_o, vocab_o = get_vocabulary(options)
        vocabulary.update(vocab_o)
        print("Vocab O size:", len(vocab_o))

    print("\tDataset Size :")
    print("Number of Questions:", len(questions))
    print("Number of Passages:", len(passages))
    print("Dataset VOCAB size:", len(vocabulary))
    
    print("\tAverage Length :")
    print("AVG P len:", avg_p)
    print("AVG Q len:", avg_q)
    print("AVG A len:", avg_o)
    
    print("\tVocabulary Size : ")
    print("Vocab P size:", len(vocab_p))
    print("Vocab Q size:", len(vocab_q))
    print("Vocab O size:", len(vocab_o))

    print("\t Write Information")
    write_documents(passages, questions, options, vocabulary , args.task_name)

if __name__ == "__main__":
    main()