
from database import get_connection, initialize_db

def seed_database():
    initialize_db()
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """INSERT INTO Employee
        (EmployeeID, EmployeeFirstName, EmployeeLastName,
        EmployeeDateOfBirth, EmployeeAddress, EmployeeHireDate)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (1, "Amanda", "Carter", "1997-04-15",
         "101 Main St, Murray, KY", "2023-01-09")
    )

    cursor.execute(
        """INSERT INTO Employee
        (EmployeeID, EmployeeFirstName, EmployeeLastName,
        EmployeeDateOfBirth, EmployeeAddress, EmployeeHireDate)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (2, "Benjamin", "Lewis", "1999-08-22",
         "205 Oak St, Murray, KY", "2024-03-18")
    )
    
    cursor.execute(
        """INSERT INTO Employee
        (EmployeeID, EmployeeFirstName, EmployeeLastName,
        EmployeeDateOfBirth, EmployeeAddress, EmployeeHireDate)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (3, "Chloe", "Martinez", "1998-12-03",
         "312 Pine St, Murray, KY", "2022-07-11")
    )

    cursor.execute(
        """INSERT INTO Employee
        (EmployeeID, EmployeeFirstName, EmployeeLastName,
        EmployeeDateOfBirth, EmployeeAddress, EmployeeHireDate)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (4, "Daniel", "Brooks", "2000-02-10",
         "410 Maple St, Murray, KY", "2025-05-12")
    )

    #each shift is 6 hours.
    #four shifts per day, Monday through Saturday.
    shift_sql = """
        INSERT INTO Shift
        (ShiftID, ShiftDay, ShiftDate, ShiftStartTime, ShiftEndTime)
        VALUES (?, ?, ?, ?, ?)
    """
    #Monday
    cursor.execute(shift_sql, (1, "Monday", "2026-11-02", "00:00", "06:00"))
    cursor.execute(shift_sql, (2, "Monday", "2026-11-02", "06:00", "12:00"))
    cursor.execute(shift_sql, (3, "Monday", "2026-11-02", "12:00", "18:00"))
    cursor.execute(shift_sql, (4, "Monday", "2026-11-02", "18:00", "00:00"))

    #Tuesday
    cursor.execute(shift_sql, (5, "Tuesday", "2026-11-03", "00:00", "06:00"))
    cursor.execute(shift_sql, (6, "Tuesday", "2026-11-03", "06:00", "12:00"))
    cursor.execute(shift_sql, (7, "Tuesday", "2026-11-03", "12:00", "18:00"))
    cursor.execute(shift_sql, (8, "Tuesday", "2026-11-03", "18:00", "00:00"))

    #Wednesday
    cursor.execute(shift_sql, (9, "Wednesday", "2026-11-04", "00:00", "06:00"))
    cursor.execute(shift_sql, (10, "Wednesday", "2026-11-04", "06:00", "12:00"))
    cursor.execute(shift_sql, (11, "Wednesday", "2026-11-04", "12:00", "18:00"))
    cursor.execute(shift_sql, (12, "Wednesday", "2026-11-04", "18:00", "00:00"))

    #Thursday
    cursor.execute(shift_sql, (13, "Thursday", "2026-11-05", "00:00", "06:00"))
    cursor.execute(shift_sql, (14, "Thursday", "2026-11-05", "06:00", "12:00"))
    cursor.execute(shift_sql, (15, "Thursday", "2026-11-05", "12:00", "18:00"))
    cursor.execute(shift_sql, (16, "Thursday", "2026-11-05", "18:00", "00:00"))

    #Friday
    cursor.execute(shift_sql, (17, "Friday", "2026-11-06", "00:00", "06:00"))
    cursor.execute(shift_sql, (18, "Friday", "2026-11-06", "06:00", "12:00"))
    cursor.execute(shift_sql, (19, "Friday", "2026-11-06", "12:00", "18:00"))
    cursor.execute(shift_sql, (20, "Friday", "2026-11-06", "18:00", "00:00"))

    #Saturday
    cursor.execute(shift_sql, (21, "Saturday", "2026-11-07", "00:00", "06:00"))
    cursor.execute(shift_sql, (22, "Saturday", "2026-11-07", "06:00", "12:00"))
    cursor.execute(shift_sql, (23, "Saturday", "2026-11-07", "12:00", "18:00"))
    cursor.execute(shift_sql, (24, "Saturday", "2026-11-07", "18:00", "00:00"))

    work_sql = """
        INSERT INTO WorkRecord
        (EmployeeID, ShiftID, ActualStartTime,
         ActualEndTime, HoursWorked, WorkStatus)
        VALUES (?, ?, ?, ?, ?, ?)
    """
    #Monday
    cursor.execute(work_sql, (1, 1, "2026-11-02 00:00:00", "2026-11-02 06:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (2, 2, "2026-11-02 06:00:00", "2026-11-02 12:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (3, 3, "2026-11-02 12:00:00", "2026-11-02 18:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (4, 4, "2026-11-02 18:00:00", "2026-11-03 00:00:00", 6.0, "Completed"))

    #Tuesday
    cursor.execute(work_sql, (1, 5, "2026-11-03 00:00:00", "2026-11-03 06:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (2, 6, "2026-11-03 06:00:00", "2026-11-03 12:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (3, 7, "2026-11-03 12:00:00", "2026-11-03 18:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (4, 8, "2026-11-03 18:00:00", "2026-11-04 00:00:00", 6.0, "Completed"))

    #wednesday
    cursor.execute(work_sql, (1, 9, "2026-11-04 00:00:00", "2026-11-04 06:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (2, 10, "2026-11-04 06:00:00", "2026-11-04 12:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (3, 11, "2026-11-04 12:00:00", "2026-11-04 18:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (4, 12, "2026-11-04 18:00:00", "2026-11-05 00:00:00", 6.0, "Completed"))

    #thurdsay
    cursor.execute(work_sql, (1, 13, "2026-11-05 00:00:00", "2026-11-05 06:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (2, 14, "2026-11-05 06:00:00", "2026-11-05 12:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (3, 15, "2026-11-05 12:00:00", "2026-11-05 18:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (4, 16, "2026-11-05 18:00:00", "2026-11-06 00:00:00", 6.0, "Completed"))

    #Friday
    cursor.execute(work_sql, (1, 17, "2026-11-06 00:00:00", "2026-11-06 06:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (2, 18, "2026-11-06 06:00:00", "2026-11-06 12:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (3, 19, "2026-11-06 12:00:00", "2026-11-06 18:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (4, 20, "2026-11-06 18:00:00", "2026-11-07 00:00:00", 6.0, "Completed"))

    #Saturday
    cursor.execute(work_sql, (1, 21, "2026-11-07 00:00:00", "2026-11-07 06:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (2, 22, "2026-11-07 06:00:00", "2026-11-07 12:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (3, 23, "2026-11-07 12:00:00", "2026-11-07 18:00:00", 6.0, "Completed"))
    cursor.execute(work_sql, (4, 24, "2026-11-07 18:00:00", "2026-11-08 00:00:00", 6.0, "Completed"))

    report_sql = """
        INSERT INTO Reports
        (ReportID, ReportName, ReportType,
         ReportPeriod, ReportStartDate, ReportEndDate,
         ReportSelectedFields, ReportGeneratedTime,
         ReportExportTime, EmployeeID)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(
        report_sql,
        (1, "Amanda's Weekly Hours", "Hours Worked",
         "Weekly", "2026-11-02", "2026-11-07",
         '["EmployeeID", "ShiftDate", "HoursWorked"]',
         "2026-11-08 09:00:00",
         "2026-11-08 09:05:00", 1)
    )

    cursor.execute(
        report_sql,
        (2, "Benjamin's Weekly Hours", "Hours Worked",
         "Weekly", "2026-11-02", "2026-11-07",
         '["EmployeeID", "ShiftDate", "HoursWorked"]',
         "2026-11-08 09:10:00",
         None, 2)
    )

    cursor.execute(
        report_sql,
        (3, "Chloe's Weekly Hours", "Hours Worked",
         "Weekly", "2026-11-02", "2026-11-07",
         '["EmployeeID", "ShiftDate", "HoursWorked"]',
         "2026-11-08 09:20:00",
         "2026-11-08 09:25:00", 3)
    )

    cursor.execute(
        report_sql,
        (4, "Daniel's Weekly Hours", "Hours Worked",
         "Weekly", "2026-11-02", "2026-11-07",
         '["EmployeeID", "ShiftDate", "HoursWorked"]',
         "2026-11-08 09:30:00",
         None, 4)
    )
    connection.commit()
    connection.close()
    print("Sample data inserted successfully.")


if __name__ == "__main__":
    seed_database()
