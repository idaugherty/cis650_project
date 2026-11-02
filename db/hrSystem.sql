CREATE TABLE IF NOT EXISTS Role (
    RoleID INTEGER PRIMARY KEY AUTOINCREMENT,
    RoleName TEXT NOT NULL,
);

CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    EmployeeFirstName VARCHAR(50),
    EmployeeLastName VARCHAR(50),
    EmployeeDateOfBirth DATE,
    EmployeeAddress VARCHAR(255),
    EmployeeHireDate DATE
);

CREATE TABLE IF NOT EXISTS TimeOffRequests (
    TimeOffRequestID INTEGER PRIMARY KEY AUTOINCREMENT,
    TimeOffRequestDate DATE,
    Approval Status VARCHAR(50),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

CREATE TABLE IF NOT EXISTS Shift (
    ShiftID INTEGER PRIMARY KEY AUTOINCREMENT,
    ShiftDayOfTheWeek VARCHAR(9),
    ShiftStartTime TEXT,
    ShiftEndTime TEXT,
    ShiftDate DATE,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

CREATE TABLE IF NOT EXISTS TrainingClasses (
    TrainingClassID INTEGER PRIMARY KEY AUTOINCREMENT,
    TrainingClassName VARCHAR(50),
    TrainingClassDescription VARCHAR(200),
    TrainingClassLength INTEGER
);

CREATE TABLE IF NOT EXISTS Reports (
    ReportID INTEGER PRIMARY KEY AUTOINCREMENT,
    ReportName VARCHAR(50),
    ReportSelectedFields TEXT,
    ReportSGenerationTime TEXT,
    ReportSGenerationTime TEXT,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

--UserRole 
--UserTrainingClasses
--Department
