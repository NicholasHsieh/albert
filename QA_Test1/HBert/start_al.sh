CURRENT_DIR=`pwd`
export DATA_DIR=$CURRENT_DIR/dataR5
export MODEL_DIR=$CURRENT_DIR/output_DRCD_albert

python run_squad.py \
  --model_type albert \
  --model_name_or_path $MODEL_DIR \
  --do_train \
  --do_eval \
  --do_lower_case \
  --train_file $DATA_DIR/train_400.json \
  --predict_file $DATA_DIR/Test_500.json \
  --per_gpu_train_batch_size 6 \
  --per_gpu_eval_batch_size 6 \
  --learning_rate 1e-5 \
  --num_train_epochs 2.0 \
  --warmup_steps 1000 \
  --max_seq_length 508 \
  --max_query_length 2 \
  --max_answer_length 508 \
  --n_best_size 20 \
  --doc_stride 192 \
  --output_dir output_DRCD_albert_400_R5 \
  --save_steps 10000