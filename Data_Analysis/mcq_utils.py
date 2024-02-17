import copy
import csv
import json
import logging
import os
import spacy
import en_core_web_lg
from nltk import sent_tokenize
from mcq_parameters import dataset_names, save_data_path

tokenizer = spacy.load("en_core_web_lg")

def get_vocabulary(text_list):
    s, avg_tokens = 0, 0
    vocabulary = set()
    for text in text_list:
        try:
            tokens = tokenizer(text)
            vocabulary.update({x.lemma_.lower() for x in tokens})
        except UnicodeEncodeError:
            print("Unicode error happens")
            tokens = text.split()
        s = s + len(tokens)
    if len(text_list) > 0:
        avg_tokens = s / len(text_list)
    return "{:.1f}".format(avg_tokens), vocabulary


def write_vocabulary(vocabulary, taskname):
    dataset = dataset_names[taskname]
    vocabulary_path = os.path.join(save_data_path, "Vocabulary")
    if not os.path.exists(vocabulary_path):
        os.makedirs(vocabulary_path)
    vocabulary_file_name = os.path.join(vocabulary_path, "{}.txt".format(dataset))
    try:
        vocabulary_file = open(vocabulary_file_name, "w",  encoding="utf-8")
        for v in sorted(vocabulary):
            string_out = v + "\n"
            vocabulary_file.write(string_out)
    except UnicodeEncodeError as e:
        print("UnicodeEncodeError: {}".format(e))
    except Exception as e:
       print("An unexpected error occurred: {}".format(e))
    vocabulary_file.close()

def write_questions(question_list, taskname):
    dataset = dataset_names[taskname]
    path = os.path.join(save_data_path, "Questions")
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = os.path.join(path, "{}.txt".format(dataset))
    file = open(file_name, "w", encoding='utf-8')
    for v in question_list:
        string_out = v + "\n"
        file.write(string_out)
    file.close()
    
def write_cloze_questions(question_list, taskname):
    dataset = dataset_names[taskname]
    path = os.path.join(save_data_path, "Cloze_Questions")
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = os.path.join(path, "{}.txt".format(dataset))
    file = open(file_name, "w", encoding='utf-8')
    for v in question_list:
        string_out = v + "\n"
        file.write(string_out)
    file.close()
    
def write_sentence_questions(question_list, taskname):
    # print("writing vocabulary...")
    dataset = dataset_names[taskname]
    path = os.path.join(save_data_path, "Sentence_Questions")
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = os.path.join(path, "{}.txt".format(dataset))
    file = open(file_name, "w", encoding='utf-8')
    for v in question_list:
        string_out = v + "\n"
        file.write(string_out)
    file.close()
    
def write_other_questions(question_list, taskname):
    dataset = dataset_names[taskname]
    path = os.path.join(save_data_path, "Other_Questions")
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = os.path.join(path, "{}.txt".format(dataset))
    file = open(file_name, "w", encoding='utf-8')
    for v in question_list:
        string_out = v + "\n"
        file.write(string_out)
    file.close()
    
def write_options(option_list, taskname):
    dataset = dataset_names[taskname]
    path = os.path.join(save_data_path, "Options")
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = os.path.join(path, "{}.txt".format(dataset))
    file = open(file_name, "w", encoding='utf-8')
    for v in option_list:
        string_out = str(v) + "\n"
        file.write(string_out)
    file.close()

def write_passage(passage_list, taskname):
    dataset = dataset_names[taskname]
    path = os.path.join(save_data_path, "Passages")
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = os.path.join(path, "{}.txt".format(dataset))
    file = open(file_name, "w", encoding='utf-8')
    for v in passage_list:
        string_out = v + "\n\n\n"
        file.write(string_out)
    file.close()


def get_all_subfiles(folder, current_list, file_type):
    inside_files = os.listdir(folder)

    for file in inside_files:
        file_path = os.path.join(folder,file)
        if file_type in file:
            current_list.append(file_path)
        else:
            get_all_subfiles(file_path, current_list, file_type)
    return current_list



class DataProcessor(object):
    """Base class for data converters for sequence classification data sets."""


    def get_train_examples(self, data_dir):
        """Gets a collection of `InputExample`s for the train set."""
        raise NotImplementedError()

    def get_dev_examples(self, data_dir):
        """Gets a collection of `InputExample`s for the dev set."""
        raise NotImplementedError()

    def get_examples(self, data_dir, subset, debug_flag):
        """Gets a collection of `InputExample`s for the set."""
        raise NotImplementedError()

    def get_labels(self):
        """Gets the list of labels for this data set."""
        raise NotImplementedError()

    def get_passages(self):
        """Gets the list of all passages (docs) for this data set."""
        raise NotImplementedError()

    def get_questions(self):
        """Gets the list of all questions for this data set."""
        raise NotImplementedError()

    def get_answers(self):
        """Gets the list of all ansers and anser candidates for this data set."""
        raise NotImplementedError()

    def tfds_map(self, example):
        """Some tensorflow_datasets datasets are not formatted the same way the GLUE datasets are.
        This method converts examples to the correct format."""
        if len(self.get_labels()) > 1:
            example.label = self.get_labels()[int(example.label)]
        return example

    @classmethod
    def _read_tsv(cls, input_file, quotechar=None):
        """Reads a tab separated value file."""
        with open(input_file, "r", encoding="utf-8-sig") as f:
            return list(csv.reader(f, delimiter="\t", quotechar=quotechar))


