import xlrd
import xlsxwriter
from gensim.summarization import keywords
import operator
import re
import string

def count_keywords(line, keywords_list):
    # Remove the leading spaces and newline character
    line = line.strip()
    count = 0
    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))

    # Split the line into words
    words = line.split(" ")
    # Iterate over each word in line
    for word in words:
        #print(word)
        # Check if the word is already in dictionary
        if any(word in sublist for sublist in keywords_list):
            # Increment count of word by 1
            count += 1

    #print("count = " + str(count))
    return count


def sort(fileName, keywords_list):
    #write sorted-colored data into a new excel file
    dataFile = xlrd.open_workbook(fileName)
    sheet = dataFile.sheet_by_index(0)
    workbook = xlsxwriter.Workbook('sorted.xlsx')
    worksheet = workbook.add_worksheet()

    # #count keywords for each line
    # print("cell values")
    # for i in range(sheet.ncols):
    #     print(sheet.cell_value(0,i))
    #
    keyword_count = {}
    for i in range(sheet.nrows):
        count = 0
        for j in range(sheet.ncols):
            line = sheet.cell_value(i, j)
            count += count_keywords(line, keywords_list)
        #add keyword count of each line
        keyword_count[i] = count
        #print("total = " + str(count))
        print(str(i) + " = " + str(count))

    ###### SORTING LINES #####
    sorted_x = sorted(keyword_count.items(), key=operator.itemgetter(1))
    print(sorted_x)

    #write sorted lines
    sorted_lines = {}
    i=0
    for key, val in sorted_x:
        sorted_lines[i] = key
        i += 1
    print(sorted_lines)

    #write sorted lines into new excel file final.xlsx
    for i in range(sheet.ncols):
        text = sheet.cell_value(0, i)
        worksheet.write(0, i, text)

    for i in range(len(sorted_lines)-1, 1, -1):
        print(i)
        print(sorted_lines[i])
        print("* " + str(i)+": " + str(sorted_lines[i]))
        key = sorted_lines[i]
        #print(key)
        for y in range(sheet.ncols):
            text = sheet.cell_value(key, y)
            worksheet.write(len(sorted_lines)-i, y, text)
            #print(str(i) + " " + str(y))
            #print(text)

    workbook.close()

# if __name__ == '__main__':
#     sort()


















    ##
