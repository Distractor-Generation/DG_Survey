data_folder = r'C://Desktop//Project//data_folder//'
result_folder = data_folder + "_DG_TASK_RESULT"
save_data_path = r'C:Desktop//Project//data_folder//DG_TASK_ANALYSIS//'

dataset_names = {
# Task : CLOZE FITB
    "cloth" : "CLOTH",
    "clothm" : "CLOTHM",
    "clothh" : "CLOTHH",
    "scde": "SCDE", 
    "dgen" : "DGEN",
    "cela": "CELA",
# Task : CLOZE MCQ
    "sciq" : "SCIQ",
    "aquarat": "AQUARAT",
    "openbookqa" : "OpenBookQA",
    "arc": "ARC", 
    "arc_challange" : "ARC_challange",
    "arc_easy" : "ARC_easy",
    "commonsenseqa" : "COMMONSENSEQA",
    "mcql" : "MCQL",
    "mathqa" : "MATHQA",
    "qasc" : "QASC",
    "medmcqa" : "MEDMCQA",
    "televic" : "TELEVIC",
    "eduqg" : "EDUQG",
    "medmcqa" : "MedMCQA",
# Task : RC FITB
    "cbt" : "CBT",
    "wdw" : "WDW",
# Task : RC MCQ
    "mctest500" : "MCTEST500",
    "mctest160" : "MCTEST160",
    "race": "RACE",
    "racem": "RACEM",
    "raceh": "RACEH",
    "racec": "RACEC",
    "dream": "DREAM",
    "cosmosqa": "CosmosQA",
    "reclor" : "RECLOR",
    "quail": "QUAIL",
# Task : Multimodal - MCQ
    "movieqa" : "MOVIEQA",
    "visual7w": "visual7w",
    "tqa" : "TQA",
    "recipeqa" : "RECIPEQA", 
    "scienceqa" : "SCIENCEQA"
}

datapaths = {
# Task : CLOZE FITB
     "cloth" : data_folder + 'CLOTH//',
     "clothm" : data_folder + 'CLOTHM//',
     "clothh" : data_folder + 'CLOTHH//',
     "scde" : data_folder + 'SCDE//',
     "dgen" : data_folder + 'DGEN//',
     "cela": data_folder + "cela//",
# Task : CLOZE MCQ   
    "sciq" : data_folder + 'SCIQ//',
    "aquarat": data_folder + "AQUARAT//",
    "openbookqa": data_folder + 'OpenBookQA//',
    "arc" : data_folder + 'ARC//',
    "arc_challange" :  data_folder + 'ARC-Challange//',
    "arc_easy" :  data_folder + 'ARC-Easy//',
    "commonsenseqa" : data_folder + 'COMMONSENSEQA//',
    "mcql" : data_folder + 'MCQL//',
    "mathqa" : data_folder + 'MATHQA//',
    "qasc": data_folder + 'QASC//',
    "medmcqa" : data_folder + "MEDMCQA//",
    "televic" : data_folder +"TELEVIC//",
    "eduqg" : data_folder + 'EDUQG//',
# Task : RC FITB
    "cbt" : data_folder + 'CBT//',
    "wdw" :  data_folder + 'WDW//',
# Task : RC MCQ
    "mctest160" :  data_folder + 'MCTEST160//',
    "mctest500" :  data_folder + 'MCTEST500//',
    "race": data_folder + 'RACE//',
    "racem": data_folder + 'RACEM//',
    "raceh": data_folder + 'RACEH//',
    "racec" : data_folder + 'RACEC//',
    "dream": data_folder + 'DREAM//',
    "cosmosqa" : data_folder + 'CosmosQA//',
    "reclor" :  data_folder + 'RECLOR//',
    "quail": data_folder + 'QUAIL//',  
# Task : Multimodal - MCQ
    "movieqa" :  data_folder + "MOVIEQA//",
    "visual7w": data_folder + "visual7w//",
    "tqa" : data_folder + "TQA//",
    "recipeqa" : data_folder + 'RECIPEQA//',
    "scienceqa" : data_folder + 'SCIENCEQA//',
}
