-- Since CurrentCredit cannot be NULL, I filter for 0 balance
UPDATE CustomerAccounts 
SET CurrentCredit = 
    CASE WHEN CurrentCredit >= 1 AND CurrentCredit <=15 THEN (CurrentCredit + 1)
         WHEN CurrentCredit >= 16 AND CurrentCredit <= 30 THEN (CurrentCredit + 2)
         WHEN CurrentCredit >= 31 THEN CEILING(CurrentCredit * 1.10)
    END
WHERE CurrentCredit > 0
;

-- ALTERNATE, preserves 0 balance, does not filter
# UPDATE CustomerAccounts 
# SET CurrentCredit = 
#     CASE WHEN CurrentCredit >= 1 AND CurrentCredit <=15 THEN (CurrentCredit + 1)
#          WHEN CurrentCredit >= 16 AND CurrentCredit <= 30 THEN (CurrentCredit + 2)
#          WHEN CurrentCredit >= 31 THEN CEILING(CurrentCredit * 1.10)
#          ELSE CurrentCredit
#     END
# ;