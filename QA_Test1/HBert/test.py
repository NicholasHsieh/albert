# coding=gbk
# from transformers.data.metrics.squad_metrics import (
#     compute_predictions_log_probs,
#     compute_predictions_logits,
#     squad_evaluate,
# )


import lawrouge
import os

gold_list = ['���ǰװV��']
pred_list = ['���ǰװV��']

files_rouge = lawrouge.FoldersRouge()
scores = files_rouge.get_scores(pred_list, gold_list, avg=True)
print(scores)
print(scores['rouge-1']['r'])
weighted_f1 = 0.2*scores['rouge-1']['f'] + 0.4*scores['rouge-2']['f']+ 0.4*scores['rouge-l']['f']
print('weighted F1-score:', weighted_f1)

# pred_list = ['the cat was found under the bed']
# gold_list = ['the cat was under the bed']
#
# files_rouge = lawrouge.FoldersRouge(CHINESE=False)
# scores = files_rouge.get_scores(pred_list, gold_list, avg=True)
# print(scores)
# weighted_f1 = 0.2*scores['rouge-1']['f'] + 0.4*scores['rouge-2']['f']+ 0.4*scores['rouge-l']['f']
# print('weighted F1-score:', weighted_f1)

# import rouge_zh
#
# evaluator = rouge_zh.Rouge(metrics=['rouge-n'],
#                            max_n=4,
#                            limit_length=True,
#                            length_limit=100,
#                            length_limit_type='words',
#                            alpha=0.5, # Default F1_score
#                            weight_factor=1.2,
#                            stemming=True)
#
# all_hypothesis = ["�� �� �� �� �� �� �� �� ʡ ��"]
# all_references = [["�� �� �� �� �� �� ��", "�� �� �� ̫ �� ��"]]
#
# all_hypothesis = ['��', '��', '�W', '��']
# all_references = ['�W', '��', '��', '��']
#
# scores = evaluator.get_scores(all_hypothesis, all_references)
# print(scores)