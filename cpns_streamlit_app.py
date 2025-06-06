import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Prediksi CPNS Kemenkeu",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        color: #1a365d;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.8rem;
        color: #2d3748;
        margin-bottom: 1.5rem;
        font-weight: 600;
    }
    .metric-container {
        background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
        padding: 1.2rem;
        border-radius: 15px;
        border-left: 5px solid #4299e1;
        margin: 0.5rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .prediction-card {
        background: linear-gradient(135deg, #4299e1 0%, #3182ce 50%, #2b6cb0 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        border: 1px solid rgba(255,255,255,0.2);
    }
    .prediction-card h3 {
        font-size: 1.8rem;
        margin-bottom: 1rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    .prediction-card .data-row {
        display: flex;
        justify-content: space-between;
        margin-top: 1.2rem;
        flex-wrap: wrap;
        gap: 1rem;
    }
    .prediction-card .data-item {
        font-size: 1.2rem;
        font-weight: 500;
        background: rgba(255,255,255,0.15);
        padding: 0.5rem 1rem;
        border-radius: 8px;
        backdrop-filter: blur(10px);
    }
    .model-result {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 3px solid #e2e8f0;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 0.8rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        text-align: center;
    }
    .model-result:hover {
        border-color: #4299e1;
        box-shadow: 0 6px 20px rgba(66, 153, 225, 0.15);
        transform: translateY(-2px);
    }
    .model-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #2d3748;
        margin-bottom: 1rem;
        text-align: center;
    }
    .prediction-result {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 1.2rem 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .accuracy-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1rem;
        margin-top: 0.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }
    .high-accuracy { 
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%); 
        color: white; 
    }
    .medium-accuracy { 
        background: linear-gradient(135deg, #ed8936 0%, #dd6b20 100%); 
        color: white; 
    }
    .low-accuracy { 
        background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%); 
        color: white; 
    }
    .stButton > button {
        background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(66, 153, 225, 0.3);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #3182ce 0%, #2c5282 100%);
        box-shadow: 0 6px 20px rgba(66, 153, 225, 0.4);
        transform: translateY(-1px);
    }
    .stForm {
        background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_models_and_encoder():
    """Load all trained models and the label encoder"""
    models = {}
    accuracy_scores = {}
    
    try:
        with open('models/accuracy_scores.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[2:]:
                if ':' in line:
                    name, score = line.strip().split(': ')
                    accuracy_scores[name] = float(score)
    except FileNotFoundError:
        st.error("Accuracy scores file not found!")
        return None, None, None
    
    model_files = {
        'SVM': 'models/svm_model.joblib',
        'Decision Tree': 'models/decision_tree_model.joblib', 
        'Random Forest': 'models/random_forest_model.joblib',
        'K-NN': 'models/k-nn_model.joblib',
        'Naïve Bayes': 'models/naïve_bayes_model.joblib'
    }
    
    print("Available accuracy scores:", list(accuracy_scores.keys()))
    
    for name, file_path in model_files.items():
        try:
            models[name] = joblib.load(file_path)
        except FileNotFoundError:
            st.error(f"Model file {file_path} not found!")
            return None, None, None
    
    try:
        label_encoder = joblib.load('models/label_encoder.joblib')
    except FileNotFoundError:
        st.error("Label encoder file not found!")
        return None, None, None
    
    return models, label_encoder, accuracy_scores

def get_accuracy_badge_class(accuracy):
    """Get CSS class for accuracy badge based on score"""
    if accuracy >= 0.85:
        return "high-accuracy"
    elif accuracy >= 0.75:
        return "medium-accuracy"
    else:
        return "low-accuracy"

def predict_all_models(models, label_encoder, input_data):
    """Make predictions using all models"""
    predictions = {}
    probabilities = {}
    
    for name, model in models.items():
        try:
            pred_encoded = model.predict([input_data])[0]
            pred_label = label_encoder.inverse_transform([pred_encoded])[0]
            predictions[name] = pred_label
            
            if hasattr(model, 'predict_proba'):
                proba = model.predict_proba([input_data])[0]
                probabilities[name] = dict(zip(label_encoder.classes_, proba))
            
        except Exception as e:
            st.error(f"Error predicting with {name}: {e}")
            predictions[name] = "Error"
            
    return predictions, probabilities

def main():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%); 
                padding: 2rem; margin: -1rem -1rem 2rem -1rem; border-radius: 0 0 20px 20px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
        <h1 class="main-header" style="color: white; margin-bottom: 0.5rem;">
            🏛️ Prediksi CPNS Kemenkeu
        </h1>
        <p style="text-align: center; font-size: 1.3rem; color: rgba(255,255,255,0.9); 
                  font-weight: 500; margin: 0;">
            Sistem Prediksi Kelulusan CPNS Kementerian Keuangan dengan Machine Learning
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.spinner('Loading models...'):
        models, label_encoder, accuracy_scores = load_models_and_encoder()
    
    if models is None:
        st.error("Failed to load models. Please check if model files exist in the 'models' directory.")
        return
    
    st.markdown('<h2 class="sub-header">📝 Input Data Peserta</h2>', unsafe_allow_html=True)
    
    with st.form("prediction_form"):
        nama = st.text_input("Nama Lengkap", value="TEOFILUS DICKY UMBU HULA PARTOGIAN SINAGA")
        
        col_input1, col_input2 = st.columns(2)
        with col_input1:
            umur = st.number_input("Umur", value=27)
            nilai_ipk = st.number_input("Nilai IPK", min_value=0.0, max_value=4.0, value=3.2, step=0.01)
        
        with col_input2:
            nilai_skd = st.number_input("Nilai SKD", min_value=0, value=400)
            nilai_skb = st.number_input("Nilai SKB", min_value=0.0, value=67.37, step=0.01)
        
        submitted = st.form_submit_button("🔮 Prediksi", use_container_width=True)
    
    if submitted:
        if not nama.strip():
            st.warning("⚠️ Silakan masukkan nama lengkap!")
            return
        
        input_data = [umur, nilai_ipk, nilai_skd, nilai_skb]
        
        # st.markdown("""
        # <div style="background: linear-gradient(135deg, #4fd1c7 0%, #14b8a6 100%); 
        #             padding: 1.5rem; margin: 2rem 0; border-radius: 15px;
        #             box-shadow: 0 4px 15px rgba(20, 184, 166, 0.2);">
        #     <h2 style="color: white; text-align: center; margin: 0; font-size: 2rem; font-weight: bold;">
        #         🎯 Hasil Prediksi dari 5 Model AI
        #     </h2>
        # </div>
        # """, unsafe_allow_html=True)
        
        with st.container():
            st.markdown(f"""
            <div class="prediction-card">
                <h3>👤 {nama}</h3>
                <div class="data-row">
                    <div class="data-item">📅 <strong>Umur:</strong> {umur} tahun</div>
                    <div class="data-item">🎓 <strong>IPK:</strong> {nilai_ipk}</div>
                    <div class="data-item">📝 <strong>SKD:</strong> {nilai_skd}</div>
                    <div class="data-item">💼 <strong>SKB:</strong> {nilai_skb}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with st.spinner('Melakukan prediksi dengan semua model...'):
            predictions, probabilities = predict_all_models(models, label_encoder, input_data)
        
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0 1rem 0;">
            <h3 style="color: #2d3748; font-size: 1.8rem; font-weight: bold; margin-bottom: 0.5rem;">
                Prediksi Individual dari Setiap Model
            </h3>
            <p style="color: #718096; font-size: 1.1rem; margin: 0;">
                Setiap model memberikan prediksi berdasarkan algoritma yang berbeda
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div style="margin: 1.5rem 0;"></div>', unsafe_allow_html=True)
        cols = st.columns(len(models), gap="medium")
        
        for idx, (model_name, prediction) in enumerate(predictions.items()):
            with cols[idx]:
                if model_name in accuracy_scores:
                    accuracy = accuracy_scores[model_name]
                else:
                    st.error(f"Accuracy score not found for {model_name}")
                    st.error(f"Available scores: {list(accuracy_scores.keys())}")
                    accuracy = 0.0
                badge_class = get_accuracy_badge_class(accuracy)
                
                pred_color = "#48bb78" if prediction == "P/L" else "#f56565"
                
                st.markdown(f"""
                <div class="model-result">
                    <div class="model-title">{model_name}</div>
                    <div class="prediction-result" style="color: {pred_color};">
                        {prediction}
                    </div>
                    <div class="accuracy-badge {badge_class}">
                        {accuracy:.2%} Accuracy
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # if model_name in probabilities:
                #     probs = probabilities[model_name]
                #     max_prob = max(probs.values())
                #     st.markdown("**Confidence:**")
                #     for class_name, prob in probs.items():
                #         if class_name == prediction:
                #             st.markdown(f"**{class_name}**: {prob:.1%}")

if __name__ == "__main__":
    main() 