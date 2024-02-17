import json
import os
import csv
import gzip
import jsonlines
import re
from xml.dom import minidom
import pandas as pd
from tqdm import tqdm
from mcq_utils import DataProcessor, write_vocabulary, get_all_subfiles


# Cloze - FITB - Datasets (CLOTH, CLOTH-M, CLOTH-H, SCDE, DGen, CELA)
# CLOTH dataset
class CLOTHProcessor(DataProcessor):
    def get_all_examples(self, data_dir, debug_flag):
       passage_list, answer_list = [], []
       all_files_list = get_all_subfiles(data_dir, [], ".json")
       for file in all_files_list:
           with open(file, "r") as reader:
               input_data = json.load(reader)
               passage = input_data["article"].replace("\n", " ")
               passage_list.append(passage)
               answer_options = input_data["options"]
               for options in answer_options:
                   answer_list+=options

       return {"questions": [],
               "passages": passage_list,
               "answers": answer_list}
   
# CLOTH-M dataset
class CLOTHHProcessor(DataProcessor):
    def get_all_examples(self, data_dir, debug_flag):
       passage_list, answer_list = [], []
       all_files_list = get_all_subfiles(data_dir, [], ".json")
       for file in all_files_list:
           with open(file, "r") as reader:
               input_data = json.load(reader)
               passage = input_data["article"].replace("\n", " ")
               passage_list.append(passage)
               answer_options = input_data["options"]
               for options in answer_options:
                   answer_list+=options
           
       return {"questions": [],
               "passages": passage_list,
               "answers": answer_list}

# CLOTH-H dataset
class CLOTHMProcessor(DataProcessor):   
    def get_all_examples(self, data_dir, debug_flag):
       passage_list, answer_list = [], []
       all_files_list = get_all_subfiles(data_dir, [], ".json")
       for file in all_files_list:
           with open(file, "r") as reader:
               input_data = json.load(reader)
               passage = input_data["article"].replace("\n", " ")
               passage_list.append(passage)
               answer_options = input_data["options"]
               for options in answer_options:
                   answer_list+=options

       return {"questions": [],
               "passages": passage_list,
               "answers": answer_list}
   
# SCDE dataset
class SCDEProcessor(DataProcessor):
   def get_all_examples(self, data_dir, debug_flag):
       train_data = self._read_questions_examples(data_dir, "train", debug_flag)
       dev_data   = self._read_questions_examples(data_dir,  "dev", debug_flag)
       test_data  = self._read_questions_examples(data_dir,  "test", debug_flag)
       answer_list   = train_data["answers"]   + dev_data["answers"]   + test_data["answers"]
       passage_list  = train_data["passages"]  + dev_data["passages"]  + test_data["passages"]
       
       return {"questions": [],
               "passages": passage_list,
               "answers": answer_list}


   def _read_questions_examples(self, data_dir, sub_set, debug_flag):
       passage_list, answer_list = [], []
       input_file = os.path.join(data_dir, "{}.json".format(sub_set))
       with open(input_file, "r", encoding='utf-8') as reader:
           input_data = json.load(reader)
       for entry in input_data:
           passage = " ".join(entry['passage'])
           passage_list.append(passage)
           answer = " ".join(entry['candidates'])
           for j in entry['candidates']:
               answer_list.append(j)

       return {"questions": [],
               "passages": passage_list,
               "answers": answer_list}
   
# DGen dataset
class DGENProcessor(DataProcessor):
    def get_all_examples(self, data_dir, debug_flag):
        test_data = self._read_questions_examples(data_dir, "total_new_cleaned_test", debug_flag)
        train_data   = self._read_questions_examples(data_dir,  "total_new_cleaned_train", debug_flag)
        question_list = train_data["questions"] + test_data["questions"]
        answer_list   = train_data["answers"]  + test_data["answers"]

        return {"questions": question_list,
                "passages": [],
                "answers": answer_list}

    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, answer_list = [], []
        input_file = os.path.join(data_dir, "{}.json".format(sub_set))
        with open(input_file, "r", encoding='utf-8') as reader:
            input_data = json.load(reader)
        for entry in input_data:
            question = entry["sentence"]
            question_list.append(question)
            answer = entry["answer"]
            answer_list += answer
            for item in entry['distractors']:
                answer_list.append(item)

        return {"questions": question_list,
                "passages": [],
                "answers": answer_list}    

# CELA dataset
class CELAProcessor(DataProcessor):
    
    def get_all_examples(self, data_dir, debug_flag):
        question_list, passage_list, answer_list = [], [], []
        all_files_list = get_all_subfiles(data_dir, [], ".json")
        for file in all_files_list:
            with open(file, "r") as reader:
                input_data = json.load(reader)
                for entry in input_data:
                    passage = input_data["article"].replace("\n", " ")
                    passage_list.append(passage)
                    answer_options = input_data["options"]
                    for options in answer_options:
                        answer_list+=options
        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

    
# Cloze - MCQ - Datasets (SciQ, OpenBookQA, ARC, ARC-Challange, ARC-Easy, CommonSenseQA, MCQL, QASC, Televic, EduQG) 
#SciQ dataset
class SciQProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        train_data = self._read_questions_examples(data_dir, "train", debug_flag)
        dev_data = self._read_questions_examples(data_dir, "valid", debug_flag)
        test_data = self._read_questions_examples(data_dir, "test", debug_flag)
        question_list = train_data["questions"] + dev_data["questions"] + test_data["questions"]
        answer_list = train_data["answers"] + dev_data["answers"] + test_data["answers"]
        passage_list = train_data["passages"] + dev_data["passages"] + test_data["passages"]
    
        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, answer_list, passage_list, instance_list = [], [], [], []
        input_file = os.path.join(data_dir, "{}.json".format(sub_set))

        with open(input_file, "r", encoding='utf-8') as reader:
            input_data = json.load(reader)

        for entry in input_data:
            passage = entry["support"].strip()
            passage_list.append(passage)
            question = entry["question"]
            question_list.append(question)
            answers = []
            answers.append(entry["distractor1"])
            answers.append(entry["distractor2"])
            answers.append(entry["distractor3"])
            answers.append(entry["correct_answer"])
            answer_list+=answers

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

#AQUA-RAT dataset
class AquaRatProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        train_data = self._read_questions_examples(data_dir, "train", debug_flag)
        dev_data = self._read_questions_examples(data_dir, "dev", debug_flag)
        test_data = self._read_questions_examples(data_dir, "test", debug_flag)
        question_list = train_data["questions"] + dev_data["questions"] + test_data["questions"]
        answer_list = train_data["answers"] + dev_data["answers"] + test_data["answers"]
        passage_list = train_data["passages"] + dev_data["passages"] + test_data["passages"]
    
        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, answer_list, passage_list = [], [], []
        input_file = os.path.join(data_dir, "{}.json".format(sub_set))

        with open(input_file, "r", encoding='utf-8') as reader:
            for line in reader:
                input_data = json.loads(line)
                passage = input_data["rationale"].replace("\n", " ")
                passage_list.append(passage)
                question = input_data["question"]
                question_list.append(question)
                answers = input_data["options"]
                for options in answers:
                    answer_list.append(options)

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

#OpenBookQA
class OpenBookQAProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        train_data = self._read_questions_examples(data_dir, "train", debug_flag)
        dev_data   = self._read_questions_examples(data_dir,  "dev", debug_flag)
        test_data  = self._read_questions_examples(data_dir,  "test", debug_flag)
        question_list   = train_data["questions"] + dev_data["questions"] + test_data["questions"]
        passage_list    = train_data["passages"] + dev_data["passages"] + test_data["passages"]
        answer_list     = train_data["answers"]   + dev_data["answers"]   + test_data["answers"]

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}


    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        examples = []
        question_list, passage_list, answer_list, instance_list = [], [], [], []
        input_file = "{}/{}_complete.jsonl".format(data_dir, sub_set)
        with jsonlines.open(input_file, "r") as reader:
            for entry in reader.iter():
                question = entry["question"]["stem"]
                question_list.append(question)
                answers = [x["text"] for x in entry["question"]["choices"]]
                answer_list =  answer_list + answers
                passage =  entry["fact1"]
                passage_list.append(passage)


        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}
    
#ARC
class ARCProcessor(DataProcessor):
    def get_all_examples(self, data_dir, debug_flag):
        train_data = self._read_questions_examples(data_dir, "Challenge-Train", debug_flag)
        dev_data   = self._read_questions_examples(data_dir,  "Challenge-Dev", debug_flag)
        test_data  = self._read_questions_examples(data_dir,  "Challenge-Test", debug_flag)
        train_data_easy = self._read_questions_examples(data_dir, "Easy-Train", debug_flag)
        dev_data_easy   = self._read_questions_examples(data_dir, "Easy-Dev", debug_flag)
        test_data_easy  = self._read_questions_examples(data_dir, "Easy-Test", debug_flag)


        question_list = train_data["questions"] + dev_data["questions"] + test_data["questions"] + train_data_easy["questions"] + dev_data_easy["questions"] + test_data_easy["questions"]
        answer_list   = train_data["answers"]   + dev_data["answers"]   + test_data["answers"]   + train_data_easy["answers"]   + dev_data_easy["answers"]   + test_data_easy["answers"]
                    
        return {"questions": question_list,
                "passages": [],
                "answers": answer_list}
    

    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, passage_list, answer_list, instance_list = [], [], [], []
        input_file = "{}/ARC-{}.jsonl".format(data_dir, sub_set)
        with jsonlines.open(input_file, "r") as reader:
            for entry in reader.iter():
                question = entry["question"]["stem"]
                question_list.append(question)
                answers = [x["text"] for x in entry["question"]["choices"]]
                answer_list += answers
                if debug_flag:
                    break

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}
#ARC- Challange   
class ARC_Challange_Processor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        train_data = self._read_questions_examples(data_dir, "Challenge-Train", debug_flag)
        dev_data   = self._read_questions_examples(data_dir,  "Challenge-Dev", debug_flag)
        test_data  = self._read_questions_examples(data_dir,  "Challenge-Test", debug_flag)

        question_list = train_data["questions"] + dev_data["questions"] + test_data["questions"] 
        answer_list   = train_data["answers"]   + dev_data["answers"]   + test_data["answers"]
                            
        return {"questions": question_list,
                "passages": [],
                "answers": answer_list}


    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, passage_list, answer_list, instance_list = [], [], [], []
        input_file = "{}/ARC-{}.jsonl".format(data_dir, sub_set)
        with jsonlines.open(input_file, "r") as reader:
            for entry in reader.iter():
                question = entry["question"]["stem"]
                question_list.append(question)
                answers = [x["text"] for x in entry["question"]["choices"]]
                answer_list += answers

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

#ARC-Easy    
class ARC_Easy_Processor(DataProcessor):
    def get_all_examples(self, data_dir, debug_flag):
        train_data_easy = self._read_questions_examples(data_dir, "Easy-Train", debug_flag)
        dev_data_easy   = self._read_questions_examples(data_dir, "Easy-Dev", debug_flag)
        test_data_easy  = self._read_questions_examples(data_dir, "Easy-Test", debug_flag)
        question_list =  train_data_easy["questions"] + dev_data_easy["questions"] + test_data_easy["questions"]
        answer_list   =  train_data_easy["answers"]   + dev_data_easy["answers"]   + test_data_easy["answers"]

        return {"questions": question_list,
                "passages": [],
                "answers": answer_list}


    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, passage_list, answer_list, instance_list = [], [], [], []
        input_file = "{}/ARC-{}.jsonl".format(data_dir, sub_set)
        with jsonlines.open(input_file, "r") as reader:
            for entry in reader.iter():
                question = entry["question"]["stem"]
                question_list.append(question)
                answers = [x["text"] for x in entry["question"]["choices"]]
                answer_list += answers

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}
    
# CommonSenseQA
class CommonSenseQAProcessor(DataProcessor):
    def get_all_examples(self, data_dir, debug_flag):
        comsense_dev = self._read_questions_examples(data_dir, "dev_rand_split", debug_flag)
        comsense_train = self._read_questions_examples(data_dir, "train_rand_split", debug_flag)
        comsense_test = self._read_questions_examples(data_dir, "test_rand_split_no_answers", debug_flag)
        question_list = comsense_dev["questions"] + comsense_train["questions"] + comsense_test["questions"]
        answer_list   = comsense_dev["answers"] + comsense_train["answers"] + comsense_test["answers"]
        
        return {"questions": question_list,
                "passages": [],
                "answers": answer_list}


    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, passage_list, answer_list, instance_list = [], [], [], []
        input_file = "{}/{}.jsonl".format(data_dir, sub_set)
        with jsonlines.open(input_file, "r") as reader:
            for entry in reader.iter():
                question = entry["question"]["stem"]
                question_list.append(question)
                for choice in entry["question"]["choices"]:
                    answer_list.append(choice["text"])  

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

# MCQL
class MCQLProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        mcql_physics = self._read_questions_examples(data_dir, "mcql_physics", debug_flag)
        mcql_physics_olvl = self._read_questions_examples(data_dir,  "mcql_physics-olvl", debug_flag)
        mcql_chem = self._read_questions_examples(data_dir, "mcql_chem", debug_flag)
        mcql_chem_olvl = self._read_questions_examples(data_dir,  "mcql_chem-olvl", debug_flag)
        mcql_biology = self._read_questions_examples(data_dir, "mcql_biology", debug_flag)
        mcql_biology_olvl = self._read_questions_examples(data_dir,  "mcql_biology-olvl", debug_flag)
        
        question_list = mcql_physics["questions"] + mcql_physics_olvl["questions"] + mcql_chem["questions"]  + mcql_chem_olvl["questions"] + mcql_biology["questions"]  + mcql_biology_olvl["questions"]
        answer_list   = mcql_physics["answers"] + mcql_physics_olvl["answers"] + mcql_chem["answers"]  + mcql_chem_olvl["answers"] + mcql_biology["answers"]  + mcql_biology_olvl["answers"]

        return {"questions": question_list,
                "passages": [],
                "answers": answer_list}


    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, passage_list, answer_list = [], [], []
        input_file = os.path.join(data_dir, "{}.json".format(sub_set))
        with open(input_file, "r", encoding='utf-8') as reader:
            input_data = json.load(reader)

        for entry in input_data:
            question = entry["sentence"]
            question_list.append(question)
            answer = entry["answer"]
            answer_list += answer
            for item in entry['distractors']:
                answer_list.append(item)

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}
#MathQA
class MathQAProcessor(DataProcessor):
    def get_all_examples(self, data_dir, debug_flag):
        train_data = self._read_questions_examples(data_dir, "train", debug_flag)
        dev_data = self._read_questions_examples(data_dir, "dev", debug_flag)
        test_data = self._read_questions_examples(data_dir, "test", debug_flag)
        question_list = train_data["questions"] + dev_data["questions"] + test_data["questions"]
        answer_list = train_data["answers"] + dev_data["answers"] + test_data["answers"]
        passage_list = train_data["passages"] + dev_data["passages"] + test_data["passages"]
    
        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, answer_list, passage_list = [], [], []
        input_file = os.path.join(data_dir, "{}.json".format(sub_set)) 
        with open(input_file, "r", encoding='utf-8') as reader:
            input_data = json.load(reader)
            for entry in input_data:
                passage = entry["Rationale"].replace("\n", " ")
                passage_list.append(passage)
                question = entry["Problem"]
                question_list.append(question)
                answers = entry["options"]
                option_pattern = re.compile(r'\)\s*([^,]+)')
                options_list = option_pattern.findall(answers)
                options = [value.strip() for value in options_list]
                for item in options:
                    answer_list.append(item)    

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

#QASC
class QASCProcessor(DataProcessor):
    def get_all_examples(self, data_dir, debug_flag):
        train_data = self._read_questions_examples(data_dir, "train", debug_flag)
        dev_data   = self._read_questions_examples(data_dir,  "dev", debug_flag)
        test_data  = self._read_questions_examples(data_dir,  "test", debug_flag)
        question_list = train_data["questions"]     + dev_data["questions"] + test_data["questions"]
        answer_list   = train_data["answers"]       + dev_data["answers"]   + test_data["answers"]
        corpus_file = os.path.join(data_dir, "QASC_Corpus.txt")
        
        passage_list = []

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}
    
    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, passage_list, answer_list, instance_list = [], [], [], []
        input_file = os.path.join(data_dir, "{}.jsonl".format(sub_set))
        with jsonlines.open(input_file, "r") as reader:
            for entry in reader.iter():
                question = entry["question"]["stem"]
                question_list.append(question)
                answers = [x["text"] for x in entry["question"]["choices"]]
                answer_list += answers

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

# MedMCQA 
class MedMCQArocessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):

        train_data = self._read_questions_examples(data_dir, "train", debug_flag)
        dev_data   = self._read_questions_examples(data_dir,  "dev", debug_flag)
        test_data  = self._read_questions_examples(data_dir,  "test", debug_flag)
        question_list = train_data["questions"] + dev_data["questions"] + test_data["questions"]
        answer_list   = train_data["answers"]   + dev_data["answers"] + test_data["answers"]
        passage_list  = train_data["passages"]  + dev_data["passages"] + test_data["passages"]

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        examples = []
        question_list, passage_list, answer_list, instance_list = [], [], [], []
        input_file = os.path.join(data_dir, "{}.json".format(sub_set))
        with open(input_file, "r", encoding='utf-8') as reader:
            for line in reader:
                try:
                    entry = json.loads(line)
                    question = entry["question"]
                    question_list.append(question)
                    if "exp" in entry:
                        passage = entry["exp"]
                        if passage != None:
                            passage_list.append(passage)
                    answera = entry["opa"]
                    answerb = entry["opb"]
                    answerc = entry["opc"]
                    answerd = entry["opd"]
                    local_answer = []
                    local_answer.append(answera)
                    local_answer.append(answerb)
                    local_answer.append(answerc)
                    local_answer.append(answerd)
                    answer_list += local_answer

                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}


# Televic
class TelevicProcessor(DataProcessor):
    def get_all_examples(self, data_dir, debug_flag):
        english_train = self._read_questions_examples(data_dir, "english", debug_flag)
        biology_train = self._read_questions_examples(data_dir, "biology", debug_flag)
        french_train = self._read_questions_examples(data_dir, "french", debug_flag)
        geography_train = self._read_questions_examples(data_dir, "geography", debug_flag)
        question_list = english_train["questions"] + biology_train["questions"] + french_train["questions"] + geography_train["questions"]
        answer_list   = english_train["answers"] + biology_train["answers"] + french_train["answers"] + geography_train["answers"]   
       
        return {"questions": question_list,
                "passages": [],
                "answers": answer_list}


    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, passage_list, answer_list, = [], [], []
        input_file = os.path.join(data_dir, "{}.json".format(sub_set))
        with open(input_file, "r", encoding='utf-8') as reader:
            input_data = json.load(reader)
            for entry in input_data:
                question = entry["question"]
                question_list.append(question)
                answer = entry['answer']
                answer_list.append(answer)
                distractors = entry['distractors']
                for item in distractors:
                    answer_list.append(item)
                    
        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

# EduQG
class EduQGProcessor(DataProcessor):
    
    def get_all_examples(self, data_dir, debug_flag):
        eduqg_train = self._read_questions_examples(data_dir, "qg_train_v0", debug_flag)
        eduqg_valid = self._read_questions_examples(data_dir, "qg_valid_v0", debug_flag)
        question_list = eduqg_train["questions"] + eduqg_valid["questions"] 
        answer_list   = eduqg_train["answers"]   + eduqg_valid["answers"] 
        passage_list  = eduqg_train["passages"]  + eduqg_valid["passages"]

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}


    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, passage_list, answer_list, instance_list = [], [], [], []
        input_file = os.path.join(data_dir, "{}.json".format(sub_set))
        with open(input_file, "r", encoding='utf-8') as reader:
            input_data = json.load(reader)
            for entry in input_data:
                question_items = entry["questions"]
                for item in question_items:
                    question = item['question']['question_text']
                    passage = item['hl_context']
                    passage_list.append(passage)
                    question_list.append(question)
                    answer = item['question']['question_choices']
                    for choice in answer:
                        answer_list.append(choice)
        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}



# Reading Comprehension - FITB - Datasets (CBT, WDW, BT) 
# Children Book Test (CBT)
class CBTestProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        question_list, passage_list, answer_list, instance_list = [], [], [], []
        files = os.listdir(data_dir)
        for file in files:
            if ".txt" not in file:
                continue
            else:
                story_input_file = os.path.join(data_dir, file)
                with open(story_input_file) as reader:
                    all_lines = reader.readlines()
                    paragraph_lines = []
                    for line in all_lines:
                        line = line.strip()
                        if len(line) == 0:
                            continue
                        parts = line.split()
                        number = int(parts[0])
                        text = " ".join(parts[1:])
                        if "XXXXX" not in text:
                            paragraph_lines.append(text)
                        if "XXXXX" in text:
                          q_parts = line.split("\t")
                          question = " ".join(q_parts[0].split()[1:])
                          question_list.append(question)
                          answer = [z.strip() for z in q_parts[-1].split("|")]
                          answer_list+=answer
                          passage = " ".join(paragraph_lines)
                          passage_list.append(passage)
                          paragraph_lines = []            
                        
        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

# Who Did What (WDW)
class WhoDidWhatProcessor(DataProcessor):
    
    def get_all_examples(self, data_dir, debug_flag):

        train_data = self._read_examples(data_dir, "train", debug_flag)
        dev_data   = self._read_examples(data_dir,  "val", debug_flag)
        test_data  = self._read_examples(data_dir,  "test", debug_flag)
        question_list = train_data["questions"] + dev_data["questions"] + test_data["questions"]
        answer_list   = train_data["answers"]   + dev_data["answers"]   + test_data["answers"]
        passage_list  = train_data["passages"]  + dev_data["passages"]  + test_data["passages"]

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

    def _read_examples(self, folder, set, debug_flag):
        """Creates examples for the training and dev sets."""
        if set == "train":
            input_file = os.path.join(folder, "Relaxed", "{}_key.xml".format(set))
        else:
            input_file = os.path.join(folder, "Strict", "{}_key.xml".format(set))

        question_list, passage_list, answer_list,  = [], [], []

        with open(input_file) as reader:
            all_lines = reader.readlines()
            left_part = ""
            question, answer = "", ""

            for line in all_lines:
                if "leftContext" in line:
                    left_part = line.split(">")[1].split("<")[0]
                if "rightContext" in line:
                    right_part = line.split(">")[1].split("<")[0]
                    question = " @placeholder ".join([left_part, right_part])
                    question_list.append(question)
                if "choice" in line:
                    answer = line.split(">")[1].split("<")[0]
                    answer_list.append(answer)
                if "</mc>" in line:
                    # NO LICENCE TO OBTAIN GIGIAWORD DATA = > no passage
                    if debug_flag:
                        break

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

#BT

# Reading Comprehension - MCQ - Datasets (MCTest, RACE, RACE-M, RACE-H, RACE-C, DREAM, CosmosQA, ReClor, QuAIL) 

# MCTest-500
class MCTest500Processor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        train_data = self._read_questions_examples(data_dir, "mc500.train", debug_flag)
        dev_data   = self._read_questions_examples(data_dir,  "mc500.dev", debug_flag)
        test_data  = self._read_questions_examples(data_dir,  "mc500.test", debug_flag)

        question_list = train_data["questions"] + dev_data["questions"] + test_data["questions"]
        answer_list   = train_data["answers"]   + dev_data["answers"]   + test_data["answers"]
        passage_list  = train_data["passages"]  + dev_data["passages"]  + test_data["passages"]

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

    def _read_questions_examples(self, data_dir, subset, debug_flag):
        question_list, passage_list, answer_list = [], [], []
        files = os.listdir(data_dir)
        for file in files:
            if "{}.tsv".format(subset) not in file:
                continue
            with open(os.path.join(data_dir, file)) as fd:
                rd = csv.reader(fd, delimiter="\t", quotechar='"')
                for row in rd:
                    actual_data = row[2:]
                    passage = actual_data[0].replace("\\newline", " ")
                    passage_list.append(passage)
                    local_q_list = []
                    local_a_list = []
                    for text in actual_data[1:]:
                        if "one:" in text:
                            question_list.append(text[4:].strip())
                            local_q_list.append(text[4:].strip())
                        elif "multiple:" in text:
                            question_list.append(text[9:].strip())
                            local_q_list.append(text[9:].strip())
                        else:
                            answer_list.append(text)
                            local_a_list.append(text)

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

# MCTest-500
class MCTest160Processor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        train_data = self._read_questions_examples(data_dir, "mc160.train", debug_flag)
        dev_data   = self._read_questions_examples(data_dir,  "mc160.dev", debug_flag)
        test_data  = self._read_questions_examples(data_dir,  "mc160.test", debug_flag)
        question_list = train_data["questions"] + dev_data["questions"] + test_data["questions"]
        answer_list   = train_data["answers"]   + dev_data["answers"]   + test_data["answers"]
        passage_list  = train_data["passages"]  + dev_data["passages"]  + test_data["passages"]

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

    def _read_questions_examples(self, data_dir, subset, debug_flag):
        question_list, passage_list, answer_list = [], [], []

        files = os.listdir(data_dir)
        for file in files:
            if "{}.tsv".format(subset) not in file:
                continue
            with open(os.path.join(data_dir, file)) as fd:
                rd = csv.reader(fd, delimiter="\t", quotechar='"')
                for row in rd:
                    actual_data = row[2:]
                    passage = actual_data[0].replace("\\newline", " ")
                    passage_list.append(passage)
                    local_q_list = []
                    local_a_list = []
                    for text in actual_data[1:]:
                        if "one:" in text:
                            question_list.append(text[4:].strip())
                            local_q_list.append(text[4:].strip())
                        elif "multiple:" in text:
                            question_list.append(text[9:].strip())
                            local_q_list.append(text[9:].strip())
                        else:
                            answer_list.append(text)
                            local_a_list.append(text)
                    if debug_flag:
                        break

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

# RACE
class RACEProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        question_list, passage_list, answer_list = [], [], []

        all_files_list = get_all_subfiles(data_dir, [], ".txt")
        for file in all_files_list:
            with open(file, "r") as reader:
                input_data = json.load(reader)
                passage = input_data["article"].replace("\n", " ")
                passage_list.append(passage)
                questions = input_data["questions"]
                question_list += questions
                answer_options = input_data["options"]
                # local_answer_list = []
                for options in answer_options:
                    answer_list+=options

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

# RACE-M
class RACEMProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):

        question_list, passage_list, answer_list = [], [], []
        all_files_list = get_all_subfiles(data_dir, [], ".txt")

        for file in all_files_list:
            with open(file, "r") as reader:
                input_data = json.load(reader)
                passage = input_data["article"].replace("\n", " ")
                passage_list.append(passage)
                questions = input_data["questions"]
                question_list += questions
                answer_options = input_data["options"]
                for options in answer_options:
                    answer_list+=options

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}


# RACE-H
class RACEHProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        question_list, passage_list, answer_list = [], [], []

        all_files_list = get_all_subfiles(data_dir, [], ".txt")
        for file in all_files_list:
            with open(file, "r") as reader:
                input_data = json.load(reader)

                passage = input_data["article"].replace("\n", " ")
                passage_list.append(passage)
                questions = input_data["questions"]
                question_list += questions
                answer_options = input_data["options"]
                for options in answer_options:
                    answer_list+=options
            if debug_flag:
                break

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

#RACE-C
class RACECProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        question_list, passage_list, answer_list = [], [], []
        all_files_list = get_all_subfiles(data_dir, [], ".txt")
        for file in all_files_list:
            with open(file, "r") as reader:
                input_data = json.load(reader)
                passage = input_data["article"].replace("\n", " ")
                passage_list.append(passage)
                questions = input_data["questions"]
                question_list += questions
                answer_options = input_data["options"]
                for options in answer_options:
                    answer_list+=options


        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

# DREAM
class DREAMProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        train_data = self._read_questions_examples(data_dir, "train", debug_flag)
        dev_data   = self._read_questions_examples(data_dir,  "dev", debug_flag)
        test_data  = self._read_questions_examples(data_dir,  "test", debug_flag)

        question_list = train_data["questions"] + dev_data["questions"] + test_data["questions"]
        answer_list   = train_data["answers"]   + dev_data["answers"]   + test_data["answers"]
        passage_list  = train_data["passages"]  + dev_data["passages"]  + test_data["passages"]

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, passage_list, answer_list = [], [], []
        input_file = os.path.join(data_dir, "{}.json".format(sub_set))
        with open(input_file, "r", encoding='utf-8') as reader:
            input_data = json.load(reader)

        for entry in input_data:
            passage = " ".join(entry[0])
            passage_list.append(passage)

            for qa in entry[1]:
                question = qa["question"]
                question_list.append(question)
                answer_list += qa["choice"]

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

#CosmosQA
class CosmosQAProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        train_data = self._read_questions_examples(data_dir, "train", debug_flag)
        dev_data   = self._read_questions_examples(data_dir,  "valid", debug_flag)
        test_data  = self._read_test_questions_examples(data_dir,  "test", debug_flag)

        question_list = train_data["questions"] + dev_data["questions"] + test_data["questions"]
        answer_list   = train_data["answers"]   + dev_data["answers"]   + test_data["answers"]
        passage_list  = train_data["passages"]  + dev_data["passages"]  + test_data["passages"]

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

    def _read_questions_examples(self, data_dir, subset, debug_flag):
        question_list, passage_list, answer_list = [], [], []
        input_file = "{}{}.csv".format(data_dir, subset)
        print("Yes, open")
        with open(input_file, newline='', encoding="utf-8") as csvfile:
            data = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(data)
            for entry in data:
                passage_list.append(entry[1])
                question_list.append(entry[2])
                answer_list.append(entry[3])
                answer_list.append(entry[4])
                answer_list.append(entry[5])
                answer_list.append(entry[6])

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

    def _read_test_questions_examples(self, data_dir, subset, debug_flag):
        question_list, passage_list, answer_list = [], [], []

        input_file = "{}/{}.jsonl".format(data_dir, subset)
        with jsonlines.open(input_file, "r") as reader:
            for entry in reader.iter():
                passage_list.append(entry["context"])
                question_list.append(entry["question"])
                answer_list.append(entry["answer0"])
                answer_list.append(entry["answer1"])
                answer_list.append(entry["answer2"])
                answer_list.append(entry["answer3"])

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}


#ReClor
class ReClorProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        train_data = self._read_questions_examples(data_dir, "train", debug_flag)
        dev_data   = self._read_questions_examples(data_dir,  "val", debug_flag)
        test_data  = self._read_questions_examples(data_dir,  "test", debug_flag)

        question_list = train_data["questions"] + dev_data["questions"] + test_data["questions"]
        answer_list   = train_data["answers"]   + dev_data["answers"]   + test_data["answers"]
        passage_list  = train_data["passages"]  + dev_data["passages"]  + test_data["passages"]

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        
        question_list, passage_list, answer_list = [], [], []
        input_file = os.path.join(data_dir, "{}.json".format(sub_set))
        with open(input_file, "r", encoding='utf-8') as reader:
            input_data = json.load(reader)

        for entry in input_data:
            passage = entry["context"]
            passage_list.append(passage)
            question = entry["question"]
            question_list.append(question)
            answer_list += entry["answers"]

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}


#QuAIL
class QuAILProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        train_data = self._read_questions_examples(data_dir, "train", debug_flag)
        dev_data = self._read_questions_examples(data_dir, "dev", debug_flag)
        challenge_data = self._read_questions_examples(data_dir, "challenge", debug_flag)
        question_list = train_data["questions"] + dev_data["questions"] + challenge_data["questions"]
        answer_list = train_data["answers"] + dev_data["answers"] + challenge_data["answers"]
        passage_list = train_data["passages"] + dev_data["passages"] +  challenge_data["passages"]
        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, answer_list, passage_list = [], [], []
        input_file = os.path.join(data_dir, "{}.json".format(sub_set))

        data, context_id = [] , []
        item_id = ''
        with open(input_file, "r", encoding='utf-8') as reader:
            for line in reader:
               data.append(json.loads(line))
        for entry in data:
            item_id = entry["context_id"]
            passage =[]
            if item_id not in context_id:
                context_id.append(item_id)
                passage = entry["context"]
                passage_list.append(passage)   
            else:
                passage = entry["context"]   

            question = entry["question"]
            question_list.append(question)
            for item in entry["answers"]:
                answer = item 
                answer_list.append(answer)

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}


# Multimodal Datasets - (MovieQA, Visual7W, TQA, RecipeQA) 
# MovieQA
class MovieQAProcessor(DataProcessor):
    def get_all_examples(self, data_dir, debug_flag):

        data = self._read_questions_examples([], data_dir, debug_flag)
        question_list = data["questions"]
        answer_list   = data["answers"]   

        return {"questions": question_list,
                "passages": [],
                "answers": answer_list}

    def _read_questions_examples(self, passages_dict, data_dir, debug_flag):
        question_list, answer_list = [], []
        input_file = "{}data/qa.json".format(data_dir)
        with open(input_file, "r", encoding='utf-8') as reader:
            input_data = json.load(reader)

        movie_questions = {}
        movie_answers = {}
        for entry in input_data:
            moview_key = entry["imdb_key"]
            if moview_key not in list(movie_questions.keys()):
                movie_questions[moview_key] = []
                movie_answers[moview_key] = []
            question_list.append(entry["question"])
            movie_questions[moview_key].append(entry["question"])
            movie_answers[moview_key]+=entry["answers"]

            local_answers = []
            for answer in entry["answers"]:
                answer_list.append(answer)
                local_answers.append(answer)

        return {"questions": question_list,
                "answers": answer_list}

# Visual7w
class Visual7WProcessor(DataProcessor):
    def get_all_examples(self, data_dir, debug_flag):
        
        pointing_data = self._read_questions_examples(data_dir, "dataset_v7w_pointing", debug_flag)
        telling_data = self._read_questions_examples(data_dir, "dataset_v7w_telling", debug_flag)
        question_list = pointing_data["questions"] + telling_data["questions"]
        answer_list = pointing_data["answers"] + telling_data["answers"]

        return {"questions": question_list,
                "passages": [],
                "answers": answer_list}


    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
       question_list, answer_list = [], []
       input_file = "{}{}.json".format(data_dir, sub_set)
       with open(input_file, "r", encoding='utf-8') as reader:
            input_data = json.load(reader)
       for image in input_data["images"]:
           for entry in image["qa_pairs"]:
               question = entry["question"]
               question_list.append(question)
               multiple_choices = entry["multiple_choices"]
               for item in multiple_choices:
                   str_item = str(item)
                   if re.match(r'\d+', str_item):
                       continue
                   answer_list.append(item)

       return {"questions": question_list,
                "answers": answer_list}

 

# TQA
class TQAProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        train_data = self._read_questions_examples(data_dir, "tqa_v1_train", debug_flag)
        val_data = self._read_questions_examples(data_dir, "tqa_v1_val", debug_flag)
        test_data = self._read_questions_examples(data_dir, "tqa_v2_test", debug_flag)


        question_list = train_data["questions"] + val_data["questions"] + test_data["questions"]
        answer_list = train_data["answers"] + val_data["answers"] + test_data["answers"]
        passage_list = train_data["passages"] + val_data["passages"] + test_data["passages"]
        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}

    def _read_questions_examples(self, data_dir, sub_set, debug_flag):

        question_list, passage_list, answer_list = [], [], []
        input_file = os.path.join(data_dir, "{}.json".format(sub_set))
        with open(input_file, "r", encoding='utf-8') as reader:
            input_data = json.load(reader)
        question_types = {'Multiple Choice', 'Matching', 'True or False', 'Diagram Multiple Choice'}
        type_counts = {type: 0 for type in question_types}
        for entry in input_data:
            non_diagram_questions = entry["questions"]["nonDiagramQuestions"]
            for question_id, question_item in non_diagram_questions.items():
                  answer_choices = question_item["answerChoices"]
                  question = question_item["beingAsked"]["processedText"]
                  question_type = question_item["questionSubType"]
                  local_answer = []
                  if question_type in question_types:
                      type_counts[question_type] += 1
                  # Extract question list
                  question_list.append(question)
                  # Extract answer list
                  for choice_id, choice_data in answer_choices.items():
                    answers = choice_data["processedText"]
                    local_answer.append(answers)
                    answer_list.append(answers)

        for entry in input_data:
          # Extracting Diagram Questions 
            # example = []
            diagram_questions = entry["questions"]["diagramQuestions"] 
            # if  diagram_questions :    
            for question_id, question_item in diagram_questions.items():
                     answer_choices = question_item["answerChoices"]
                     question = question_item["beingAsked"]["processedText"]
                     question_type = question_item["questionType"]
                     if question_type in question_types:
                         type_counts[question_type] += 1
                     # Extract question list
                     question_list.append(question)
                     # Extract answer list
                     for choice_id, choice_data in answer_choices.items():
                       processed_text = choice_data["processedText"]
                       answer_list.append(processed_text)
           
        i= 0
        for entry in input_data:
             text_content, passage = [], []
            
             for section_key, section_value in entry["adjunctTopics"].items():
                 if "content" in section_value and "text" in section_value["content"]:
                     text_content ="".join(section_value["content"]["text"])
                     passage.append(text_content)
                 else:
                   i+=1
             text = [s.replace('\n', '') for s in passage]
             passage_list.append(" ".join(text))
             
           
        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list,
                "question_types" : type_counts}
    

# RecipeQA
class RecipeQAProcessor(DataProcessor):

    def get_all_examples(self, folder, debug_flag):
       passage_list, answer_list = [], []
       question_list = { "textual_cloze": [], "visual_ordering": [], "visual_coherence": [], "visual_cloze": [] }
       all_files_list = get_all_subfiles(folder, [], ".json")
       for file in all_files_list:
           with open(file, "r") as reader:
               input_data = json.load(reader)
           for entry in input_data["data"]:
              
              # Extract Passage
              context_list = []
              for context in entry["context"]:
                  context_list.append(context["body"])
              passage = " ".join(context_list)
              passage_list.append(passage)
              
              # Extract Queries
              question = " ".join(entry["question"])
              if entry["task"] == "textual_cloze":
                  # textual_cloze_question = question
                  question_list["textual_cloze"].append(question)
              elif entry["task"] == "visual_cloze":
                  question_list["visual_cloze"].append(question)
              elif entry["task"] == "visual_coherence":
                  question_list["visual_coherence"].append(question)
              elif entry["task"] == "visual_ordering":
                  question_list["visual_ordering"].append(question)
              else:
                  print("error")
                  
              # Extract Options
              options = entry["choice_list"]
              for op in options:
                  if entry["task"] == "visual_ordering":
                      for item in op:
                          answer_list.append(item) 
                  else:
                      answer_list.append(op) 
                 
       return {"questions": question_list,
               "passages": passage_list,
               "answers": answer_list}

# ScienceQA
class ScienceQAProcessor(DataProcessor):

    def get_all_examples(self, data_dir, debug_flag):
        problems_data = self._read_questions_examples(data_dir, "problems", debug_flag)
        question_list = problems_data["questions"] 
        answer_list = problems_data["answers"] 
        passage_list = problems_data["passages"] 

        return {"questions": question_list,
                "passages": [],
                "answers": answer_list}

    def _read_questions_examples(self, data_dir, sub_set, debug_flag):
        question_list, answer_list, passage_list = [], [], []
        input_file = os.path.join(data_dir, "{}.json".format(sub_set))

        with open(input_file, "r", encoding='utf-8') as reader:
            input_data = json.load(reader)
            for entry in input_data:
                item = input_data[entry]
                question = item["question"]
                question_list.append(question)
                answers = item["choices"]
                for choice in answers:
                    answer_list.append(choice)    

        return {"questions": question_list,
                "passages": passage_list,
                "answers": answer_list}
  
processors = {
# CLOZE - FITB
    "cloth" : CLOTHProcessor,
    "clothm" : CLOTHMProcessor,
    "clothh" : CLOTHHProcessor,
    "scde" : SCDEProcessor,
    "dgen"  : DGENProcessor,
    "cela" : CELAProcessor,
# CLOZE - MCQ   
    "sciq" : SciQProcessor,
    "aquarat": AquaRatProcessor,
    "openbookqa" : OpenBookQAProcessor,
    "arc" : ARCProcessor,
    "arc_challange" :  ARC_Challange_Processor,
    "arc_easy" : ARC_Easy_Processor,
    "commonsenseqa" : CommonSenseQAProcessor,
    "mcql" : MCQLProcessor,
    "mathqa": MathQAProcessor,
    "qasc" : QASCProcessor,
    "medmcqa" : MedMCQArocessor,
    "televic": TelevicProcessor,
    "eduqg" : EduQGProcessor,
# RC - FITB       
    "cbt" : CBTestProcessor,
    "wdw" : WhoDidWhatProcessor,
# RC - MCQ  
    "mctest160" : MCTest160Processor,
    "mctest500" : MCTest500Processor,
    "race":  RACEProcessor,
    "racem": RACEMProcessor,
    "raceh": RACEHProcessor,
    "racec" : RACECProcessor,
    "dream" : DREAMProcessor,
    "cosmosqa" : CosmosQAProcessor,
    "reclor" : ReClorProcessor,
    "quail" : QuAILProcessor,
# Multimodal - MCQ
    "movieqa" : MovieQAProcessor,
    "visual7w" : Visual7WProcessor,
    "tqa" : TQAProcessor,
    "recipeqa" :  RecipeQAProcessor,
    "scienceqa" : ScienceQAProcessor,
}

