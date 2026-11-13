CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    EmployeeFirstName TEXT NOT NULL,
    EmployeeLastName TEXT NOT NULL,
    EmployeeDateOfBirth TEXT, --YYYY-MM-DD
    EmployeeAddress TEXT,
    EmployeeHireDate TEXT NOT NULL --YYYY-MM-DD
);

CREATE TABLE IF NOT EXISTS Shift (
    ShiftID INTEGER PRIMARY KEY AUTOINCREMENT,
    ShiftDay TEXT NOT NULL,
    ShiftDate TEXT NOT NULL, --YYYY-MM-DD
    ShiftStartTime TEXT NOT NULL, --HH:MM
    ShiftEndTime TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS WorkRecord (
    EmployeeID INTEGER NOT NULL,
    ShiftID INTEGER NOT NULL,
    ActualStartTime TEXT, --HH:MM
    ActualEndTime TEXT, --HH:MM
    HoursWorked REAL,
    WorkStatus TEXT NOT NULL DEFAULT 'Scheduled',
    PRIMARY KEY (EmployeeID, ShiftID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
    FOREIGN KEY (ShiftID) REFERENCES Shift(ShiftID),
    CHECK (HoursWorked IS NULL OR HoursWorked >= 0) 
);

CREATE TABLE IF NOT EXISTS Reports (
    ReportID INTEGER PRIMARY KEY AUTOINCREMENT,
    ReportName TEXT NOT NULL,
    ReportType TEXT NOT NULL,
    ReportPeriod TEXT NOT NULL,
    ReportStartDate TEXT NOT NULL, --YYYY-MM-DD
    ReportEndDate TEXT NOT NULL, --YYYY-MM-DD
    ReportSelectedFields TEXT,
    ReportGeneratedTime TEXT NOT NULL, --HH:MM
    ReportExportTime TEXT, --HH:MM
    EmployeeID INTEGER NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);