import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

from sklearn.pipeline import Pipeline, FeatureUnion
# from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score


class GetCategorical(BaseEstimator, TransformerMixin):
    """
    Split into categories
    """
    def __init__(self, colname, bins):
        self.colname = colname
        self.bins = bins

    def fit(self, X, y=None):
        self.labels = ['{}-{}'.format(low, high) for low, high in zip(self.bins[:-1], self.bins[1:])]
        return self

    def transform(self, X, y=None):
        X_copy = X.copy()
        binned = pd.cut(X_copy[self.colname],
                        bins=self.bins,
                        labels=self.labels,
                        include_lowest=True)
        X_copy[self.colname] = binned.astype(str)
        return X_copy


class Binarizer(BaseEstimator, TransformerMixin):
    """
    Turn column category data into binary (1 or 0)
    """
    def __init__(self, colname, drop_first):
        self.colname = colname
        self.drop_first = drop_first

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        dummies = pd.get_dummies(X[self.colname],
                                prefix = self.colname,
                                columns = [self.colname],
                                drop_first = self.drop_first)
        X_no_col = X.drop(self.colname, axis=1, inplace=False)
        X_with_dummies = X_no_col.join(dummies)
        return X_with_dummies


def main():

    # ---------------------------
    # load the data
    # ---------------------------
    input_file_path = r"T:\Users\yaniv\Dropbox\Dropbox\Limor_DS_Workspace\Work\Project_Dating\final_data2.csv"
    dating_orig_df = pd.read_csv(input_file_path, parse_dates=['lead_date'], usecols=["age_group",
                                                                                      "lead_date",
                                                                                      "user_gender",
                                                                                      "ad_group_name",
                                                                                      "source_join",
                                                                                      "is_sale"])

    # ---------------------------
    # initial cleanup of rows
    # ---------------------------
    dating_orig_df = dating_orig_df.dropna(how='all')
    dating_orig_df.dropna(subset=['ad_group_name'], inplace=True)

    # --------------------------------------
    # initial preparation of data to binary
    # --------------------------------------

    # prepare ad_group_name
    dating_orig_df['ad_group_name'] = dating_orig_df['ad_group_name'].map(
                                          lambda x: 1 if 'free' in x else 1 if 'Cheap' in x else 0)

    gender_binarizer = Binarizer(colname='user_gender', drop_first=True)
    source_join_binarizer = Binarizer(colname='source_join', drop_first=True)
    is_sale_binarizer = Binarizer(colname='is_sale', drop_first=True)

    # age_gender_binarizer = Binarizer(colname='age_gender', drop_first=False)
    # from_age_binarizer = Binarizer(colname='from age', drop_first=False)

    binarizer_pipeline = Pipeline([('gender_binarizer', gender_binarizer),
                                   ('source_join_binarizer', source_join_binarizer),
                                   ('is_sale_binarizer', is_sale_binarizer)
                                   #                                ,('age_gender_binarizer', age_gender_binarizer),
                                   #                                ('from_age_binarizer', from_age_binarizer)
                                   ])
    # binarizer_pipeline.fit_transform(dating_orig_df).head()

    # --------------------------------------------
    # initial preparation of data to new category
    # -------------------------------------------

    # prepare age groups histogram (use Google's age groups)
    dating_orig_df['from age'], dating_orig_df['to age'] = dating_orig_df['age_group'].str.split('-').str
    # remove '+' from group 80+
    dating_orig_df['from age'] = dating_orig_df['from age'].str.replace('+', '')
    dating_orig_df['to age'] = dating_orig_df['to age'].str.replace('+', '')
    dating_orig_df['from age'] = dating_orig_df['from age'].astype(int)

    # add column google_age_group
    google_age_group = GetCategorical('from age', [18, 24, 34, 44, 54, 64, 100])
    pipeline_age = Pipeline([('google_age_group', google_age_group)])

    # pipeline_age.fit_transform(dating_orig_df).head()

    # ---------------------------
    # add computed columns
    # ---------------------------

    # add column is_weekend
    # 0 = Monday and 6 = Sunday
    lead_date_dayofweek = dating_orig_df['lead_date'].dt.dayofweek
    dating_orig_df['is_weekend'] = lead_date_dayofweek.apply(lambda x: 1 if(x == 5 or x == 6) else 0)

    # ---------------------------
    # transform columns
    # ---------------------------

    all_pipeline = Pipeline([('pipeline_age', pipeline_age),
                             ('binarizer_pipeline', binarizer_pipeline)
                           ])

    dating_orig_df_new = all_pipeline.fit_transform(dating_orig_df)

    # add column age_gender
    dating_orig_df_new['age_gender'] = dating_orig_df_new.apply(
                                       lambda x: '{}_{}'.format(x['from age'], x['user_gender_male']), axis=1)

    dating_orig_df_new = pd.get_dummies(dating_orig_df_new, columns=['age_gender', 'from age'])

    # ---------------------------
    # remove raw columns
    # ---------------------------
    dating_orig_df_new = dating_orig_df_new.drop(['age_group', 'lead_date', 'to age'], axis=1)

    dating_orig_df_new.info()

    print dating_orig_df_new.head()


if __name__ == "__main__":
    main()
