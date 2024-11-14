
import numpy as np
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, ConfusionMatrixDisplay, roc_curve, auc, RocCurveDisplay
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.utils.class_weight import compute_class_weight
from imblearn.over_sampling import SMOTE

dataset = "https://raw.githubusercontent.com/ssuelims/Datasets/refs/heads/main/Dados.csv"
df = pd.read_csv(dataset,sep=";")
df.drop(columns=["Unnamed: 19","Carimbo de data/hora"],inplace=True)
df["Qual a sua forma de trabalho?"].fillna("não trabalho",inplace=True)
df["A quantos anos você trabalha?"].fillna(0,inplace=True)
mapping = {
    "Área de Vendas": "Área de atendimento",
    "Atendimento": "Área de atendimento",
    "Comércio": "Área de atendimento",
    "Central de compras": "Área de atendimento",
    "Auxiliar de serviços Gerais": "Área de atendimento",
    "Área Alimenticia": "Área de atendimento",
    "Autônomo": "Área de atendimento",
    "Área de TI": "Área de TI",
    "Sistema S": "Área de TI",
    "Diretor de marketing": "Área de TI",
    "Educação": "Área de Educação",
    "Escolar": "Área de Educação",
    "Recursos humanos": "Área de Educação",
    "Área de saúde": "Área serviço público",
    "Administração": "Área serviço público",
    "Área Pública": "Área serviço público",
    "Área Militar": "Área serviço público",
    "Jurídica": "Área serviço público",
    "Advogada": "Área serviço público",
    "Contabilidade": "Área serviço público",
    "não trabalho": "não trabalho",
    "Logística": "Área de logística",
    "Admistrativo": "Área administrativa",
    "Comercio": "Área de comércio",
    "Área Publica": "Área serviço público",
    "Área de Saude": "Área de saúde"
}

df["Qual o setor do seu trabalho?"] = df["Qual o setor do seu trabalho?"].str.strip()

df["Qual o setor do seu trabalho?"] = df["Qual o setor do seu trabalho?"].replace(mapping)
problemas = {
    "Ansiedade":"Ansiedade",
    "Depressão":"Depressão",
    "Nunca percebi nenhum problema": "Nunca percebi nenhum problema",
    "Sindrome de Pânico":"Ansiedade",
    "Burnout": "Burnout",
    "Nenhum ": "Nunca percebi nenhum problema",
    "Ansiedade ":"Ansiedade",
    "Os três primeiros": "Ansiedade",
    "autismo": "Ansiedade",
    "TDAH ANSIEDADE " : "Ansiedade",
    "Depressão, Ansiedade, Sindrome de Pânico":"Depressão",
}

df["Você se identifica ou já se identificou com algum destes problemas mentais ou já teve casos com as caracteristicas destes?"] = df["Você se identifica ou já se identificou com algum destes problemas mentais ou já teve casos com as caracteristicas destes?"].replace(problemas)
df_binario = pd.get_dummies(df.drop(columns="Você se identifica ou já se identificou com algum destes problemas mentais ou já teve casos com as caracteristicas destes?"), drop_first=True)


train_x = df_binario
train_y = df["Você se identifica ou já se identificou com algum destes problemas mentais ou já teve casos com as caracteristicas destes?"]
X_train, X_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.2, random_state=42)

model = LinearSVC(max_iter=2000)

smote = SMOTE(random_state=42)
X_balanced, y_balanced = smote.fit_resample(train_x, train_y)

model.fit(X_balanced,y_balanced)
pred = model.predict(X_test)

def predict(dados):
    prev = model.predict(dados)
    return prev
def accuracia(dados):
    prob = model.predict(dados)
    acc = accuracy_score(y_test, prob)
    return acc