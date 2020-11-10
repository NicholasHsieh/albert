CURRENT_DIR=`pwd`
export SQUAD_DIR=$CURRENT_DIR/dataR5

python run_squad.py \
  --model_type bert \
  --model_name_or_path bert-base-chinese \
  --do_train \
  --do_eval \
  --do_lower_case \
  --train_file $SQUAD_DIR/train_200_X.json \
  --predict_file $SQUAD_DIR/Test_500_X.json \
  --per_gpu_train_batch_size 2 \
  --per_gpu_eval_batch_size 2 \
  --learning_rate 1e-5 \
  --num_train_epochs 2.0 \
  --warmup_steps 1000 \
  --max_seq_length 508 \
  --max_query_length 2 \
  --max_answer_length 508 \
  --n_best_size 20 \
  --doc_stride 192 \
  --output_dir output_bert_200_R5 \
  --save_steps 10000