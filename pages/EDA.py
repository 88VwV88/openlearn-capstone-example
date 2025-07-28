import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better visualizations
plt.style.use("seaborn-v0_8")
sns.set_palette("husl")

# Configure plot settings
plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 12

survey = pd.read_csv("datasets/cleaned_survey.csv")

st.title("Data Analysis, Observations & Inferences")

st.divider()

st.header("Dataset Anomalies")
st.markdown("""
The dataset being the result of a survey, \
clearly had a lot of anomalies like the range problems \
for the numerical data and outliers. Also the optinal user \
specified values such as `Gender` suffer from extreme number \
of non-standard terminologies which needed cleaning.
""")

st.markdown("""
**Checking for missing values**
This small piece of code helps you visually see what percentage and number of values are missing
""")
st.table(
    pd.DataFrame(
        index=["comments", "state", "work_interfere", "self_employed"],
        data={
            "Missing Count": [1095, 515, 264, 18],
            "Missing Percentage": [86.973789, 40.905481, 20.969023, 1.429706],
        },
    )
)

st.markdown("""
**Checking for outliers**
Numerical columns for outlier analysis: [`Age`, `cleaned_employees`]

`Age`:
- *Total values*: `1251`
- *Outliers*: `32 (2.6%)`
- *Bounds*: `(13.50, 49.50)`
- *Sample outlier values*: `[50, 56, 60, 54, 55]`

`cleaned_employees`:
- *Total values*: `1243`
- *Outliers*: `0 (0.0%)`
- *Bounds*: `(-1087.50, 1852.50)`

Dataset shape after outlier removal: `(1251, 29)`
Original dataset shape: `(1251, 29)`
Rows removed: `0`
""")

st.subheader("Observations:")
st.markdown("""
* Need for range specification for numerical columns in future surveys,
* specification of standard options with inclusive options accounting for the diversity of the surveyee pool, and
* the models need to be fitted with imputation capabilities for handling NaN values.
* The features in the data have a fair amount of outliers as with over `41%` of outliers in the Age column alone.
""")

st.divider()

st.header("Univariate feature analysis")


st.image("images/univariate1.png")
cols = st.columns(3)
with cols[0]:
    st.markdown("""
- Average age of treatment seekers: `32.6`
- Average age of non-treatment seekers: `31.5`
""")
with cols[1]:
    st.markdown("""
Treatment rates by gender:
- *Female*: `69.6%`
- *Male*: `45.4%`
- *Not* Specified: `100.0%`
- *Other*: `80.0%`
""")
with cols[2]:
    st.markdown("""   
Top 5 countries by treatment rate:
- *Croatia*: `100.0%`
- *Denmark*: `100.0%`
- *Japan*: `100.0%`
- *Slovenia*: `100.0%`
- *Moldova*: `100.0%`
""")

st.image("images/univariate1.png")
cols = st.columns(4)
with cols[0]:
    st.markdown("""
Treatment rates by benefits availability:
- *No*: `48.2%`
- *Unknown*: `37.1%`
- *Yes*: 63.8%
""")
with cols[1]:
    st.markdown("""
Treatment rates by remote work:
- *No*: `49.7%`
- *Yes*: `52.6%`
""")
with cols[2]:
    st.markdown("""
Treatment rates by company size:
- `3.0`: `40.1%`
- `15.0`: `50.9%`
- `63.0`: `54.5%`
- `300.0`: `46.3%`
- `750.0`: `58.3%`
- `1001.0`: `52.2%`
""")
with cols[3]:
    st.markdown("""
Treatment rates by work interference:
- *Never*: `14.2%`
- *Often*: `85.0%`
- *Rarely*: `70.5%`
- *Sometimes*: `49.7%`
""")

st.image("images/univariate3.png")
cols = st.columns(4)
with cols[0]:
    st.markdown("""
Treatment rates by family history:
- *Family history No*: `35.4%`
- *Family history Yes*: `74.0%`
""")
with cols[1]:
    st.markdown("""
Treatment rates by supervisor support:
- *No*: `52.3%`
- *Some* of them: `51.6%`
- *Yes*: `48.4%`
""")
with cols[2]:
    st.markdown("""
Treatment rates by coworker support:
- *No*: `45.3%`
- *Some of them*: `50.5%`
- *Yes*: `56.8%`
""")
with cols[3]:
    st.markdown("""
Treatment rates by anonymity protection:
- *No*: `57.8%`
- *Unknown*: `45.3%`
- *Yes*: `60.8%`
""")

st.divider()
st.header("Bivariate Analysis")

st.image("images/bivariate1.png")
st.image("images/bivariate2.png")

st.divider()
st.header("Multivariate Analysis")
st.image("images/multivariate1.png")
st.image("images/multivariate2.png")

st.divider()
st.header("Key Observations & Patterns")

cols = st.columns(2)
with cols[0]:
    st.markdown("""
    - *High-risk threshold*: `18.0`
    - *High-risk group size*: `369 (29.5%)`
    - *Treatment rate in high-risk group*: `44.7%`
    - *Overall treatment rate*: `50.5%`
    """)
with cols[1]:
    st.markdown("""
    High-risk group characteristics:
    - Average age: `31.8`
    - Gender distribution:
        - Male: `313 (84.8%)`
        - Female: `53 (14.4%)`
        - Not Specified: `2 (0.5%)`
        - Other: `1 (0.3%)`
    """)
st.image("images/observations.png")
st.markdown("""
Protective factor impact (difference in treatment rates):
- Care Options: `+27.7` percentage points
- Benefits: `+15.6` percentage points
- Wellness Program: `+9.2` percentage points
- Anonymity: `+2.9` percentage points
- Supervisor Support: `-3.9` percentage points
""")