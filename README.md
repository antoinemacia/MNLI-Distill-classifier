# MNLI text classifier distillation for bugs prediciton

## What is this

Predicts wether a statement is a feature request, issue/bug or question

This model was trained using the [**Zero-shot classifier distillation**](https://github.com/huggingface/transformers/tree/main/examples/research_projects/zero-shot-distillation) method
with the [BART-large-mnli](https://huggingface.co/facebook/bart-large-mnli) model as teacher model, to train a classifier on Github issues from the [Github Issues Prediction dataset](https://www.kaggle.com/datasets/anmolkumar/github-bugs-prediction)

HG: https://huggingface.co/AntoineMC/distilbart-mnli-github-issues

### Resources

* Zero-shot classifier distillation extracted from https://github.com/huggingface/transformers/tree/main/examples/research_projects/zero-shot-distillation
* Dataset of bugs from https://www.kaggle.com/datasets/anmolkumar/github-bugs-prediction (gpl 2.0)

## How was it trained

* 15k of Github issues titles ("unlabeled_titles_simple.txt")
* Hypothesis used: "This request is a {}"
* Teacher model used: valhalla/distilbart-mnli-12-1
* Studend model used: distilbert-base-uncased

See [this notebook](https://www.kaggle.com/code/antoinemacia/zero-shot-classifier-for-bug-analysis/edit) for more info on feature engineering choice made

### Results

Agreement of student and teacher predictions: **94.82%**

## How to use

Hosted on HG: https://huggingface.co/AntoineMC/distilbart-mnli-github-issues

## How to train using your own dataset
* Download training dataset from https://www.kaggle.com/datasets/anmolkumar/github-bugs-prediction
* Modify and run convert.py, updating the paths to convert to a CSV
* Run distill.py with the csv file (see [here](https://github.com/huggingface/transformers/tree/main/examples/research_projects/zero-shot-distillation) for more info)

## Acknowledgements

* Joe Davison and his article on [Zero-Shot Learning in Modern NLP](https://joeddav.github.io/blog/2020/05/29/ZSL.html)
* Jeremy Evans and his notebook on [Iterate like a grandmaster](https://www.kaggle.com/code/antoinemacia/iterate-like-a-grandmaster)