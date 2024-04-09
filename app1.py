#import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

st.set_page_config(
    page_title="Панели идоракунии маълумот ДТТ дар вақти воқеӣ",
    page_icon="✅",
    layout="wide",
)

# read csv from a github repo
df = pd.read_csv('tahlilv.csv')

# dashboard title
st.title("Панели идоракунии маълумот дар вақти воқеӣ")

# top-level filters
job_filter = st.selectbox("ном ва насаби донишчу", pd.unique(df["name"]))

# creating a single-element container
placeholder = st.empty()

# dataframe filter
df = df[df["name"] == job_filter]

# near real-time / live feed simulation
for seconds in range(200):
    df["MB2"] = df["MB2"] #* np.random.choice(range(1, 5))
    df["sumi_shart"] = df["sumi_shart"] #* np.random.choice(range(1, 5))

    # creating KPIs
    avg_age = np.mean(df["MB2"])

    count_married = str(
        df[(df["su"] == "su")]["su"].count()
        #+ np.random.choice(range(1, 30))
    )

    balance = np.mean(df["sumi_shart"])

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(
            label="дарс шикани ⏳",
            value=round(avg_age),
           # delta=round(avg_age) #- 10,
        )

        kpi2.metric(
            label="раками телофон",
            value=int(df['number']),
            #delta=-10 + count_married,
        )

        kpi3.metric(
            label="суми шартномаро супоридаги ",
            value=f" {round(balance, 2)} ",
            #delta=-round(balance / count_married) * 100,
        )

        # create two columns for charts
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(
                data_frame=df, y="MB2", x="su"
            )
            st.write(fig)

        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x="MB2")
            st.write(fig2)

        st.markdown("### Detailed Data View")
        st.dataframe(df)
        #time.sleep(1)

