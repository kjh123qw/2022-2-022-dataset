from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import datasets
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, Seq2SeqTrainingArguments, Seq2SeqTrainer
from transformers import AutoModel, AutoTokenizer
import pandas as pd

import os
import sys
import json
from tqdm import tqdm
from datetime import datetime
import argparse
from omegaconf import OmegaConf

def make_dataset(train_data_path_list, validation_data_path_list):
    '''
    This is a function for making dataset.
    
    Args:
        train_data_path_list (list): The list of the train data files path.
        validation_data_path_list (list): The list of the validation data files path.
    Returns:
        dataset (DatasetDict):
            - train (Dataset):
                - err_sentence (list): Error sentences list.
                - cor_sentence (list): Correction sentences list.
            - validation (Dataset):
                - err_sentence (list): Error sentences list.
                - cor_sentence (list): Correction sentences list.
    '''
    # load files
    loaded_data_dict = {
        'train': {
            'err_sentence': [],
            'cor_sentence': [],
        },
        'validation': {
            'err_sentence': [],
            'cor_sentence': [],
        }
    }
    # train
    for i, train_data_path in enumerate(train_data_path_list):
        with open(train_data_path, 'r') as f:
            _temp_json = json.load(f)
        loaded_data_dict['train']['err_sentence'].extend(list(map(lambda x: x['annotation']['err_sentence'], _temp_json['data'])))
        loaded_data_dict['train']['cor_sentence'].extend(list(map(lambda x: x['annotation']['cor_sentence'], _temp_json['data'])))
        print(f'train data {i} :', len(_temp_json['data']))
    # validation
    for i, validation_data_path in enumerate(validation_data_path_list):
        with open(validation_data_path, 'r') as f:
            _temp_json = json.load(f)
        loaded_data_dict['validation']['err_sentence'].extend(list(map(lambda x: x['annotation']['err_sentence'], _temp_json['data'])))
        loaded_data_dict['validation']['cor_sentence'].extend(list(map(lambda x: x['annotation']['cor_sentence'], _temp_json['data'])))
        print(f'validation data {i} :', len(_temp_json['data']))
    
    dataset_dict = {}
    for _trg in loaded_data_dict.keys():
        dataset_dict[_trg] = datasets.Dataset.from_dict(loaded_data_dict[_trg], split=_trg)
    dataset = datasets.DatasetDict(dataset_dict)
    return dataset

def preprocess_function(df, tokenizer, src_col, tgt_col, max_length):
    '''
    This is a function for preprocessing dataset.
    
    Args:
        df (Dataset): A data in the dataset.
        tokenizer (AutoTokenizer): Model tokenizer.
        src_col (str): Source column name.
        tgt_col (str): Target column name.
        max_length (int): Max length.
    Returns:
        model_inputs (Dataset):
            - input_ids (list): Input data.
            - labels (list): Labeled Data.
    '''
    inputs = df[src_col]
    targets = df[tgt_col]
    model_inputs = tokenizer(
        inputs,
        max_length=max_length,
        truncation=True,
    )
    
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(targets, max_length=max_length, truncation=True)
        
    model_inputs["labels"] = labels['input_ids']
    return model_inputs

def train(config):
    '''
    This is a function for training.
    
    Args:
        config (Dict): Config dict is made by config.yaml
    '''
    # Load model and tokenizer
    _now_time = datetime.now().__str__()
    print(f'[{_now_time}] ====== Model Load Start ======')
    model = AutoModelForSeq2SeqLM.from_pretrained(config.pretrained_model_name)
    tokenizer = AutoTokenizer.from_pretrained(config.pretrained_model_name)
    _now_time = datetime.now().__str__()
    print(f'[{_now_time}] ====== Model Load Finished ======')
    
    # Load data collator
    data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)
    
    # load data and set data
    print(f'[{_now_time}] ====== Data Load Start ======')
    _now_time = datetime.now().__str__()
    dataset = make_dataset(config.train_data_path_list, config.validation_data_path_list)
    _now_time = datetime.now().__str__()
    print(f'[{_now_time}] ====== Data Load Finished ======')
    
    # data preprocessing
    print(f'[{_now_time}] ====== Data Preprocessing Start ======')
    _now_time = datetime.now().__str__()
    dataset_tokenized = dataset.map(lambda d: preprocess_function(d, tokenizer, config.src_col, config.tgt_col, config.max_length), batched=True, batch_size=config.per_device_train_batch_size)
    _now_time = datetime.now().__str__()
    print(f'[{_now_time}] ====== Data Preprocessing Finished ======')
    
    # set training arguments
    training_args = Seq2SeqTrainingArguments(
        output_dir=config.output_dir,
        learning_rate=config.learning_rate,
        per_device_train_batch_size=config.per_device_train_batch_size,
        per_device_eval_batch_size=config.per_device_eval_batch_size,
        num_train_epochs=config.num_train_epochs,
        fp16=config.fp16,
        weight_decay=config.weight_decay,
        do_eval=config.do_eval,
        evaluation_strategy=config.evaluation_strategy,
        warmup_ratio=config.warmup_ratio,
        log_level=config.log_level,
        logging_dir=config.logging_dir,
        logging_strategy=config.logging_strategy,
        logging_steps=config.logging_steps,
        eval_steps=config.eval_steps,
        save_strategy=config.save_strategy,
        save_steps=config.save_steps,
        save_total_limit=config.save_total_limit,
        load_best_model_at_end=config.load_best_model_at_end,
        metric_for_best_model=config.metric_for_best_model,
        greater_is_better=config.greater_is_better,
        dataloader_num_workers=config.dataloader_num_workers,
        group_by_length=config.group_by_length,
        report_to=config.report_to,
        ddp_find_unused_parameters=config.ddp_find_unused_parameters,
     )
    
    # set trainer
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset_tokenized['train'],
        eval_dataset=dataset_tokenized['validation'],
        tokenizer=tokenizer,
        data_collator=data_collator,
    )
    
    # start train
    trainer.train()
    

if __name__ == '__main__':
    '''
    Usage:
        python train.py --config-file config/base-config.yaml
    '''
    # parse inputs args
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-file')
    args = parser.parse_args(sys.argv[1:])
    
    # load config file
    config_file = args.config_file
    config = OmegaConf.load(config_file)
    
    # make save path
    save_path = './data/results'
    os.makedirs(save_path, exist_ok=True)
    
    # set device
    os.environ["CUDA_VISIBLE_DEVICES"] = config.CUDA_VISIBLE_DEVICES
    os.environ['TOKENIZERS_PARALLELISM'] = 'true'
    
    _now_time = datetime.now().__str__()
    print(f'[{_now_time}] ========== Train Start ==========')
    
    # call main method
    print(f'DEVICE : {config.CUDA_VISIBLE_DEVICES}')
    print(f'MODEL NAME : {config.pretrained_model_name}')
    print(f'TRAIN FILE PATH :')
    for _path in config.train_data_path_list:
        print(f' - {_path}')
    print(f'VALIDATION FILE PATH :')
    for _path in config.validation_data_path_list:
        print(f' - {_path}')
    print(f'SAVE PATH : {config.output_dir}')
    train(config)
    
    _now_time = datetime.now().__str__()
    print(f'[{_now_time}] ========== Train Finished ==========')
