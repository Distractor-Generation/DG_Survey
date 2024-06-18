# DG_Survey
This is reading list for **Distractor Generation for Multiple-Choice Tasks: A Survey of Methods, Datasets, and Evaluation**

It contains **recommended reading papers** and dataset **links**.

## Recommended Reading Papers
### Surveys
* A Survey of Natural Language Generation (ACM Computing Surveys) [Paper](https://dl-acm-org.simsrad.net.ocs.mq.edu.au/doi/10.1145/3554727)
* A Review on Question Generation from Natural Language Text (ACM Transactions on Information Systems) [Paper](https://dl.acm.org/doi/abs/10.1145/3468889)
* A Systematic Review of Automatic Question Generation for Educational Purposes (International Journal of Artificial Intelligence in Education) [Paper](https://link.springer.com/article/10.1007/s40593-019-00186-y)
* Automatic Multiple Choice Question Generation From Text: A Survey (IEEE Transactions on Learning Technologies) [Paper](https://ieeexplore.ieee.org/abstract/document/8585151)
* Automatic question generation and answer assessment: a survey (Research and Practice in Technology Enhanced Learning) [Paper](https://telrp.springeropen.com/articles/10.1186/s41039-021-00151-1)
* Survey of Hallucination in Natural Language Generation  (ACM Computing Surveys) [Paper](https://dl.acm.org/doi/abs/10.1145/3571730)
* A Survey of Controllable Text Generation Using Transformer-based Pre-trained Language Models (ACM Computing Surveys) [Paper](https://dl.acm.org/doi/abs/10.1145/3617680)
* Recent Advances in Natural Language Processing via Large Pre-trained Language Models: A Survey (ACM Computing Surveys) [Paper](https://dl.acm.org/doi/abs/10.1145/3605943)
* Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing (ACM Computing Surveys) [Paper](https://dl.acm.org/doi/full/10.1145/3560815)

## Distractor Generation Methods
### Traditioanl
#### Corpus-based
* Fast--an automatic generation system for grammar tests (COLING) [Paper](https://aclanthology.org/P06-4001.pdf)
* Glove: Global vectors for word representation (EMNLP) [Paper](https://aclanthology.org/D14-1162.pdf)
* Automatic generation of context-based fill-in-the-blank exercises using co-occurrence likelihoods and Google n-grams (BEA) [Paper](https://aclanthology.org/W16-0503.pdf)
* Discriminative Approach to Fill-in-the-Blank Quiz Generation for Language Learners (ACL) [Paper](https://aclanthology.org/P13-2043.pdf)
* Automatic Gap-fill Question Generation from Text Books (BEA) [Paper](https://aclanthology.org/W11-1407.pdf)
* Automatic Generation of Challenging Distractors Using Context-Sensitive Inference Rules (BEA)[Paper](https://aclanthology.org/W14-1817.pdf)

#### Graph-based
* Semantic Similarity of Distractors in Multiple-Choice Tests: Extrinsic Evaluation (GEMS) [Paper](https://aclanthology.org/W09-0207.pdf)
* Knowledge-Driven Distractor Generation for Cloze-Style Multiple Choice Questions (AAAI) [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/16559)
* Multiple Choice Question Generation Utilizing An Ontology (BEA) [Paper](https://aclanthology.org/W17-5034/)
* Ontology-Based Generation of Medical, Multi-term MCQs (International Journal of Artificial Intelligence in Education) [Paper](https://link.springer.com/article/10.1007/s40593-018-00172-w)
* A novel approach to generate distractors for Multiple Choice Questions (Expert Systems with Applications)[Paper](https://www.sciencedirect.com/science/article/pii/S0957417423005249)

### Deep Neural Networks
* Sequence to sequence learning with neural networks (NeurIPS) [Paper](https://proceedings.neurips.cc/paper/2014/hash/a14ac55a4f27472c5d894ec1c3c743d2-Abstract.html)
* Neural Machine Translation by Jointly Learning to Align and Translate (ICLR) [Paper](https://arxiv.org/pdf/1409.0473)
* Effective Approaches to Attention-based Neural Machine Translation (EMNLP) [Paper](https://aclanthology.org/D15-1166.pdf)
* Generating Distractors for Reading Comprehension Questions from Real Examinations (AAAI) [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/4606)
* A Hierarchical Neural Autoencoder for Paragraphs and Documents (ACL) [Paper](https://aclanthology.org/P15-1107.pdf)
* From Neural Sentence Summarization to Headline Generation: A Coarse-to-Fine Approach (IJCAI) [Paper](https://www.ijcai.org/proceedings/2017/574)
* Coarse-to-Fine Attention Models for Document Summarization (WS) [Paper](https://aclanthology.org/W17-4505/)
* Co-Attention Hierarchical Network: Generating Coherent Long Distractors for Reading Comprehension (AAAI) [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/6522)
* Bidirectional Attention Flow for Machine Comprehension (ICLR)[Paper](https://arxiv.org/pdf/1611.01603)
* Topic Enhanced Multi-head Co-Attention: Generating Distractors for Reading Comprehension (IJCNN) [Paper](https://ieeexplore.ieee.org/abstract/document/9533341)
* Learning to Distract: A Hierarchical Multi-Decoder Network for Automated Generation of Long Distractors for Multiple-Choice Questions for Reading Comprehension (CIKM) [Paper](https://dl.acm.org/doi/10.1145/3340531.3411997)
* QDG: A unified model for automatic question-distractor pairs generation (Applied Intelligence) [Paper](https://link.springer.com/article/10.1007/s10489-022-03894-6)
* Diverse Distractor Generation for Constructing High-Quality Multiple Choice Questions (IEEE/ACM Transactions on Audio, Speech and Language Processing) [Paper](https://dl.acm.org/doi/abs/10.1109/TASLP.2021.3138706)
* Mixture Content Selection for Diverse Sequence Generation (EMNLP|IJCNLP) [Paper](https://aclanthology.org/D19-1308.pdf)
* Automatic Distractor Generation for Multiple Choice Questions in Standard Tests  (COLING) [Paper](https://aclanthology.org/2020.coling-main.189/)

### Pre-trained Models
#### Word-Embedding 
* GloVe: Global Vectors for Word Representation (EMNLP) [Paper](https://aclanthology.org/D14-1162.pdf)
* Enriching Word Vectors with Subword Information (TACL) [Paper](https://aclanthology.org/Q17-1010.pdf)
* Revup: Automatic Gap-fill Question Generation from Educational Texts (BEA) [Paper](https://aclanthology.org/W15-0618.pdf)
* Distractor Generation for Chinese Fill-in-the-blank Items (BEA) [Paper](https://aclanthology.org/W17-5015.pdf)
* Distractor Generation for Fill-in-the-Blank Exercises by Question Type (ACL) [Paper](https://aclanthology.org/2023.acl-srw.38/)
* Questimator: Generating Knowledge Assessments for Arbitrary Topics (IJCAI) [Paper](https://www.ijcai.org/Proceedings/16/Papers/524.pdf)
* Automatic distractor generation for multiple-choice English vocabulary questions (Research and Practice in Technology Enhanced Learning) [Paper](https://telrp.springeropen.com/articles/10.1186/s41039-018-0082-z)
* Difficulty-aware Distractor Generation for Gap-Fill Items (ALTA) [Paper](https://aclanthology.org/U19-1021.pdf)

#### Pre-trained Language Models (PLMs)
* Language Models are Few-Shot Learners (NeurIPS) [Paper](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html)
* BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (NAACL) [Paper](https://aclanthology.org/N19-1423.pdf)
* Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (The Journal of Machine Learning Research) [Paper](https://dl.acm.org/doi/abs/10.5555/3455716.3455856)
* BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension (ACL) [Paper](https://aclanthology.org/2020.acl-main.703.pdf)

#### PLMs with Fine-Tuning
* A BERT-based Distractor Generation Scheme with Multi-tasking and Negative Answer Training Strategies (Findings) [Paper](https://aclanthology.org/2020.findings-emnlp.393.pdf)
* CDGP: Automatic Cloze Distractor Generation based on Pre-trained Language Model (Findings) [Paper](https://aclanthology.org/2022.findings-emnlp.429.pdf)
* Learning to Reuse Distractors to Support Multiple-Choice Question Generation in Education (IEEE Transactions on Learning Technologies) [Paper](https://ieeexplore.ieee.org/abstract/document/9969921)
* Distractor Generation based on Text2Text Language Models with Pseudo Kullback-Leibler Divergence Regulation (Findings) [Paper](https://aclanthology.org/2023.findings-acl.790.pdf)
* Distractor Generation Using Generative and Discriminative Capabilities of Transformer-based Models (LREC|COLING) [Paper](https://aclanthology.org/2024.lrec-main.452.pdf)
* BERT-based distractor generation for Swedish reading comprehension questions using a small-scale dataset (INLG) [Paper](https://aclanthology.org/2021.inlg-1.43.pdf)
* Distractor Generation Through Text-to-Text Transformer Models (IEEE Access) [Paper](https://ieeexplore.ieee.org/abstract/document/10418879)

#### PLMs with Prompting
* Generating Multiple Choice Questions for Computing Courses Using Large Language Models (Frontiers in Education) [Paper](https://ieeexplore.ieee.org/abstract/document/10342898)
* A Novel Multi-Stage Prompting Approach for Language Agnostic MCQ Generation Using GPT (Advances in Information Retrieval) [Paper](https://link.springer.com/chapter/10.1007/978-3-031-56063-7_18)
* Distractor generation for multiple-choice questions with predictive prompting and large language models (RKDE) [Paper](https://arxiv.org/pdf/2307.16338)
* Automated Distractor and Feedback Generation for Math Multiple-choice Questions via In-context Learning (NeurIPS) [Paper](https://arxiv.org/pdf/2308.03234)
* A Comparative Study of AI-Generated (GPT-4) and Human-crafted MCQs in Programming Education (ACE) [Paper](https://dl.acm.org/doi/abs/10.1145/3636243.3636256)

### Other Models
* Distractor Generation for Multiple Choice Questions Using Learning to Rank (BEA) [Paper](https://aclanthology.org/W18-0533.pdf)
* Ranking Multiple Choice Question Distractors using Semantically Informed Neural Networks (CIKM) [Paper](https://dl.acm.org/doi/abs/10.1145/3340531.3417468)
* Distractor generation with generative adversarial nets for automatically creating fill-in-the-blank questions (K-Cap) [Paper](https://dl.acm.org/doi/abs/10.1145/3148011.3154463)
* Automatic Generation of Distractors for Fill-in-the-Blank Exercises with Round-Trip Neural Machine Translation (ACL) [Paper](https://aclanthology.org/2022.acl-srw.31.pdf)
* Using Neural Machine Translation for Generating Diverse Challenging Exercises for Language Learner (ACL) [Paper](https://aclanthology.org/2023.acl-long.337.pdf)
* Good, better, best: Textual distractors generation for multiple-choice visual question answering via reinforcement learning (CVPR) [Paper](https://openaccess.thecvf.com/content/CVPR2022W/ODRUM/html/Lu_Good_Better_Best_Textual_Distractors_Generation_for_Multiple-Choice_Visual_Question_CVPRW_2022_paper.html)
* Can We Learn Question, Answer, and Distractors All from an Image? A New Task for Multiple-choice Visual Question Answering (LREC|COLING) [Paper](https://aclanthology.org/2024.lrec-main.254.pdf)

## Evalaution Methods
* Assessing ranking metrics in top-N recommendation (Information Retrieval Journal) [Paper](https://link.springer.com/article/10.1007/s10791-020-09377-x)
* A Survey of Evaluation Metrics Used for NLG Systems (ACM Computing Surveys) [Paper](https://dl.acm.org/doi/abs/10.1145/3485766)
* Bleu: a Method for Automatic Evaluation of Machine Translation (ACL) [Paper](https://aclanthology.org/P02-1040.pdf)
* ROUGE: A Package for Automatic Evaluation of Summaries (WS) [Paper](https://aclanthology.org/W04-1013.pdf)
* The METEOR metric for automatic evaluation of machine translation (Machine Translation) [Paper](https://link.springer.com/article/10.1007/s10590-009-9059-4)
* Why We Need New Evaluation Metrics for NLG (EMNLP) [Paper](https://aclanthology.org/D17-1238/)
* BLEU is Not Suitable for the Evaluation of Text Simplification (EMNLP) [Paper](https://aclanthology.org/D18-1081/)

## Dataset - [Paper] (Publisher) [Dataset Link]
* CLOTH  - [Large-scale Cloze Test Dataset Created by Teachers] (EMNLP) [Dataset](https://www.cs.cmu.edu/~glai1/data/cloth/)
* SCDE   - [SCDE: Sentence Cloze Dataset with High Quality Distractors From Examinations] (ACL) [Dataset](https://vgtomahawk.github.io/sced.html)
* DGen   - [Knowledge-Driven Distractor Generation for Cloze-Style Multiple Choice Questions] (AAAI) [Dataset](https://github.com/DRSY/DGen)
* CELA - [Cloze Quality Estimation for Language Assessment] (EACL) [Dataset](https://github.com/zz-zhang/cloze-quality-estimation)
* SciQ - [Crowdsourcing Multiple Choice Science Questions] (WNUT) [Dataset](https://allenai.org/data/sciq)
* AQUA-RAT  - [Program Induction by Rationale Generation: Learning to Solve and Explain Algebraic Word Problems] (ACL) [Dataset](https://github.com/google-deepmind/AQuA)
* OpenBookQA  - [Can a Suit of Armor Conduct Electricity? A New Dataset for Open Book Question Answering] (EMNLP) [Dataset](https://allenai.org/data/open-book-qa)
* ARC - [Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge] (AI2) [Dataset](https://allenai.org/data/arc)
* CommonsenseQA - [CommonsenseQA: A Question Answering Challenge Targeting Commonsense Knowledge] (NAACL) [Dataset](https://www.tau-nlp.sites.tau.ac.il/commonsenseqa)
* MCQL - [Distractor Generation for Multiple Choice Questions Using Learning to Rank] (BEA) [Dataset](https://github.com/harrylclc/LTR-DG)
* MathQA  - [MathQA: Towards Interpretable Math Word Problem Solving with Operation-Based Formalisms] (NAACL) [Dataset](https://math-qa.github.io/)
* QASC  - [QASC: A Dataset for Question Answering via Sentence Composition] (AAAI) [Dataset](https://allenai.org/data/qasc)
* MedMCQA  - [MedMCQA: A Large-scale Multi-Subject Multi-Choice Dataset for Medical domain Question Answering] (PMLR) [Dataset](https://github.com/MedMCQA/MedMCQA?tab=readme-ov-file)
* Televic - [Learning to Reuse Distractors to Support Multiple-Choice Question Generation in Education] (IEEE Transactions on Learning Technologies) [Dataset](https://ieee-dataport.org/documents/distractor-retrieval-dataset), [Sample Test](https://github.com/semerekiros/dist-retrieval)
* EduQG   - [EduQG: A Multi-Format Multiple-Choice Dataset for the Educational Domain] (IEEE Access) [Dataset](https://github.com/hadifar/question-generation)
* ChildrenBookTest  - [The Goldilocks principle: Reading children’s books with explicit memory representations] (ICLR) [Dataset](https://github.com/facebookresearch/ParlAI/tree/main/parlai/tasks/cbt)
* WhoDidWhat  - [Whodid What: ALarge-Scale Person-Centered Cloze Dataset] (EMNLP) [Dataset](https://tticnlp.github.io/who_did_what/)
* MCTest - [MCTest: A Challenge Dataset for the Open-Domain Machine Comprehension of Text ] (EMNLP) [Dataset](https://github.com/mcobzarenco/mctest/tree/master)
* RACE - [RACE: Large-scale ReAding Comprehension Dataset From Examinations] (EMNLP) [Dataset](https://www.cs.cmu.edu/~glai1/data/race/)
* RACE-C - [A New Multi-choice Reading Comprehension Dataset for Curriculum Learning] (PMLR) [Dataset](https://github.com/mrcdata/race-c)
* DREAM - [DREAM: A Challenge Data Set and Models for Dialogue-Based Reading Comprehension] (TACL) [Dataset](https://dataset.org/dream/)
* CosmosQA - [Cosmos QA: Machine Reading Comprehension with Contextual Commonsense Reasoning] (EMNLP) [Dataset](https://wilburone.github.io/cosmos/)
* ReClor - [ReClor: A Reading Comprehension Dataset Requiring Logical Reasoning] (ICLR) [Dataset](https://whyu.me/reclor/)
* QuAIL - [Getting Closer to AI Complete Question Answering: A Set of Prerequisite Real Tasks] (AAAI) [Dataset](https://github.com/text-machine-lab/quail)
* MovieQA - [MovieQA: Understanding Stories in Movies Through Question-Answering] (CVPR) [Dataset](https://metatext.io/datasets/movieqa)
* Visual7W - [Visual7W: Grounded Question Answering in Images] (CVPR) [Dataset](https://ai.stanford.edu/~yukez/visual7w/)
* TQA - [Are You Smarter Than a Sixth Grader? Textbook Question Answering for Multimodal Machine Comprehension] (CVPR) [Dataset](https://allenai.org/data/tqa)
* RecipeQA - [RecipeQA: A Challenge Dataset for Multimodal Comprehension of Cooking Recipes] (EMNLP) [Dataset](https://hucvl.github.io/recipeqa/)
* ScienceQA - [Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering] (NeurIPS) [Dataset](https://scienceqa.github.io/#dataset)
