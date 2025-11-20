import streamlit as st

# 🎲 Ευρωπαϊκή ρουλέτα - φυσική διάταξη δεξιόστροφα
ROULETTE_NUMBERS = [
    0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11,
    30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18,
    29, 7, 28, 12, 35, 3, 26
]

# 📝 Αρχικοποίηση Ιστορικού
if 'history_right' not in st.session_state:
    st.session_state.history_right = []
    
# Η ΔΙΟΡΘΩΣΗ ΕΙΝΑΙ ΕΔΩ: αφαιρέθηκε το διπλό 'in'
if 'history_left' not in st.session_state: 
    st.session_state.history_left = []
    
TOTAL_NUMBERS = len(ROULETTE_NUMBERS)

def get_indices(start, end):
    """Ελέγχει αν οι αριθμοί είναι έγκυροι και επιστρέφει τους δείκτες τους."""
    if start not in ROULETTE_NUMBERS or end not in ROULETTE_NUMBERS:
        return None, None, "ΛΑΘΟΣ: Χρησιμοποίησε αριθμούς 0-36 της ευρωπαϊκής ρουλέτας."
    
    start_index = ROULETTE_NUMBERS.index(start)
    end_index = ROULETTE_NUMBERS.index(end)
    return start_index, end_index, None

def calculate_right_shift(start, end):
    """Υπολογίζει τη δεξιόστροφη μετατόπιση και ενημερώνει το ιστορικό."""
    start_idx, end_idx, error = get_indices(start, end)
    
    if error:
        entry = f"Δεξιά: {start} → {end} | {error}"
        st.session_state.history_right.append(entry)
        return error

    distance = (end_idx - start_idx) % TOTAL_NUMBERS
    
    entry = f"Δεξιά: {start} → {end} | {distance} θέσεις"
    st.session_state.history_right.append(entry)
    
    return distance

def calculate_left_shift(start, end):
    """Υπολογίζει την αριστερόστροφη μετατόπιση και ενημερώνει το ιστορικό."""
    start_idx, end_idx, error = get_indices(start, end)
    
    if error:
        entry = f"Αριστερά: {start} → {end} | {error}"
        st.session_state.history_left.append(entry)
        return error

    distance = (start_idx - end_idx) % TOTAL_NUMBERS
    
    entry = f"Αριστερά: {start} → {end} | {distance} θέσεις"
    st.session_state.history_left.append(entry)
    
    return distance

# --- ΚΥΡΙΩΣ ΠΡΟΓΡΑΜΜΑ STREAMLIT (UI) ---

st.title("🎲 Υπολογιστής Μετατόπισης Ρουλέτας")

st.markdown("""
Εισάγετε ξεχωριστές αρχικές και τελικές θέσεις για τον υπολογισμό της **Δεξιόστροφης** και της **Αριστερόστροφης** μετατόπισης.
""")

# Δημιουργία μεταβλητών για τα αποτελέσματα
right_result_placeholder = st.empty()
left_result_placeholder = st.empty()

col_right, col_left = st.columns(2)

# --- 1. Εισαγωγές Δεξιόστροφης Μετατόπισης ---
with col_right:
    st.subheader("➡️ Δεξιόστροφη Μετατόπιση")
    start_right = st.number_input("Αρχική Θέση (Δεξιά):", key="start_r", min_value=0, max_value=36, value=0)
    end_right = st.number_input("Τελική Θέση (Δεξιά):", key="end_r", min_value=0, max_value=36, value=26)
    
    # ΝΕΟ ΚΟΥΜΠΙ ΓΙΑ ΤΟΝ ΔΕΞΙΟΣΤΡΟΦΟ ΥΠΟΛΟΓΙΣΜΟ
    if st.button("Υπολόγισε Δεξιά", key="btn_right"):
        result_right = calculate_right_shift(start_right, end_right)
        st.success(f"**Δεξιόστροφη Μετατόπιση:** {start_right} → {end_right} : **{result_right} θέσεις**")

# --- 2. Εισαγωγές Αριστερόστροφης Μετατόπισης ---
with col_left:
    st.subheader("⬅️ Αριστερόστροφη Μετατόπιση")
    start_left = st.number_input("Αρχική Θέση (Αριστερά):", key="start_l", min_value=0, max_value=36, value=0)
    end_left = st.number_input("Τελική Θέση (Αριστερά):", key="end_l", min_value=0, max_value=36, value=26)

    # ΝΕΟ ΚΟΥΜΠΙ ΓΙΑ ΤΟΝ ΑΡΙΣΤΕΡΟΣΤΡΟΦΟ ΥΠΟΛΟΓΙΣΜΟ
    if st.button("Υπολόγισε Αριστερά", key="btn_left"):
        result_left = calculate_left_shift(start_left, end_left)
        st.success(f"**Αριστερόστροφη Μετατόπιση:** {start_left} → {end_left} : **{result_left} θέσεις**")


# --- Εμφάνιση Ιστορικού ---
st.sidebar.header("📜 Ιστορικό")

st.sidebar.subheader("Δεξιόστροφες")
if st.session_state.history_right:
    # Ταξινόμηση (Δεν χρειάζεται, αφού το history_right ενημερώνεται με τη σειρά που γίνονται οι υπολογισμοί)
    st.sidebar.text('\n'.join(st.session_state.history_right[-10:])) 
else:
    st.sidebar.text('Δεν υπάρχουν καταχωρήσεις.')

st.sidebar.subheader("Αριστερόστροφες")
if st.session_state.history_left:
    st.sidebar.text('\n'.join(st.session_state.history_left[-10:]))
else:
    st.sidebar.text('Δεν υπάρχουν καταχωρήσεις.')
