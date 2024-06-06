import pickle
import pandas as pd
import streamlit as st 


#Load model + enc
with open('best_model_xgb.pkl', 'rb') as file_1:
  model_best = pickle.load(file_1)

with open('encoder.pkl', 'rb') as file_2:
  enc_inf = pickle.load(file_2)

def run():
    with st.form(key='IntelliBuy'):
        
        administrative = st.number_input('Administrative', value=0, min_value=0)
        administrative_duration = st.number_input('Administrative Duration', value=0.0, min_value=0.0, step=0.01)
        informational = st.number_input('Informational', value=0, min_value=0)
        informational_duration = st.number_input('Informational Duration', value=0.0, min_value=0.0, step=0.01)
        product_related = st.number_input('Product Related', value=0, min_value=0)
        product_related_duration = st.number_input('Product Related Duration', value=0.0, min_value=0.0, step=0.01)
        bounce_rates = st.number_input('Bounce Rates', value=0.0, min_value=0.0, step=0.0001)
        exit_rates = st.number_input('Exit Rates', value=0.0, min_value=0.0, step=0.0001)
        page_values = st.number_input('Page Values', value=0.0, min_value=0.0, step=0.0001)
        special_day = st.number_input('Special Day', value=0.0, min_value=0.0, max_value=1.0, step=0.1)
        month_mapping = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'June':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
        month = st.selectbox('Month', options=list(month_mapping.keys()))
        operating_systems = st.number_input('Operating Systems', value=1, min_value=1, max_value=8)
        browser  = st.number_input('Browser', value=1, min_value=1, max_value=13)
        region = st.number_input('Region', value=1, min_value=1, max_value=9)
        traffic_type = st.number_input('Traffic Type', value=1, min_value=1, max_value=20)
        visitor_type = st.selectbox('Visitor Type', options=['Returning_Visitor', 'New_Visitor', 'Other'])
        weekend = st.selectbox('Weekend', options=[True, False])
        
        submitted = st.form_submit_button(label='Predict')

    month_number = month_mapping[month]

    data_inf = {'Administrative': administrative,
        'Administrative_Duration': administrative_duration,
        'Informational': informational,
        'Informational_Duration': informational_duration,
        'ProductRelated': product_related,
        'ProductRelated_Duration': product_related_duration,
        'BounceRates': bounce_rates,
        'ExitRates': exit_rates,
        'PageValues': page_values,
        'SpecialDay': special_day,
        'Month': month_number,
        'OperatingSystems': operating_systems,
        'Browser': browser,
        'Region': region,
        'TrafficType': traffic_type,
        'VisitorType': 'visitor_type',
        'Weekend': weekend,
    }

    if submitted:
        data_inf = pd.DataFrame([data_inf])

        

        # Encoding
        data_inf_cat = enc_inf.transform(data_inf[['VisitorType','Weekend']])
        # Get nama fitur yang sesuai
        fn = enc_inf.get_feature_names_out()
        # Konversi hasil transformasi ke DataFrame yang baru
        data_inf_cat_enc = pd.DataFrame(data_inf_cat.toarray(), columns=fn)

        # Scaler
        data_inf = data_inf.drop(['VisitorType','Weekend'], axis = 1)

        data_inf_final = pd.concat([data_inf, data_inf_cat_enc], axis=1)

        # Predict
        y_pred_inf = model_best.predict(data_inf_final)

        prediction_result = 'False / Not Purchasing' if y_pred_inf == 0 else 'True / Purchasing'
        st.write('## prediction categories : ', str(int(y_pred_inf)))
        st.write('## prediction categories (str) : ', prediction_result)

if __name__ == '__main__':
    run()