import cx_Freeze

executables = [cx_Freeze.Executable("app.py")]

cx_Freeze.setup(
       name="JSON TO EXCEL",
       version="1.0",
       description="Json to excel conversion",
       executables=executables,
)