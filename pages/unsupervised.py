import pandas as pd
import streamlit as st

st.title("Unsupervised goals")

st.divider()
st.header("Dataset overview")

st.markdown("""
The raw dataset being unfit for unsupervised learning, was preprocessed as:
- Removed non-binary features except `Age` and `work_interference`
- Scaling using `StandardScaler` for easier convergence
- Encoding binary 'yes' and 'no' values using mappings
- Computing the `employee_score` and `op_employer` features
""")
st.table(pd.read_csv("datasets/unsupervised_survey.csv").describe())

st.divider()
st.header("Correlation & Sihlouette Analysis")

st.markdown("""
Performing Sihlouette analysis on the dataset the best parameters for the clustering are:
- *K*: `10`
- *n_neighbours*: `15`
- *sihlouette score*: `0.73`
""")

st.markdown("The features are highly correlated as illustrated by this heatmap:")
st.image("images/unsupervised2.png")

st.markdown("The clusters can be illustrated using the UMAP algorithm as:")
st.image("images/unsupervised1.png")

st.markdown("The cluster profiles depict how the clusters fit the various relationships \
between the features and how employees can be clustered into various groups using them: ")
st.image("images/unsupervised3.png")

st.markdown("""
The employees thereforce and be divided into the following groups using the KMeans clustering algorithm:
### Cluster 0: **Supervisor-Reliant Onsite Workers**  
- **Family history**: Low (19%)  
- **Treatment**: None (0%)  
- **Work interference**: Moderate (38%)  
- **Remote work**: None (0%)  
- **Openness to coworkers**: Moderate (46%)  
- **Openness to supervisor**: High (58%)  
- **Openness to employer**: Moderate (40%)  
- **Description**: Onsite workers with minimal mental health history who avoid treatment. Rely heavily on supervisors despite moderate work disruption.  

### Cluster 1: **Treated but Employer-Wary**  
- **Family history**: None (0%)  
- **Treatment**: Universal (100%)  
- **Work interference**: High (60%)  
- **Remote work**: None (0%)  
- **Openness to coworkers**: Moderate (51%)  
- **Openness to supervisor**: Moderate (51%)  
- **Openness to employer**: Low (32%)  
- **Description**: Actively seek treatment despite no family history. Experience high work disruption but distrust employers.  

### Cluster 2: **Remote High-Risk Communicators**  
- **Family history**: High (39%)  
- **Treatment**: Moderate (52%)  
- **Work interference**: High (52%)  
- **Remote work**: All (100%)  
- **Openness to coworkers**: High (53%)  
- **Openness to supervisor**: High (57%)  
- **Openness to employer**: Moderate (37%)  
- **Description**: Remote workers with strong family mental health history. Openly communicate across all levels despite work challenges.  

### Cluster 3: **High-Risk Onsite Survivors**  
- **Family history**: Universal (100%)  
- **Treatment**: Universal (100%)  
- **Work interference**: Severe (65%)  
- **Remote work**: None (0%)  
- **Openness to coworkers**: Low (49%)  
- **Openness to supervisor**: Low (52%)  
- **Openness to employer**: Low (31%)  
- **Description**: Onsite employees with pervasive mental health history. Seek treatment but distrust workplace support amid severe disruption.  

---

### Key Employer Trust Insights  
| Cluster              | Employer Trust | Employer Score |  
|----------------------|----------------|----------------|  
| Supervisor-Reliant   | Moderate (40%) | 0.51           |  
| Treated but Wary     | Low (32%)      | 0.54           |  
| Remote Communicators | Moderate (37%) | 0.51           |  
| High-Risk Survivors  | Low (31%)      | 0.53           |  

**Pattern**: Employees who sought treatment (Clusters 1 & 3) show lowest employer trust, suggesting stigma concerns. Remote workers (Cluster 2) exhibit balanced openness.
""")