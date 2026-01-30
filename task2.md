

**<How long the dispense record must be kept in the system?, Constraint>**  
Keeping records for a set of time is not something a programmer picks, but it is defined by the pharmacy policy. Therefore, this comes under a constraint.

**<What specific information of a patient needs to be captured?, Functional Requirement>**  
This describes a task or behaviour of the dispenser system where the data of patient needs to be stored and managed. Therefore, this comes under functional requirement.

**<Should the system check drug to drug and drug to allergy interactions before dispensing?, Functional Requirement>**  
This is a system behaviour or feature. System is doing a task to assist user. Therefore, it is a functional requirement. 

**<Does the system support prescription refills?, Functional Requirement>**  
The system must have a feature to handle refills. This is a system behaviour of the dispensing workflow. It is a functional requirement. 

**<Is there an expiry date for a prescrption?, Constraint>**  
This is a rule defined by the environment (law/policy) and the system needs to follow that. Therefore, it is a constraint.

**<If a patient is prescribed multiple doses, can all doses be dispensed at once?, Functional Requirement>**  
Dispensing all medicine at once is a way how system handles the dispensing process either one by one or all at once. Therefore, it is a functional requirement.

**<Do different dispensing rules exist for different medication forms?, Constraint>**  
These are rules or regulations. The pharmacy/environment forces different medication types (pills or liquid) to be treated differently. Therefore, it is a constraint. 

**<Is every dispensing instance associated with exactly one medication?, Invariant>**  
A dispensing event must be attached to a medicine because an empty event without medicine attached to it makes no sense and would break the logic. Therefore, it is an invariant. 
