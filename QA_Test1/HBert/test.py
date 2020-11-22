# coding=gbk
# from transformers.data.metrics.squad_metrics import (
#     compute_predictions_log_probs,
#     compute_predictions_logits,
#     squad_evaluate,
# )


import lawrouge
import os

gold_list = ['王福財於民國99年間經友人介紹及由電腦網際網路認識當時就讀國中1年級之A女，並自同年8月間起2人進而交往成為男女朋友。詎王福財知A女真實年齡係14歲以上，未滿16歲之女子，且縱使A女同意為性行為，亦不得與A女為之，卻仍基於對於14歲以上未滿16歲女子性交之犯意，在未違反A女意願之情況下，分別於100年3月21日上午某時、100年4月6日上午6時40分許，在其位於臺南市○○區○○路3段720巷10號住處房間內，以其陰莖插入A女陰道內之方式，對A女為性交行為2次。嗣因A女之母代號0000-000000A察覺A女行動電話費用暴增有異，經追問緣由，始查悉上情。']
pred_list = ['於100年3月21日上午某時、100年4月6日上午6時40分許，在其位於臺南市○○區○○路3段720巷10號住處房間內，以其陰莖插入A女陰道內之方式，對A女為性交行為2次。嗣因A女之母代號0000-000000A察覺A女行動電話費用暴增有異，經追問緣由，始查悉上情。']

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
# all_hypothesis = ["哈 尔 滨 是 黑 龙 江 的 省 会"]
# all_references = [["哈 工 大 在 哈 尔 滨", "黑 龙 江 太 冷 了"]]
#
# all_hypothesis = ['我', '是', '學', '生']
# all_references = ['學', '生', '是', '我']
#
# scores = evaluator.get_scores(all_hypothesis, all_references)
# print(scores)