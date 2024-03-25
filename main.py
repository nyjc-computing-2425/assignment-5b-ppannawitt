# Part 1
def read_csv(filename):
  '''Read filename and return its '''
  header = []
  data = []
  with open(filename, 'r') as f:
    header = f.readline().strip().split(',')
    for line in f:
      newline = line.strip().split(',')
      newline[0] = int(newline[0])
      newline[3] = int(newline[3])
      data.append(newline)
  return (header, data)
    
# Part 2
def filter_gender(enrolment_by_age, sex):
  '''return a list of data with has header==sex'''
  filtered_record = []
  for line in enrolment_by_age:
    if line[2] == sex:
      filtered_record.append([line[0], line[1], line[3]])
  return filtered_record


# Part 3
def sum_by_year(enrolment):
  '''return a pair of year and total enrolemnt of that year'''
  dict = {}
  enrolment_by_year = []
  for line in enrolment:
    year = line[0]
    if year not in dict:
      dict[year] = 0
    dict[year]+=line[2]
  for key in dict:
    enrolment_by_year.append([key, dict[key]])
  return enrolment_by_year
  
# Part 4
def write_csv(filename, header, data):
  '''write header and data to filename '''
    # Type your code below
  file = open(filename, 'w')
  file.writelines(header)
  counter = 0
  for line in data:
    for i in range(len(line)):
      line[i] = str(line[i])
    file.writelines(','.join(line))
    counter+=1
  file.close()
  return counter

"""

Sample Grader:
enrolment_header = read_csv('pre-u-enrolment-by-age.csv')[0]
enrolment_data = read_csv('pre-u-enrolment-by-age.csv')[1]
print(enrolment_header, enrolment_data)
mf_enrolment = filter_gender(enrolment_data, "MF")
print(mf_enrolment)
enrolment_by_year = sum_by_year(enrolment_data)
print(enrolment_by_year)
filename = 'total-enrolment-by-year.csv'
header = ["year", "total_enrolment"]
print(write_csv(filename, header, enrolment_by_year))
"""