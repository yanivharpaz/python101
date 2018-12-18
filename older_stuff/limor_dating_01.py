from __future__ import print_function
#
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import FunctionTransformer , LabelEncoder
from sklearn.pipeline import Pipeline, FeatureUnion
import numpy as np



input_file_path = r"t:\Users\yaniv\Dropbox\Dropbox\Limor_DS_Workspace\Work\Project_Dating\final_data2.csv"
# dating_orig_df = pd.read_csv(input_file_path, nrows=70, usecols=["topic"])
# df01 = dating_orig_df.dropna(how='all')
# dating_orig_df_is_sale = pd.read_csv(input_file_path, nrows=70, usecols=["is_sale"])

dating_orig_df = pd.read_csv(input_file_path, parse_dates=['lead_date'], usecols=["cid", "age_group", "lead_date",
                                                                                "segment", "user_gender",
                                                       "region_name", "country_name", "ad_group_name", "topic",
                                                       "keyword", "traffic_source_name", "source_join",
                                                       "lead_week", "is_sale"])

dating_not_nan_df = dating_orig_df.dropna(how='all')

# cid = len(dating_not_nan_df['cid'].unique())

# a = dating_not_nan_df.groupby(['cid']).count()

# lead_date_weekday = dating_not_nan_df['lead_date'].dt.weekday_name


# all_sale_df = dating_not_nan_df[dating_not_nan_df['is_sale'] == 'TRUE']





# def get_columns_to_dummies(df):
#     return df[['user_gender', 'source_join', 'is_sale']]
#
#
# columns_to_dummies = FunctionTransformer(func=get_columns_to_dummies, validate=False)
#
# def get_dummies_func(df):
#     return pd.get_dummies(df, drop_first=True)
#
#
# dummies_func = FunctionTransformer(func=get_dummies_func, validate=False)
#
# get_dummies_pipeline = Pipeline([('columns_to_dummies', columns_to_dummies), ('dummies_func', dummies_func)])
#
# data_after_transform = get_dummies_pipeline.fit_transform(dating_orig_df)
#
#
# dating_dummies_df = pd.get_dummies(dating_not_nan_df, drop_first=True, columns=['user_gender', 'source_join', 'is_sale'])

# all_sale_df = dating_dummies_df[dating_dummies_df['is_sale_True'] == 1]
# all_not_sale_df = dating_dummies_df[dating_dummies_df['is_sale_True'] == 0]

#
# aa = all_sale_df['traffic_source_name'].unique()
# bb = all_sale_df['traffic_source_name'].value_counts()

# columns = ["age_group",  "segment", "country_name", "topic",  "traffic_source_name"]
#
# fig = plt.figure()
# for i, column in enumerate(columns):
#     plt.subplot(5, 1, i + 1)
#     (all_sale_df[column].value_counts() / dating_dummies_df[column].value_counts()).plot(kind='bar')
#     plt.xlabel(column)
#     fig.tight_layout()
#     plt.show()


# for i, column in enumerate(columns):
#     fig = plt.figure()
#     plt.subplot(6,1,i+1)
#     (all_sale_df[column].value_counts() / dating_dummies_df[column].value_counts()).plot(kind='bar')
#     plt.xlabel(column)
#     fig.tight_layout()
#     plt.show()




# age_group_bar_plot = all_sale_df['age_group'].value_counts()/dating_dummies_df['age_group'].value_counts()
# age_group_bar_plot.plot(kind='bar')

# dating_dummies_df['traffic_source_name'].value_counts().plot(kind='bar')



#
# def get_columns_to_dummies_user_gender(df):
#     return df['user_gender']
#
#
# columns_to_dummies_user_gender = FunctionTransformer(func=get_columns_to_dummies_user_gender, validate=False)
#
# def get_columns_to_dummies_source_join(df):
#     return df['source_join']
#
#
# columns_to_dummies_source_join = FunctionTransformer(func=get_columns_to_dummies_source_join, validate=False)
#
# def get_columns_to_dummies_is_sale(df):
#     return df['is_sale']
#
#
# columns_to_dummies_is_sale = FunctionTransformer(func=get_columns_to_dummies_is_sale, validate=False)
#
# def get_dummies_func(df):
#     return pd.get_dummies(df, drop_first=True)
#
#
# dummies_func = FunctionTransformer(func=get_dummies_func, validate=False)
#
# get_dummies_pipeline_gender = Pipeline([('columns_to_dummies_user_gender', columns_to_dummies_user_gender),
#                                  ('dummies_func', dummies_func)])
#
# get_dummies_pipeline_source_join = Pipeline([('columns_to_dummies_source_join', columns_to_dummies_source_join),
#                                  ('dummies_func', dummies_func)])
#
# get_dummies_pipeline_is_sale = Pipeline([('columns_to_dummies_is_sale', columns_to_dummies_is_sale),
#                                  ('dummies_func', dummies_func)])
#
# multy_pipeline = FeatureUnion([('get_dummies_pipeline_gender', get_dummies_pipeline_gender),
#                                ('get_dummies_pipeline_source_join', get_dummies_pipeline_source_join),
#                                ('get_dummies_pipeline_is_sale', get_dummies_pipeline_is_sale)])
#
# full_multy_pipeline = multy_pipeline.fit_transform(dating_orig_df)








# def get_len(df):
#     return df.str.len()
#
#
# df02_len = FunctionTransformer(func=get_len, validate=False)
#
#
# def get_column_topic(df):
#     return df['topic']
#
#
# column_topic = FunctionTransformer(func=get_column_topic, validate=False)
#
# # df02 = get_len(df01["topic"])
#
#
# len_pipeline = Pipeline([('column_topic', column_topic), ('df02_len', df02_len)])
#
# prepared_train = len_pipeline.fit_transform(dating_orig_df)



# def get_column_is_sale(df):
#     return df['is_sale']
#
#
# column_is_sale = FunctionTransformer(func=get_column_is_sale, validate=False)
#
#
# def get_dummies_func(df):
#     # c = pd.get_dummies(df, drop_first=True)
#     c = pd.get_dummies(df)
#     return c
#
#
# get_dummies_is_sale = FunctionTransformer(func=get_dummies_func, validate=False)
#
# get_dummies_pipeline = Pipeline([('column_is_sale', column_is_sale), ('get_dummies_is_sale', get_dummies_is_sale)])
# # prepared_get_dummies = get_dummies_pipeline.fit_transform(dating_orig_df_is_sale)
# prepared_get_dummies = get_dummies_pipeline.fit_transform(dating_orig_df_test)









# import sys
#
# from sklearn.preprocessing import FunctionTransformer
# from sklearn.pipeline import Pipeline, FeatureUnion
# from sklearn.preprocessing import StandardScaler, MaxAbsScaler, Binarizer
#
#
# # def main(argv):
#
# def get_dating_dummies(df, columns):
#     new_is_dummy_df = pd.get_dummies(df, columns=columns)
#     # return new_is_dummy_df[['segment']]
#     return new_is_dummy_df
#
#
#
#
# print("Hello...")
# input_file_path = r"t:\Users\yaniv\Dropbox\Dropbox\Limor_DS_Workspace\Work\Project_Dating\final_data2.csv"
# dating_orig_df = pd.read_csv(input_file_path, nrows=70, usecols=["cid", "age_group", "lead_date", "segment", "user_gender",
#                                                        "region_name", "country_name", "ad_group_name", "topic",
#                                                        "keyword", "traffic_source_name", "source_join",
#                                                        "lead_week", "is_sale"])
# print(len(dating_orig_df))
# dating_orig_df.dropna(how='all')
# print(len(dating_orig_df))
#
# # dating_dummy01 = pd.get_dummies(dating_orig_df, columns=["is_sale"])
#
# xxx = get_dating_dummies(dating_orig_df["is_sale"], columns=["is_sale"])
#
#
# # ss_selector = FunctionTransformer(func=get_dating_dummies, validate=False)
# # ss_pipeline = Pipeline([('ss_selector', ss_selector), ('ss', StandardScaler())])
# # prep01 = ss_pipeline.transform(dating_orig_df)
#
# # if __name__ == "__main__":
# #     main(sys.argv)
#
