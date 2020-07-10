import xlrd
from gensim.summarization import keywords
import xlsxwriter
import operator
import re
import string

def get_colored_text(text, keywords_list, red, black):
    whole = [] #keeps text with colors
    line = text.strip()

    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))

    # Split the line into words
    words = line.split()

    #search for each word in keyword list, put into colored whole text
    for word in words:
        if any(word in sublist for sublist in keywords_list):
            whole.append(red)
            whole.append(word)
        else:
            whole.append(black)
            whole.append(word)
        whole.append(" ")

    return whole

def color(fileName, keywords_list):
    #open excel file
    dataFile = xlrd.open_workbook(fileName)
    sheet = dataFile.sheet_by_index(0)

    #file where we write write colored data
    workbook = xlsxwriter.Workbook('colored.xlsx')
    worksheet = workbook.add_worksheet()

    #count keywords for each line
    red = workbook.add_format({'color': 'red'})
    black = workbook.add_format({'color': 'black'})
    text_wrap = workbook.add_format({'text_wrap': True})

    #count keywords for each line
    keyword_count = {}
    for i in range(sheet.nrows):
        count = 0
        for j in range(sheet.ncols):
            line = sheet.cell_value(i, j)
            # red = workbook.add_format({'color': 'red'})
            # black = workbook.add_format({'color': 'black'})
            # text_wrap = workbook.add_format({'text_wrap': False})
            string_parts = get_colored_text(line, keywords_list, red, black)
            string_parts.append(text_wrap)
            #print(string_parts)
            worksheet.write_rich_string(i,j, *string_parts)

        #add keyword count of each line
        keyword_count[i] = count
        #print("total = " + str(count))
        print(str(i))

    workbook.close()


# if __name__ == '__main__':
#     color()


















    ##
