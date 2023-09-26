# Classification_Propaganda
Bachelor Thesis of Marius Kiefer

Characteristics of deleted vs. non-deleted Propaganda on Social Media

Disclaimer: Some of the data is not available due to data privacy

# Abstarct

Social Media is used by billions of people every day. Twitter is one of the most well-
known and widely used Social Media Networks. On Twitter, messages can be shared,
thus informing people in the shortest possible time. The simplicity can also be exploited
negatively. The invasion of Ukraine by Russia was accompanied by a wave of propaganda
on Twitter. This wave was captured in data. Yet, the majority of the data collected for
this purpose was deleted. The goal here is to identify features of the data that could be
decisive for a tweet being deleted. The results could not prove that bot created tweets were
subsequently deleted. Using feature extraction and machine learning, it was demonstrated
that the text and the timestamp of a tweet’s publication provide the most information about
the deletion status of a tweet. Four Classifier Models were evaluated using three different
metrics. The results, are not fully conclusive and could potentially be re-examined using
different Feature Extraction Methods, Pretrained Deep Learning Models, or more data.


# Code Structure

`BA_Marius.ipynb`: Notebook with machine learning part

`appendID.py` & `lookfortweet.py`: Files that helped to divide the data into 'deleted' and 'non-deleted'

`data/deleted_ids.txt` & `data/nondeleted_ids.txt`: tweet IDs of projects data
