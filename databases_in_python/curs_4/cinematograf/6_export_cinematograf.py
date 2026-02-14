import mysql.connector
import xlsxwriter

def fetch_data_table(table_name):
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='#t*W3*z5+a77I!P@+173',
        database='cinematograf'
    )
    
    cursor = db.cursor()
    
    cursor.execute(f'select * from {table_name}')
    
    # Preluam capul de tabel
    header = [row[0] for row in cursor.description]
    
    # header = []
    
    # for row in cursor.description:
    #     header.append(row[0])
    
    # Preluam datele
    rows = cursor.fetchall()
    
    db.close()
    
    return header, rows


def export(table_name):
    # Cream un fisiel Excel nou cu numele tabelei
    workbook = xlsxwriter.Workbook(f"{table_name}.xlsx")
    worksheet = workbook.add_worksheet(table_name)
    
    header_cell_format = workbook.add_format({'bold': True, 'border': True, 'bg_color': 'yellow'})
    body_cell_format = workbook.add_format({'border': True})
    
    header, rows = fetch_data_table(table_name)
    
    # Ii spunem de unde sa inceapa sa scrie header-ul
    row_index = 0
    column_index = 0

    # Itereaza peste lista cu numele coloanelor si merge la dreapta pe fiecare coloana, pe masura ce itereaza peste lista de valori
    for column_name in header:
        worksheet.write(row_index, column_index, column_name, header_cell_format)
        column_index += 1
        
    # Ii spunem sa scrie de la linia urmatoare pt. ca prima linie este header-ul
    row_index += 1
    
    for row in rows:
        column_index = 0
        for column in row:
            worksheet.write(row_index, column_index, column, body_cell_format)
            column_index += 1
        row_index += 1
    
    print(f'{row_index} rows written in {workbook.filename}')
    
    workbook.close()
    
    
export('clienti')
export('bilete')
export('sali')
export('filme')
