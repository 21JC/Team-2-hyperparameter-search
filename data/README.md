# README

Anonymized Uber Automatic Hyperparameter Search Dataset that contains 501 Studies and 3725 Trials.
All Trials are trained using XGBoost regression.

## features_data

Description: Contains information on the training dataset that went into the model.
	:data_source = name of the hive table we extracted the training dataset from
	:feature_names = list of feature names that went into the model
	:data_start_date = the hive table is partitioned by date. the initial raw training set is defined by [start_date, end_date]
	:data_end_date = the hive table is partitioned by date. the initial raw training set is defined by [start_date, end_date]
	:study_id = corresponding Study ID

## study_level_data

Description: Contains information on the Study/Hyperparameter Tuning configuration.
	:study_id = corresponding Study ID
	:max_trials = maximum number of Trials to run in this Study before we terminate
	:evalution_metric = evaluation metric used to evalute the performance of each Trial candidate

## hyperparams_data

Description: Contains information on the hyperparameter values suggested for each Trial.
	:parent_study_id = corresponding Study ID that this Trial belongs to
	:trial_id = corresponding Trial ID
	:hyperparameters = the set of hyperparameter values used to train this Trial

## learning_summaries_data

Description: Contains the training and test learning summaries (learning curves) for each Trial.
	:train_summaries: points on the train learning curve (final point is the final train performance of this Trial)
	:test_summaries: points on the test learning curve (final point is the final test performance of this Trial)
	:parent_study_id = corresponding Study ID that this Trial belongs to
	:trial_id = corresponding Trial ID
