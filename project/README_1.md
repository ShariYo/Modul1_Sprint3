
# Coursera courses analysis

This project main goal is to analyse coursera courses dataset from various perspectives and visualize some of the data got get better insights.  
Project consists of dataset fetch, raw dataframe preview, data clean, EDA with visuals and summary.


## Data source

Given data source can be found at Kaggle with the link provided below:

```bash
  https://www.kaggle.com/datasets/siddharthm1698/coursera-course-dataset/data
```
    
## Main functions/libraries used for data analysis:

* pandas(pd) - library of pandas functions;  
* numpy(np) - library of numpy functions;  
* matplotlib.pyplot(plt) - library for data visualizations;  
* seaborn(sns) - library for data visualizations;

Main functions:  
* pd.read_csv() - to read a given data source;  
* .duplicated().any() - checks if there are any duplicates;  
* .isna().any() - checks if there are any NaN values;  
* .describe() - brief information about dataframe values;  
* .unique() - gets unique values;  
* .groupby() - groups data by a given column name;  

Visualizations:  
* sns.barplot();  
* sns.histplot();  
* sns.heatmap();  
* sns.boxplot();  
* sns.kdeplot();


