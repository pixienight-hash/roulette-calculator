import streamlit as st

# (ΟΛΟΚΛΗΡΩΝΕΤΑΙ Ο ΥΠΑΡΧΩΝ ΚΩΔΙΚΑΣ ΣΟΥ)
# Βάλε εδώ τις λίστες ROULETTE_NUMBERS, history_right, history_left
# και τις συναρτήσεις get_indices, calculate_right_shift, calculate_left_shift

# --- ΚΥΡΙΩΣ ΠΡΟΓΡΑΜΜΑ STREAMLIT ---
st.title("🎲 Υπολογιστής Μετατόπισης Ρουλέτας")

st.markdown("""
Εφαρμογή για τον υπολογισμό της αριθμητικής απόστασης μετατόπισης 
στη φυσική διάταξη της Ευρωπαϊκής ρουλέτας.
""")

col1, col2 = st.columns(2)

with col1:
    st.header("Εισαγωγή Αριθμών")
    # Πλαίσια Εισαγωγής
    start_num = st.number_input("Αριθμός Εκκίνησης (0-36):", min_value=0, max_value=36, value=0)
    end_num = st.number_input("Αριθμός Τερματισμού (0-36):", min_value=0, max_value=36, value=26)

if st.button("Υπολόγισε τη Μετατόπιση"):
    st.subheader("Αποτελέσματα")
    
    # Υπολογισμός Δεξιόστροφα
    result_right = calculate_right_shift(start_num, end_num)
    st.success(f"➡️ **Δεξιόστροφη Μετατόπιση:** {result_right} θέσεις")
    
    # Υπολογισμός Αριστερόστροφα
    result_left = calculate_left_shift(start_num, end_num)
    st.success(f"⬅️ **Αριστερόστροφη Μετατόπιση:** {result_left} θέσεις")

# Εμφάνιση Ιστορικού
st.sidebar.header("📜 Ιστορικό")
st.sidebar.subheader("Δεξιόστροφες")
st.sidebar.text('\n'.join(history_right[-5:])) # Εμφάνιση των τελευταίων 5
st.sidebar.subheader("Αριστερόστροφες")
st.sidebar.text('\n'.join(history_left[-5:]))
