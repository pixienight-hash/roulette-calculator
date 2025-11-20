import streamlit as st

# 🎲 Ευρωπαϊκή ρουλέτα - φυσική διάταξη δεξιόστροφα
ROULETTE_NUMBERS = [
    0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11,
    30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18,
    29, 7, 28, 12, 35, 3, 26
]

# 📝 Ξεχωριστό Ιστορικό (χρησιμοποιούμε τη session_state για να διατηρείται το ιστορικό στο Streamlit)
if 'history_right' not in st.session_state:
    st.session_state.history_right = []
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
