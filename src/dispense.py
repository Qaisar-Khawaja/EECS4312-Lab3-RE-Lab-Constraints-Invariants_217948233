#static list of events here = []
class DispenseEvent:
    """
    Represents a single medication dispensing event for a patient.

    """

    # TODO Task 3: Encode and enforce input constraints (e.g., valid dose, quantity, identifiers)
    def __init__(self, patient_id, medication, dose_mg, quantity, dose_limit):
        """
        Initialize a new DispenseEvent.

        Args:
            patient_id: Unique identifier for the patient receiving medication.
            medication: Name or identifier of the medication being dispensed.
            dose_mg: Dose per unit in milligrams. Must be a positive number.
            quantity: Number of units dispensed. Must be a positive integer.

        """

        if not dose_mg.endswith("mg"):
            raise ValueError("The dose is not specified by right units(mg).")
       
        try: 
            number_digit = dose_mg.replace("mg", "")
            num_Value = float(number_digit)
            if num_Value <= 0:
                raise ValueError("The dose must be a positive value.")
        except ValueError:
            raise ValueError("Dose must contain a number")

        
        if not isinstance (quantity, int) or quantity <= 0: 
                raise ValueError("The quantity must be a psoitive integer.")
        if not patient_id:
            raise ValueError("Please provide the patient ID")
        if num_Value > dose_limit:
            raise ValueError("Maximum dose reached")

        
        self.patient_id = patient_id
        self.medication = medication
        self.dose_mg = dose_mg
        self.quantity = quantity
        self.dose_limit = dose_limit
        

    # TODO Task 4: Define and check system invariants 
    def invariant_holds(existing_events, new_event):
        """
        Check whether adding a new dispense event preserves all system invariants.

        Args:
            existing_events: Iterable of previously recorded DispenseEvent objects.
            new_event: The proposed DispenseEvent to validate.

        Returns:
            bool: True if all invariants hold after adding new_event; False otherwise.
            
        """
        for event in existing_events: 
            if (event.patient_id == new_event.patient_id and 
                event.medication == new_event.medication) and
                event.date == new_event.date):
                return False

            if dose_mg.endswith("mg"):
                number_part = dose_str.replace("mg", "")
            if number_part.isdigit():
                return True 
            

        return True

