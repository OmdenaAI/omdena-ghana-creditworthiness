# Auto-ML Pipeline

## 1. Unsupervised Learning Pipeline
Since we think more features are available to Creedix team that cannot be provided to us, it will be useful to provide them a system to perform unsupervised learning in the future at their discretion.

User Configurable
- Clustering Algorithms
- Metrics
- Features (need to be modified in code)

## 2. Supervised Learning Pipeline
Same reason as above, there might also be target variables available to Creedix in the now/future, we can recommend/demonstrate to them the system for generating accurate models. We only created the notebooks and made the notebooks to demonstrate the auto-ml packages' ease of usage.

Main Benefit
- Automated supervised learning pipeline (__TPOT__ and __auto-sklearn__ packages) aims to take in any dataset
- Will iterate through all ML algorithms to find the near optimal model



| Notebook                                         | Link                                                                                                                                                       | Dataset (Demo)                                                        |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Supervised_Learning_Pipeline(auto-sklearn).ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/125Z8QpJFglSEDIEX2YPa2R2_udmyx5Fj) | [Give Me Some Credit](https://www.kaggle.com/c/GiveMeSomeCredit/data) |
| Supervised_Learning_Pipeline(TPOT).ipynb         | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/12SeY_V-avn2Wgv86MCmUDbW4E43RrB5f) | [Give Me Some Credit](https://www.kaggle.com/c/GiveMeSomeCredit/data) |
| Unsupervised_Learning_Pipeline.ipynb             | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1s1FY0VpQPp5EKUFjtEEDowNd29BtB7SU) | [Give Me Some Credit](https://www.kaggle.com/c/GiveMeSomeCredit/data) |