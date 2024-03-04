import pandas as pd
data={'StudentID':[1,2,3,4,5,6,7,8],'Grade':['a','b','c','a','c','a','b','c'],
      'Math_Score':[90,85,92,78,88,75,95,80],'English_Score':[88,90,85,78,92,80,85,78]}
df=pd.DataFrame(data)
print("original DataFrame:")
print(df)
contrast_encoded_df=pd.get_dummies(df['Grade'],prefix='Grade',drop_first=True)
print("\nDataFrame after Constrast Encoding:")
print(contrast_encoded_df)