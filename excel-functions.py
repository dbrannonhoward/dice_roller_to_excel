from openpyxl import Workbook
import string


wb = Workbook()
worksheet = wb.active


def change_column(action='increment', active_column='A'):
    list_of_columns = generate_qty_of_column_names()
    active_column_index = list_of_columns.index(active_column)
    if action == 'increment':
        return list_of_columns[active_column_index + 1]
    return list_of_columns[active_column_index - 1]


def change_row(action='increment', active_row=1):
    list_of_rows = generate_qty_of_row_names()
    active_row_index = list_of_rows.index(active_row)
    if action == 'increment':
        return list_of_rows[active_row_index + 1]


def generate_qty_of_column_names(qty = 5):
    list_of_column_names = list()
    column_building_blocks = string.ascii_uppercase
    column_loop = 0
    for column_set in range(qty):
        column_root = column_building_blocks[column_loop-1]
        if column_set == 0:
            for character in column_building_blocks:
                list_of_column_names.append(character)
                if character == 'Z':
                    column_loop += 1
        else:
            for character in column_building_blocks:
                list_of_column_names.append(column_root + character)
                if character == 'Z':
                    column_loop += 1
    return list_of_column_names


def generate_qty_of_row_names(qty = 1000):
    row_list = list()
    for i in range(qty):
        row_list.append(i+1)
    return row_list
    return list_of_rows[active_row_index - 1]


def main():
    pass


if __name__ == '__main__':
    main()

