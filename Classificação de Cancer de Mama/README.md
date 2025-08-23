
# 🩺 Classificação de Câncer de Mama - Machine Learning para Diagnóstico Médico

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3%2B-orange)](https://scikit-learn.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.7%2B-green)](https://xgboost.readthedocs.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📊 Coleta de Dados

- **Fonte**: [Breast Cancer Wisconsin Dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))  
- **Total de amostras**: 569  
- **Features**: 30 variáveis numéricas extraídas de imagens de núcleos celulares  
- **Classes alvo**:  
  - Benigno (B) → 357 casos (62,7%)  
  - Maligno (M) → 212 casos (37,3%)  

### Pré-processamento realizado:
1. Remoção de colunas irrelevantes (`id`, `Unnamed: 32`)  
2. Codificação da variável alvo (`B` = 0, `M` = 1)  
3. Seleção das **top 10 features mais correlacionadas**  
4. Tratamento de **outliers com IQR**  
5. **Padronização** com `StandardScaler`  
6. **Redução de dimensionalidade (PCA)** garantindo ≥95% de variância explicada  

---

## 🤖 Modelagem

### Passos do pipeline:
1. **Divisão Treino/Teste**: 70% / 30% (estratificado)  
2. **Balanceamento**: Aplicação de **SMOTE** apenas nos dados de treino  
3. **Modelos testados**:
   - Regressão Logística  
   - Random Forest  
   - XGBoost  
   - Ensemble (Voting, Stacking e Calibrated Models)  

### Avaliação:
- **Métrica prioritária**: **Recall** (importante para identificar todos os casos malignos)  
- Outras métricas utilizadas: **Accuracy, Precision, F1-score e AUC**  

---

## 📈 Resultados

### Comparação Final dos Modelos (ordenados por Recall):
| Modelo                | Accuracy |   AUC  | Recall |
|------------------------|----------|--------|--------|
| Logistic Regression    | 0.9103   | 0.9924 | 1.0000 |
| Random Forest          | 0.9744   | 0.9962 | 0.9796 |
| Voting Classifier      | 0.9551   | 0.9950 | 0.9796 |
| Stacking Classifier    | 0.9615   | 0.9952 | 0.9796 |
| Calibrated Model       | 0.9679   | 0.9969 | 0.9796 |
| XGBoost                | 0.9423   | 0.9924 | 0.9592 |

---

## 🏆 Conclusões

- 🎯 **Modelos com Recall perfeito (100%)**:  
  - Regressão Logística detectou **todos os casos malignos**.  

- 🏆 **Melhor Modelo (Recall + AUC)**:  
  - **Logistic Regression** → Recall = 1.000 e AUC = 0.9924  
  - Apesar da menor acurácia em relação a Random Forest e outros ensembles, é o modelo **mais indicado em aplicações médicas**, pois garante **nenhum falso negativo** (não deixa passar câncer sem diagnóstico).  

- ✅ Este estudo demonstra a importância de escolher a métrica adequada (nesse caso, **Recall**) em problemas de saúde, onde um falso negativo pode ter consequências graves.  

---

📌 **Próximos passos sugeridos**:
- Testar mais técnicas de seleção de features (ex: RFE, SHAP Values).  
- Avaliar outros algoritmos de ensemble.  
- Realizar validação cruzada estratificada para maior robustez.  

---

👨‍💻 Desenvolvido por **Emerson Martins**  
📅 Projeto de Portfólio em Ciência de Dados  
