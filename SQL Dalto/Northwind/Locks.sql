--- Locks and TRANSACTION


--- The locks, is  a form to handle modifying the same data, to avoid modify in the same type

--- Types
--Shares Locks(Bloqueo Compartido): Any one can write but they can read
-- Reserved Locks(Bloqueo Reservad): The same of the other one, we apply it when we're writing, and let anyone write too
-- EXCLUSIVE Locks(Bloque exclusivo): When we're writint we don't let anyone read and write


-- BEGIN;
-- UPDATE Products SET ProductName = "mg" WHERE ProductName = "santi"; -- To modify a data using  a conditional
-- COMMIT;


-- COMMIT	 is forward to keep the it
-- ROLLBACK is back 


BEGIN; -- to start it
UPDATE Products SET ProductName = "VEV" WHERE ProductName = "mg"; 
ROLLBACK;  -- I think this one is to go back 
