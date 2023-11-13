# Stress Identification

Dataset: https://www.kaggle.com/datasets/kreeshrajani/human-stress-prediction

The dataset contains data posted on subreddits related to mental health. This dataset contains various mental health problems shared by people about their life. 
Fortunately, this dataset is labelled as 0 and 1, where 0 indicates no stress and 1 indicates stress.

To properly use this document, you must install the following libraries:
```shell
pip install pandas
pip install seaborn
pip install spacy
pip install wordcloud
pip install tqdm
pip install scikit-learn
pip install keras
pip install tensorflow
pip install matplotlib
```
## Description of the Chosen Model

It is simple convolutional neural network (CNN) with following layers:
1. Embedding Layer
2. Convolutional Layer (Conv1D)
3. GlobalMaxPooling1D Layer
4. Dense Layer

## Model usage
1. Install Required Libraries
2. Run the Entire File by Clicking the `Run All` Button
3. In the Last Cell, Locate the `sentence` Variable. Replace the Placeholder Sentence with Your Own Text that You Want to Classify.