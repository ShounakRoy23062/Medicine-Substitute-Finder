CREATE DATABASE IF NOT EXISTS MediFindDB;

USE MediFindDB;

DROP TABLE IF EXISTS Det;
DROP TABLE IF EXISTS Supplier;

CREATE TABLE Det (
    Med_ID INT PRIMARY KEY,
    Med_Name VARCHAR(100) NOT NULL,
    Composition VARCHAR(100) NOT NULL,
    Med_Type VARCHAR(50) NOT NULL,
    Price DECIMAL(8,2) NOT NULL
);

INSERT INTO Det
(Med_ID, Med_Name, Composition, Med_Type, Price)
VALUES
(1, 'Dolo 650',     'Paracetamol',  'Tablet', 35.00),
(2, 'Crocin',       'Paracetamol',  'Tablet', 30.00),
(3, 'Calpol',       'Paracetamol',  'Tablet', 25.00),
(4, 'Azithral 500', 'Azithromycin', 'Tablet', 110.00),
(5, 'Azee 500',     'Azithromycin', 'Tablet', 90.00),
(6, 'Pantocid 40',  'Pantoprazole', 'Tablet', 100.00),
(7, 'Pantop 40',    'Pantoprazole', 'Tablet', 75.00);

CREATE TABLE Supplier (
    Supplier_ID INT PRIMARY KEY,
    Supplier_Name VARCHAR(100) NOT NULL,
    City VARCHAR(50) NOT NULL,
    Contact_No VARCHAR(15) NOT NULL,
    Supply_Type VARCHAR(50) NOT NULL
);


INSERT INTO Supplier
(Supplier_ID, Supplier_Name, City, Contact_No, Supply_Type)
VALUES
(1, 'MedPlus Distributors',  'Chennai',   '9876492315', 'Tablets'),
(2, 'Apollo Pharma Supply',  'Bangalore', '9558435160', 'Capsules'),
(3, 'Healthcare',            'Hyderabad', '9127411892', 'Syrups'),
(4, 'Cipla Dist',            'Mumbai',    '9847138291', 'Antibiotics'),
(5, 'SunPharma',             'Delhi',     '9876543214', 'General'),
(6, 'LifeCare',              'Pune',      '9743296412', 'Injections'),
(7, 'MediServe',             'Kolkata',   '9876543216', 'Tablets');


SELECT * FROM Det ORDER BY Med_ID;

SELECT * FROM Supplier ORDER BY Supplier_ID;

-- ==========================================================
-- TEST: FIND CHEAPER MEDICINES WITH THE SAME COMPOSITION
-- Example: Dolo 650

SELECT
    M.Med_Name AS Original_Medicine,
    M.Composition,
    S.Med_Name AS Substitute_Medicine,
    M.Price AS Original_Price,
    S.Price AS Substitute_Price,
    M.Price - S.Price AS Savings
FROM Det AS M
JOIN Det AS S
    ON M.Composition = S.Composition
WHERE M.Med_Name = 'Dolo 650'
  AND S.Med_ID <> M.Med_ID
  AND S.Price < M.Price
ORDER BY S.Price ASC;

-- ==========================================================
-- TEST: FIND SUPPLIERS FOR TABLETS

SELECT *
FROM Supplier
WHERE Supply_Type IN ('Tablets', 'General');