Explainable AI research paper + implementation using SHAP on the Iris dataset.

Contents
SHAP_Analysis.py — SHAP feature importance on Iris dataset using Random Forest
PAPER_09_Unraveling_with_AI_Decision_Interpreting_and_Breaking_Down_the_Black_Box_using_SHAP.pdf — Survey paper on SHAP & LIME for XAI

What the Code Does
Trains a RandomForestClassifier on the Iris dataset
Computes SHAP values via TreeExplainer
Plots per-class feature importance + combined stacked bar chart

Tech Stack
Python scikit-learn SHAP matplotlib NumPy

Run
pip install shap scikit-learn matplotlib numpy
python SHAP_Analysis.py

Paper Summary
Reviews SHAP and LIME as XAI techniques, covering feature collinearity, model dependence, and a biomedical case study (myocardial infarction classification). Introduces NMR and MIP metrics for explanation stability.
Authors: Tanishq Varpe, Shravan Raut, Rohan Gundgal
