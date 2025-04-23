import pandas as pd
from scipy.stats import ttest_ind

# Load and clean dataset
df = pd.read_csv("data/social_media_stress.csv")
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df.dropna(subset=["Age"], inplace=True)

# Group definitions
group1 = df[df["Dominant_Emotion"].isin(["Anxiety", "Sadness"])]
group2 = df[~df["Dominant_Emotion"].isin(["Anxiety", "Sadness"])]

# Perform independent t-tests
msg_test = ttest_ind(group1["Messages_Sent_Per_Day"], group2["Messages_Sent_Per_Day"])
cmt_test = ttest_ind(group1["Comments_Received_Per_Day"], group2["Comments_Received_Per_Day"])

# Print results
print("Messages Sent Per Day: t =", round(msg_test.statistic, 4), ", p =", round(msg_test.pvalue, 4))
print("Comments Received Per Day: t =", round(cmt_test.statistic, 4), ", p =", round(cmt_test.pvalue, 4))
