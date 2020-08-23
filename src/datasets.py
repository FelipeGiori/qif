import numpy as np
import pandas as pd


def load_data_adult():
    adult_columns = ["age", "workclass", "fnlwgt", "education", "education_num", "marital_status", "occupation",
                 "relationship", "race", "sex", "capital_gain", "capital_loss", "hours_per_week",
                 "native_country", "target"]
    df = pd.read_csv("data/adult/adult.data", names=adult_columns)
    df2 = pd.read_csv("data/adult/adult.test", names=adult_columns)
    df = pd.concat([df, df2])
    df.replace(to_replace=" ?", value=np.nan, inplace=True)
    df = df.dropna()
    df['target'] = df['target'].apply(remove_dot)
    df['race_norm'] = df['race'].apply(process_race_adult)
    return df


def load_data_german():
    cols = ['status_existing_checking_account', 'duration', 'credit_history', 'purpose', 'credit_amount', 'savings',
        'present_employment', 'installment_rate', 'sex', 'debtors', 'present_residance_since', 'property', 'age', 
        'installment_plans', 'housing', 'number_existing_credits', 'job', 'number_of_guarantors', 'phone',
        'foreign_worker', 'target']
    german = pd.read_csv("data/german/german.data", sep=" ", names=cols)
    german['sex_norm'] = german['sex'].apply(process_german_sex)
    return german


def load_data_compas():
    compas = pd.read_csv("data/compas/compas_data.csv")
    compas.rename(columns={'two_year_recid':'target'}, inplace=True)
    compas['race_norm'] = compas['race'].apply(process_compas_race)
    return compas


def load_data_breastw():
    df = pd.read_csv("data/breast_w/breast-w_csv.csv")
    df.rename(columns={'Class':'target'}, inplace=True)
    return df


def load_data_hepatitis():
    cols = ['target', 'age', 'sex', 'steroid', 'antivirals', 'fatigue', 'malaise', 'anorexia', 'liver_big',
        'liver_firm', 'spleen_palpable', 'spiders', 'ascites', 'varices', 'bilirubin', 'alk_phostate',
        'sgot', 'albumin', 'protime', 'histology']
    df = pd.read_csv("data/hepatitis/hepatitis.data", names=cols)
    return df


def load_data_breast_tumor():
    cols = ['target', 'age', 'menopause', 'tumor_size', 'inv_nodes', 'node_caps', 'deg_malig', 'breast',
        'breast_quad', 'irradiat']
    df = pd.read_csv("data/breast_tumor/breast-cancer.data", names=cols)
    return df


def load_data_cholesterol():
    cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope',
        'ca', 'thal', 'target']
    df = pd.read_csv("data/cholesterol/processed.cleveland.data", names=cols)
    return df


def load_data_balance_scale():
    cols = ['target', 'left_weight', 'left_distance', 'right_weight', 'right_distance']
    df = pd.read_csv("data/balance_scale/balance-scale.data", names=cols)
    return df


def load_data_heart_disease():
    cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak',
        'slope', 'ca', 'thal', 'target']
    df = pd.read_csv("data/heart_disease/processed.cleveland.data", names=cols)
    return df


def load_data_sensory():
    df = pd.read_csv("data/sensory/sensory.csv")
    return df


def remove_dot(s):
    return s.strip(".")


def process_race_adult(s):
    if(s == " White"):
        return " White"
    else:
        return " Other"
    

def process_german_sex(s):
    if(s == 'A91'):
        return 'male'
    elif(s == 'A92'):
        return 'female'
    elif(s == 'A93'):
        return 'male'
    elif(s == 'A94'):
        return 'male'
    elif(s == 'A95'):
        return 'female'
    

def process_compas_race(s):
    if(s == 'Caucasian'):
        return "Protected"
    else:
        return "Favored"