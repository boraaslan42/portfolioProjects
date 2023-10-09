import openpyxl

# Load the Excel file
def adjustColumnWidth(file_path):
    workbook = openpyxl.load_workbook(file_path)

    # Select the first sheet (you can change the sheet name if needed)
    sheet = workbook.active

    # Iterate through columns and adjust the width based on the length of the first item
    for column in sheet.columns:
        column_letter = openpyxl.utils.get_column_letter(column[0].column)  # Get the column letter
        first_cell = column[0]  # Get the first cell in the column
        
        # Set the column width based on the length of the first item
        adjusted_width = len(str(first_cell.value)) + 2  # Add a little extra space
        sheet.column_dimensions[column_letter].width = adjusted_width

    # Save the modified workbook
    workbook.save(file_path)
