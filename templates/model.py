import pandas as pd
import xgboost as xgb
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as mean_absolute_error 
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_absolute_error as mean_absolute_error 


dataset = pd.read_csv('templates//predictions_dataset.csv')


# split dataset
X = dataset[['average_uk_annual_salary', 'python', 'excel', 'powerbi', 'sql', 'tableau', 'seniority_level', 'industry_category' , 'in_out_london', 'tech_stack_count_group', 'job_title_two']]
y= dataset[['annual_salary']]


X_train, X_test, y_train, y_test = train_test_split(X,y , 
                                   random_state=42,  
                                   test_size=0.25,  
                                   shuffle=True) 

# instantiate model

xgb_model = xgb.XGBRegressor(objective= 'reg:squarederror', 
                             subsample=0.9, 
                             colsample_bytree=0.5,
                             learning_rate= 0.5,
                             max_depth=6,
                             gamma=0,
                             reg_lambda=1.0
                            )

no_transform_columns = ['python', 'excel', 'powerbi', 'sql', 'tableau', 'average_uk_annual_salary']
categorical_columns = ['seniority_level', 'industry_category', 'in_out_london', 'tech_stack_count_group', 'job_title_two']

no_transform_transformer = 'passthrough'

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))  # Apply one-hot encoding to categorical columns
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', no_transform_transformer, no_transform_columns),  # Leave numeric columns as is
        ('cat', categorical_transformer, categorical_columns)  # Apply one-hot encoding to categorical columns
    ],
    remainder='drop'  # Drop any columns not explicitly specified
)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('xgb', xgb_model)  # Assuming xgb_model is your XGBoost model
])

# Fit the model
pipeline.fit(X_train, y_train)

# predictions = pipeline.predict(X_test)

# mae_of_xgboost_tuned = mean_absolute_error(y_test, predictions)
# print(mae_of_xgboost_tuned)

# r2 = r2_score(y_test, predictions)
# print(r2)

# make pickle file
pickle.dump(pipeline, open('model.pkl', 'wb'))
