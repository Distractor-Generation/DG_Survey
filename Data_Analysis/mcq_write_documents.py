from mcq_utils import write_vocabulary, write_questions, write_cloze_questions, write_sentence_questions, write_options, write_passage, write_other_questions
from mcq_query_types import categorize_query_types, blanks_number_cbt ,blanks_number_cloth, blanks_number_scde, blanks_number_wdw, blanks_number_dgen, blanks_number_cela

def write_documents(passages, questions, options, vocabulary , taskname):
    if taskname in ["cloth", "clothm", "clothh"]:
        write_vocabulary(vocabulary, taskname)
        write_cloze_questions(questions, taskname)
        write_passage(passages, taskname) 
        write_options(options, taskname)
        print("Total blnak Numbers in " + str(taskname) + " is " + str(blanks_number_cloth(passages)))
        
    elif taskname in ["scde"]:
        write_vocabulary(vocabulary, taskname)
        write_cloze_questions(questions, taskname)
        write_passage(passages, taskname) 
        write_options(options, taskname)
        print("Total blnak Numbers in " + str(taskname) + " is " + str(blanks_number_scde(passages)))
        
    elif taskname in ["cbt"]:
        write_vocabulary(vocabulary, taskname)
        write_cloze_questions(questions, taskname)
        write_passage(passages, taskname) 
        write_options(options, taskname)
        print("Total blnak Numbers in " + str(taskname) + " is " + str(blanks_number_cbt(questions)))
        
    elif taskname in ["wdw"]:
          write_vocabulary(vocabulary, taskname)
          write_cloze_questions(questions, taskname)
          write_passage(passages, taskname) 
          write_options(options, taskname)
          print("Total blnak Numbers in " + str(taskname) + " is " + str(blanks_number_wdw(questions)))
          
    elif taskname in ["dgen"]:
          write_vocabulary(vocabulary, taskname)
          write_cloze_questions(questions, taskname)
          write_passage(passages, taskname) 
          write_options(options, taskname)
          print("Total blnak Numbers in " + str(taskname) + " is " + str(blanks_number_dgen(questions)))
          
    elif taskname in ["cela"]:
        write_vocabulary(vocabulary, taskname)
        write_cloze_questions(questions, taskname)
        write_passage(passages, taskname) 
        write_options(options, taskname)
        print("Total blnak Numbers in " + str(taskname) + " is " + str(blanks_number_cela(passages)))
    else:
        write_vocabulary(vocabulary, taskname)
        write_cloze_questions(questions, taskname)
        write_passage(passages, taskname) 
        write_options(options, taskname)
        all_questions = categorize_query_types(questions)
        if len(all_questions["question_type"]) > 0:
            write_questions(all_questions["question_type"], taskname)
        if len(all_questions["cloze_type"]) > 0:
            write_cloze_questions(all_questions["cloze_type"], taskname)
        if len(all_questions["sentence_type"]) > 0:
            write_sentence_questions(all_questions["sentence_type"], taskname)
        if len(all_questions["other_type"]) > 0:
            write_other_questions(all_questions["other_type"], taskname)