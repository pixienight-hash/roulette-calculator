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
if 'history_left' not in st.session_state:
    st.session_state.history_left = []
    
TOTAL_NUMBERS = len(ROULETTE_NUMBERS)

# ----------------- ΕΝΗΜΕΡΩΣΗ ΣΥΝΑΡΤΗΣΕΩΝ -----------------
# Οι συναρτήσεις τώρα δέχονται 4 επιπλέον προαιρετικά ορίσματα για την ταχύτητα
def get_indices(start, end):
    """Ελέγχει αν οι αριθμοί είναι έγκυροι και επιστρέφει τους δείκτες τους."""
    if start not in ROULETTE_NUMBERS or end not in ROULETTE_NUMBERS:
        return None, None, "ΛΑΘΟΣ: Χρησιμοποίησε αριθμούς 0-36 της ευρωπαϊκής ρουλέτας."
    
    start_index = ROULETTE_NUMBERS.index(start)
    end_index = ROULETTE_NUMBERS.index(end)
    return start_index, end_index, None

def format_speed(spin_speed, ball_speed):
    """Δημιουργεί μια μορφοποιημένη συμβολοσειρά για την ταχύτητα."""
    if spin_speed or ball_speed:
        spin_str = f"Ρουλέτα: {spin_speed if spin_speed else '?'}"
        ball_str = f"Μπίλια: {ball_speed if ball_speed else '?'}"
        return f" ({spin_str}, {ball_str})"
    return ""

def calculate_right_shift(start, end, spin_speed="", ball_speed=""):
    """Υπολογίζει τη δεξιόστροφη μετατόπιση και ενημερώνει το ιστορικό."""
    start_idx, end_idx, error = get_indices(start, end)
    
    speed_info = format_speed(spin_speed, ball_speed)
    
    if error:
        entry = f"Δεξιά: {start} → {end} | {error} {speed_info}"
        st.session_state.history_right.append(entry)
        return error

    distance = (end_idx - start_idx) % TOTAL_NUMBERS
    
    entry = f"Δεξιά: {start} → {end} | {distance} θέσεις{speed_info}"
    st.session_state.history_right.append(entry)
    
    return distance

def calculate_left_shift(start, end, spin_speed="", ball_speed=""):
    """Υπολογίζει την αριστερόστροφη μετατόπιση και ενημερώνει το ιστορικό."""
    start_idx, end_idx, error = get_indices(start, end)
    
    speed_info = format_speed(spin_speed, ball_speed)

    if error:
        entry = f"Αριστερά: {start} → {end} | {error} {speed_info}"
        st.session_state.history_left.append(entry)
        return error

    distance = (start_idx - end_idx) % TOTAL_NUMBERS
    
    entry = f"Αριστερά: {start} → {end} | {distance} θέσεις{speed_info}"
    st.session_state.history_left.append(entry)
    
    return distance

# --- ΚΥΡΙΩΣ ΠΡΟΓΡΑΜΜΑ STREAMLIT (UI) ---

st.title("🎲 Υπολογιστής Μετατόπισης Ρουλέτας")

st.markdown("""
Εισάγετε τις θέσεις και προαιρετικά τις ταχύτητες περιστροφής (π.χ., 500 RPM, 3 δευτ.).
""")

col_right, col_left = st.columns(2)

# --- 1. Εισαγωγές Δεξιόστροφης Μετατόπισης ---
with col_right:
    st.subheader("➡️ Δεξιόστροφη Μετατόπιση")
    start_right = st.number_input("Αρχική Θέση (Δεξιά):", key="start_r", min_value=0, max_value=36, value=0)
    end_right = st.number_input("Τελική Θέση (Δεξιά):", key="end_r", min_value=0, max_value=36, value=26)
    
    # ΝΕΑ ΠΡΟΑΙΡΕΤΙΚΑ ΠΕΔΙΑ ΤΑΧΥΤΗΤΑΣ
    st.markdown("##### Προαιρετικές Ταχύτητες:")
    spin_speed_r = st.text_input("Ταχύτητα Ρουλέτας (Δεξιά):", key="speed_r", help="Π.χ. 'Slow', '500 RPM', ή κενό")
    ball_speed_r = st.text_input("Ταχύτητα Μπίλιας (Δεξιά):", key="ball_r", help="Π.χ. 'Fast', '3 sec', ή κενό")
    
    if st.button("Υπολόγισε Δεξιά", key="btn_right"):
        # Περνάμε τις ταχύτητες στη συνάρτηση
        result_right = calculate_right_shift(start_right, end_right, spin_speed_r, ball_speed_r)
        st.success(f"**Δεξιόστροφη Μετατόπιση:** {start_right} → {end_right} : **{result_right} θέσεις**")

# --- 2. Εισαγωγές Αριστερόστροφης Μετατόπισης ---
with col_left:
    st.subheader("⬅️ Αριστερόστροφη Μετατόπιση")
    start_left = st.number_input("Αρχική Θέση (Αριστερά):", key="start_l", min_value=0, max_value=36, value=0)
    end_left = st.number_input("Τελική Θέση (Αριστερά):", key="end_l", min_value=0, max_value=36, value=26)
    
    # ΝΕΑ ΠΡΟΑΙΡΕΤΙΚΑ ΠΕΔΙΑ ΤΑΧΥΤΗΤΑΣ
    st.markdown("##### Προαιρετικές Ταχύτητες:")
    spin_speed_l = st.text_input("Ταχύτητα Ρουλέτας (Αριστερά):", key="speed_l", help="Π.χ. 'Slow', '500 RPM', ή κενό")
    ball_speed_l = st.text_input("Ταχύτητα Μπίλιας (Αριστερά):", key="ball_l", help="Π.χ. 'Fast', '3 sec', ή κενό")

    if st.button("Υπολόγισε Αριστερά", key="btn_left"):
        # Περνάμε τις ταχύτητες στη συνάρτηση
        result_left = calculate_left_shift(start_left, end_left, spin_speed_l, ball_speed_l)
        st.success(f"**Αριστερόστροφη Μετατόπιση:** {start_left} → {end_left} : **{result_left} θέσεις**")


# --- Εμφ
