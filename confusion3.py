
import streamlit as st
from streamlit_player import st_player
import pandas as pd
import plotly.express as px
import plotly.io as pio
import pymysql
import matplotlib.pyplot as plt

pio.renderers.default = 'browser'

connection = pymysql.connect(
    host="localhost",
    database="phonepe pulse",
    user="root",
    password="98655",

)
cursor = connection.cursor()
df_aggregated_transaction = pd.read_csv(r'pagg_transaction.csv')
df_aggregated_user=pd.read_csv(r'pagg_users.csv')
df_map_transaction=pd.read_csv(r'pmap_transcation.csv')
df_map_user=pd.read_csv(r'pmap_users.csv')
df_top_transaction=pd.read_csv(r'ptop_transcation.csv')
df_top_user=pd.read_csv(r'ptop_users.csv')


st.set_page_config(page_title = "PhonePe",layout="wide")

st.title("📱 PHONEPE PULSE DATA VISUALIZATION ")


choice = st.sidebar.selectbox("phonepe Pulse Dashboard",("Home","Data Visualization", "Data Analysis"))

if choice == "Home":
    col1, col2, col3 = st.columns([1, 1, 2])
    st.subheader("🖊About Phonepe")
    st.write('''The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages,
              there is a payments revolution being driven by the penetration of mobile phones and data.
                PhonePe Pulse is your window to the world of how India transacts with interesting trends,
              deep insights and in-depth analysis based on our data put together by the PhonePe team.''')
    st_player("https://www.youtube.com/watch?v=c_1H6vivsiA&embeds_euri=https%3A%2F%2Fwww.phonepe.com%2F&feature=emb_imp_woyt")
    st.subheader("🔸About Dashboard")
    st.write('''The Dashboard is created based on the data available on phonepe pulse github, the link is below''')
    st.write("Phonepe Pulse [Github](https://github.com/PhonePe/pulse)")
    # st.subheader("App Created By VISHWA PRIYA")
    
    
    st.subheader("🔸Technologies Used")
    st.write("Github Cloning")
    st.write("Python")
    st.write("Pandas")
    st.write("MySQL")
    st.write("Plotly")
    st.write("Streamlit")
elif choice == "Data Visualization":
    options = ["--select--","Top 10 states based on year and amount of transaction","Least 10 states based on year and amount of transaction",
               "Least 10 transactions_type based on states and transaction_amount","Top 10 Registered-users based on States and District(pincode)",
               "Top 10 Districts based on states and amount of transaction","Least 10 Districts based on states and amount of transaction",
               "Least 10 registered-users based on Districts(pincode) and states","Top 10 transactions_type based on states and transaction_amount"]
    select = st.selectbox("Select the option",options)
    if select=="Top 10 states based on year and amount of transaction":
        cursor.execute("SELECT DISTINCT State,Year,sum(Transaction_amount) as Amount FROM top_transaction GROUP BY State,Year ORDER BY Amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Year','Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 states based on year and amount of transaction")
            #st.bar_chart(data=df,x="State",y="Amount")
            fig4 = px.sunburst(df, path=['State', 'Year'], values='Amount',
                               color='Amount', hover_data=['Amount'],
                               color_continuous_scale='Jet',
                               )
            st.plotly_chart(fig4)
            
    elif select=="Least 10 states based on year and amount of transaction":
        cursor.execute("SELECT DISTINCT State,Year,sum(Transaction_amount) as Amount FROM top_transaction GROUP BY State,Year ORDER BY Amount ASC LIMIT 10");
        df1= pd.DataFrame(cursor.fetchall(),columns=['State','Year','Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df1)
        with col2:
            st.title("Least 10 states based on year and amount of transaction")
            st.bar_chart(data=df1,x="State",y="Amount")
    elif select=="Least 10 transactions_type based on states and transaction_amount":
        cursor.execute("SELECT DISTINCT State,Transaction_type,sum(Transaction_amount) as Amount FROM aggregated_transaction GROUP BY State,Transaction_type ORDER BY Amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_type','Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 transactions_type based on states and transaction_amount")
            #st.bar_chart(data=df,x="State",y="Amount")
            fig = px.bar(df, x='State', y='Amount',color="Transaction_type",
                 color_continuous_scale="Viridis") 
            st.plotly_chart(fig)
            
    elif select=="Top 10 Registered-users based on States and District(pincode)":
        cursor.execute("SELECT DISTINCT State,District,sum(RegisteredUser) as TotalRegUsers FROM top_user GROUP BY State,District ORDER BY TotalRegUsers DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','TotalRegUsers'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Registered-users based on States and District(pincode)")
            st.bar_chart(data=df,x="State",y="District")
    elif select=="Top 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT State,District,sum(amount) as Amount FROM map_transaction GROUP BY State,District ORDER BY Amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts based on Districts and amount of transaction")
    
            fig = px.bar(df, x='State', y='Amount',color="District",
                 color_continuous_scale="Viridis") 
            st.plotly_chart(fig)
    elif select=="Least 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT State,District,sum(amount) as Amount FROM map_transaction GROUP BY State,District ORDER BY Amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 Districts based on Districts and amount of transaction")
            st.bar_chart(data=df,x="District",y="Amount")
    elif select=="Least 10 registered-users based on Districts(pincode) and states":
        cursor.execute("SELECT DISTINCT State,District,sum(RegisteredUser) as TotalRegUsers FROM top_user GROUP BY State,District ORDER BY TotalRegUsers ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','TotalRegUsers'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 registered-users based on Districts and states")
            #st.bar_chart(data=df,x="State",y="District")
            fig4 = px.sunburst(df, path=['State', 'District'], values='TotalRegUsers',
                               color='TotalRegUsers', hover_data=['TotalRegUsers'],
                               color_continuous_scale='Jet',
                               )
            st.plotly_chart(fig4)
    elif select=="Top 10 transactions_type based on states and transaction_amount":
        cursor.execute("SELECT DISTINCT State,Transaction_type,sum(Transaction_amount) as Amount FROM aggregated_transaction GROUP BY State,Transaction_type ORDER BY Amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_type','Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 transactions_type based on states and transaction_amount")
            st.bar_chart(data=df,x="State",y="Amount")
elif choice == "Data Analysis":
    Topic = ["","Transaction-Type","District","Brand","Top-Transactions","Registered-users"]
    choice_topic = st.selectbox("Search by",Topic)

    def type_(type):
        cursor.execute(f"SELECT DISTINCT State,Quater,Year,Transaction_type,Transaction_amount FROM aggregated_transaction WHERE Transaction_type = '{type}' ORDER BY State,Quater,Year");
        df = pd.DataFrame(cursor.fetchall(), columns=['State','Quater', 'Year', 'Transaction_type', 'Transaction_amount'])
        return df
    def type_year(year,type):
        cursor.execute(f"SELECT DISTINCT State,Year,Quater,Transaction_type,Transaction_amount FROM aggregated_transaction WHERE Year = '{year}' AND Transaction_type = '{type}' ORDER BY State,Quater,Year");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Transaction_type', 'Transaction_amount'])
        return df
    def type_state(state,year,type):
        cursor.execute(f"SELECT DISTINCT State,Year,Quater,Transaction_type,Transaction_amount FROM aggregated_transaction WHERE State = '{state}' AND Transaction_type = '{type}' And Year = '{year}' ORDER BY State,Quater,Year");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Transaction_type', 'Transaction_amount'])
        return df
    def district_choice_state(_state):
        cursor.execute(f"SELECT DISTINCT State,Year,Quater,District,amount FROM map_transaction WHERE State = '{_state}' ORDER BY State,Year,Quater,District");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'amount'])
        return df
    def dist_year_state(year,_state):
        cursor.execute(f"SELECT DISTINCT State,Year,Quater,District,amount FROM map_transaction WHERE Year = '{year}' AND State = '{_state}' ORDER BY State,Year,Quater,District");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'amount'])
        return df
    def district_year_state(_dist,year,_state):
        cursor.execute(f"SELECT DISTINCT State,Year,Quater,District,amount FROM map_transaction WHERE District = '{_dist}' AND State = '{_state}' AND Year = '{year}' ORDER BY State,Year,Quater,District");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'amount'])
        return df
    def brand_(brand_type):
        cursor.execute(f"SELECT State,Year,Quater,brands,Percentage FROM aggregated_user WHERE brands='{brand_type}' ORDER BY State,Year,Quater,brands,Percentage DESC");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'brands', 'Percentage'])
        return df
    def brand_year(brand_type,year):
        cursor.execute(f"SELECT State,Year,Quater,brands,Percentage FROM aggregated_user WHERE Year = '{year}' AND brands='{brand_type}' ORDER BY State,Year,Quater,brands,Percentage DESC");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'brands', 'Percentage'])
        return df
    def brand_state(state,brand_type,year):
        cursor.execute(f"SELECT State,Year,Quater,brands,Percentage FROM aggregated_user WHERE State = '{state}' AND brands='{brand_type}' AND Year = '{year}' ORDER BY State,Year,Quater,brands,Percentage DESC");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'brands', 'Percentage'])
        return df
    def transaction_state(_state):
        cursor.execute(f"SELECT State,Year,Quater,sum(Transaction_amount) as Amount FROM top_transaction WHERE State = '{_state}' GROUP BY State,Year,Quater")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Amount'])
        return df
    def transaction_year(_state,_year):
        cursor.execute(f"SELECT State,Quater,sum(Transaction_count) as Count FROM top_transaction WHERE Year = '{_year}' AND State = '{_state}' GROUP BY State,Quater")
        df = pd.DataFrame(cursor.fetchall(), columns=['State','Quater', "Count"])
        return df
    def transaction_quater(_state,_year,_quater):
        cursor.execute(f"SELECT State,Year,District,sum(Transaction_count) as Count FROM top_transaction WHERE Year = '{_year}' AND Quater = '{_quater}' AND State = '{_state}' GROUP BY State,Year,District")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year','District' ,'Count'])
        return df
    def registered_user_state(_state):
        cursor.execute(f"SELECT State,Year,Quater,District,RegisteredUser FROM map_user WHERE State = '{_state}' ORDER BY State,Year,Quater,District")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'RegisteredUser'])
        return df
    def registered_user_year(_state,_year):
        cursor.execute(f"SELECT State,Year,Quater,District,RegisteredUser FROM map_user WHERE Year = '{_year}' AND State = '{_state}' ORDER BY State,Year,Quater,District")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'RegisteredUser'])
        return df
    def registered_user_district(_state,_year,_dist):
        cursor.execute(f"SELECT State,Year,Quater,District,RegisteredUser FROM map_user WHERE Year = '{_year}' AND State = '{_state}' AND District = '{_dist}' ORDER BY State,Year,Quater,District")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'RegisteredUser'])
        return df


    if choice_topic=="Transaction-Type":
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("-- 5 TYPES OF TRANSACTION --")
            transaction_type = st.selectbox("search by", ["Choose an option", "Peer-to-peer payments",
                                                          "Merchant payments", "Financial Services",
                                                          "Recharge & bill payments", "Others"], 0)
        with col2:
            st.subheader("-- 5 YEARS --")
            choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
        with col3:
            st.subheader("-- 36 STATES --")
            menu_state = ["", 'uttar-pradesh', 'jharkhand', 'puducherry', 'rajasthan', 'odisha', 'nagaland',
                          'chandigarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'assam', 'haryana', 'jammu-&-kashmir',
                          'tamil-nadu', 'himachal-pradesh', 'ladakh', 'bihar', 'maharashtra', 'uttarakhand',
                          'karnataka', 'lakshadweep', 'andhra-pradesh', 'sikkim', 'madhya-pradesh', 'mizoram',
                          'kerala', 'manipur', 'arunachal-pradesh', 'andaman-&-nicobar-islands', 'delhi', 'tripura',
                          'chhattisgarh', 'meghalaya', 'goa', 'west-bengal', 'telangana', 'gujarat', 'punjab']
            choice_state = st.selectbox("State", menu_state, 0)

        if transaction_type:
            col1,col2,col3, = st.columns(3)
            with col1:
                st.subheader(f'{transaction_type}')
                st.write(type_(transaction_type))
        if transaction_type and choice_year:
            with col2:
                st.subheader(f' in {choice_year}')
                st.write(type_year(choice_year,transaction_type))
        if transaction_type and choice_state and choice_year:
            with col3:
                st.subheader(f' in {choice_state}')
                st.write(type_state(choice_state,choice_year,transaction_type))

    if choice_topic=="District":
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("-- 36 STATES --")
            menu_state = ["", 'uttar-pradesh', 'jharkhand', 'puducherry', 'rajasthan', 'odisha', 'nagaland',
                          'chandigarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'assam', 'haryana', 'jammu-&-kashmir',
                          'tamil-nadu', 'himachal-pradesh', 'ladakh', 'bihar', 'maharashtra', 'uttarakhand',
                          'karnataka', 'lakshadweep', 'andhra-pradesh', 'sikkim', 'madhya-pradesh', 'mizoram',
                          'kerala', 'manipur', 'arunachal-pradesh', 'andaman-&-nicobar-islands', 'delhi', 'tripura',
                          'chhattisgarh', 'meghalaya', 'goa', 'west-bengal', 'telangana', 'gujarat', 'punjab']
            choice_state = st.selectbox("State", menu_state, 0)
        with col2:
            st.subheader("-- 5 YEARS --")
            choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
        with col3:
            st.subheader("-- SELECT DISTRICTS --")
            district = st.selectbox("search by", df_map_transaction["District"].unique().tolist())
        if choice_state:
            col1,col2,col3 = st.columns(3)
            with col1:
                st.subheader(f'{choice_state}')
                st.write(district_choice_state(choice_state))
        if choice_year and choice_state:
            with col2:
                st.subheader(f'in {choice_year} ')
                st.write(dist_year_state(choice_year,choice_state))
        if district and choice_state and choice_year:
            with col3:
                st.subheader(f'in {district} ')
                st.write(district_year_state(district,choice_year,choice_state))

    if choice_topic=="Brand":
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("-- TYPES OF BRANDS --")
            mobiles = ["",'Xiaomi', 'Vivo', 'Samsung', 'Oppo', 'Realme', 'Apple', 'Huawei', 'Motorola', 'Tecno', 'Infinix',
                       'Lenovo', 'Lava', 'OnePlus', 'Micromax', 'Asus', 'Gionee', 'HMD Global', 'COOLPAD', 'Lyf',
                       'Others']
            brand_type = st.selectbox("search by",mobiles, 0)
        with col2:
            st.subheader("-- 5 YEARS --")
            choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
        with col3:
            st.subheader("-- 36 STATES --")
            menu_state = ["", 'uttar-pradesh', 'jharkhand', 'puducherry', 'rajasthan', 'odisha', 'nagaland',
                          'chandigarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'assam', 'haryana', 'jammu-&-kashmir',
                          'tamil-nadu', 'himachal-pradesh', 'ladakh', 'bihar', 'maharashtra', 'uttarakhand',
                          'karnataka', 'lakshadweep', 'andhra-pradesh', 'sikkim', 'madhya-pradesh', 'mizoram',
                          'kerala', 'manipur', 'arunachal-pradesh', 'andaman-&-nicobar-islands', 'delhi', 'tripura',
                          'chhattisgarh', 'meghalaya', 'goa', 'west-bengal', 'telangana', 'gujarat', 'punjab']
            choice_state = st.selectbox("State", menu_state, 0)

        if brand_type:
            col1,col2,col3, = st.columns(3)
            with col1:
                st.subheader(f'{brand_type}')
                st.write(brand_(brand_type))
        if brand_type and choice_year:
            with col2:
                st.subheader(f' in {choice_year}')
                st.write(brand_year(brand_type,choice_year))
        if brand_type and choice_state and choice_year:
            with col3:
                st.subheader(f' in {choice_state}')
                st.write(brand_state(choice_state,brand_type,choice_year))

    if choice_topic=="Top-Transactions":
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("-- 36 STATES --")
            menu_state = ["", 'uttar-pradesh', 'jharkhand', 'puducherry', 'rajasthan', 'odisha', 'nagaland',
                          'chandigarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'assam', 'haryana', 'jammu-&-kashmir',
                          'tamil-nadu', 'himachal-pradesh', 'ladakh', 'bihar', 'maharashtra', 'uttarakhand',
                          'karnataka', 'lakshadweep', 'andhra-pradesh', 'sikkim', 'madhya-pradesh', 'mizoram',
                          'kerala', 'manipur', 'arunachal-pradesh', 'andaman-&-nicobar-islands', 'delhi', 'tripura',
                          'chhattisgarh', 'meghalaya', 'goa', 'west-bengal', 'telangana', 'gujarat', 'punjab']
            choice_state = st.selectbox("State", menu_state, 0)
        with col2:
            st.subheader("-- 5 YEARS --")
            choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
        with col3:
            st.subheader("--4 Quaters --")
            menu_quater = ["", "1", "2", "3", "4"]
            choice_quater = st.selectbox("Quater", menu_quater, 0)

        if choice_state:
            with col1:
                st.subheader(f'{choice_state}')
                st.write(transaction_state(choice_state))
        if choice_state and choice_year:
            with col2:
                st.subheader(f'{choice_year}')
                st.write(transaction_year(choice_state,choice_year))
        if choice_state and choice_quater:
            with col3:
                st.subheader(f'{choice_quater}')
                st.write(transaction_quater(choice_state,choice_year,choice_quater))

    if choice_topic=="Registered-users":
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("-- 36 STATES --")
            menu_state = ["", 'uttar-pradesh', 'jharkhand', 'puducherry', 'rajasthan', 'odisha', 'nagaland',
                          'chandigarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'assam', 'haryana', 'jammu-&-kashmir',
                          'tamil-nadu', 'himachal-pradesh', 'ladakh', 'bihar', 'maharashtra', 'uttarakhand',
                          'karnataka', 'lakshadweep', 'andhra-pradesh', 'sikkim', 'madhya-pradesh', 'mizoram',
                          'kerala', 'manipur', 'arunachal-pradesh', 'andaman-&-nicobar-islands', 'delhi', 'tripura',
                          'chhattisgarh', 'meghalaya', 'goa', 'west-bengal', 'telangana', 'gujarat', 'punjab']
            choice_state = st.selectbox("State", menu_state, 0)
        with col2:
            st.subheader("-- 5 YEARS --")
            choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
        with col3:
            st.subheader("-- SELECT DISTRICTS --")
            district = st.selectbox("search by", df_map_transaction["District"].unique().tolist())

        if choice_state:
            with col1:
                st.subheader(f'{choice_state}')
                st.write(registered_user_state(choice_state))
        if choice_state and choice_year:
            with col2:
                st.subheader(f'{choice_year}')
                st.write(registered_user_year(choice_state,choice_year))
        if choice_state and choice_year and district:
            with col3:
                st.subheader(f'{district}')
                st.write(registered_user_district(choice_state,choice_year,district))


    