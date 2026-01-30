import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(path)

from dispense import DispenseEvent

def run_tests():
    events = []
    dose_limit = 500
    # Test 1
    print("Test 1: Patient ID is Not Given")
    try:
        test1 = DispenseEvent("", "Ibuprofen", "200mg", 1, dose_limit, "2026-01-29")
        if DispenseEvent.invariant_holds(events, test1):
            print("Fail: Accepted an empty patient's ID")
    except Exception as e:
        print(f"Pass: Identified problem with patient's ID")


    #Test 2
    print("Test 2: Different Dose Unit")
    try:
        test2 = DispenseEvent("Patient003", "Ibuprofen", "20cmg", 1, dose_limit, "2026-01-29")
        if DispenseEvent.invariant_holds(events, test2):
            print("Fail: Accepted invalid units")
    except Exception as e:
        print(f"Pass: Blocked the dose with other units") 
    
    #Test 3
    print("Test 3: Negative value of dose")
    try:
        test3 = DispenseEvent("Patient003", "Ibuprofen", "-10mg", 1, dose_limit, "2026-01-29")
        if DispenseEvent.invariant_holds(events, test3):
            print("Fail: Accaepted negative dose")
    except Exception as e:
        print(f"Pass:Correctly blocked negative dose. {e}") 
   
    #Test 4
    print("Test 4: Dose is a float")
    try:
        test4 = DispenseEvent("Patient003", "Ibuprofen", "10.1mg", 1, dose_limit, "2026-01-29")
        if DispenseEvent.invariant_holds(events, test4):
            events.append(test4)
            print("Pass: Accepted the float value for dose")
    except Exception as e:
        print(f"Fail: Blocked the floating value of dose") 

    #Test 5
    print("Test 5: Quantity NOT an Integer")
    try:
        test5 = DispenseEvent("Patient003", "Ibuprofen", "10.1mg", 1.5, dose_limit, "2026-01-29")
        if DispenseEvent.invariant_holds(events, test5):
            print("Failed blocking non-integer value")
    except Exception as e:
        print(f"Pass: System blocked non-integer quantity") 

    #Test 6
    print("Test 6: Quantity is 0")
    try:
        test6 = DispenseEvent("Patient003", "Ibuprofen", "10.1mg", 0, dose_limit, "2026-01-29")
        if DispenseEvent.invariant_holds(events, test6):
            print("Failed to Block 0 quantity")
    except Exception as e:
        print(f"Pass: System blocked 0 quantity") 
    
    #Test 7
    print("Test 7: Quantity is negative")
    try:
        test7 = DispenseEvent("Patient003", "Ibuprofen", "10.1mg", -9, dose_limit, "2026-01-29")
        if DispenseEvent.invariant_holds(events, test7):
            print("Failed to Block negative quantity")
    except Exception as e:
        print(f"Pass: System blocked negative quantity") 

        
    #Test 8
    print("Test 8: Maximum Dose Limit  Reached")
    try:
        test8 = DispenseEvent("Patient003", "Ibuprofen", "700mg", 9, dose_limit, "2026-01-29")
        if DispenseEvent.invariant_holds(events, test8):
            print("Failed to Block maximum dose request")
    except Exception as e:
        print(f"Pass: System blocked having dose beyond the daily limit") 
    

    #Test 9
    print("Test 9: Adding duplicate of the Patient for same meds and day")

    test9 = DispenseEvent("Patient005", "Advil", "200mg", 1, dose_limit, "2026-01-30")
    if DispenseEvent.invariant_holds(events, test9):
        events.append(test9)
        print("Initial Patient Data is Added")
    
    try:
        test10 = DispenseEvent("Patient005", "Advil", "200mg", 1, dose_limit, "2026-01-30")
        if not DispenseEvent.invariant_holds(events, test10):
            print("Pass: System didn't allow to dispense same medicine at the same day for same patient")
        else:
            print("Fail: System allowed a duplicate entry of patient")
    except Exception as e:
        print(f"Unexpected Error: {e}")

    #Test 10
    print("Test 10: Adding duplicate of the Patient (same day but different medicine)")

    test10 = DispenseEvent("Patient007", "Advil", "200mg", 1, dose_limit, "2026-01-30")
    if DispenseEvent.invariant_holds(events, test10):
        events.append(test10)
        print("Patient Data is Added")
    
    try:
        test10 = DispenseEvent("Patient007", "Tylenol", "200mg", 1, dose_limit, "2026-01-30")
        if DispenseEvent.invariant_holds(events, test10):
            print("Pass: Patient was given both medicines on same day")
        else:
            print("Fail: System denied giving the medicine")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    run_tests()