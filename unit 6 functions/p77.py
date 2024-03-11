numList = [4, 5, 6]
strList = ['four', 'five', 'six']
# No iterables are passed
result = zip()
# Converting iterator to list
resultList = list(result)
print(resultList)
# Two iterables are passed
result = zip(numList, strList)
# Converting iterator to set
resultSet = set(result)
print(resultSet)
# resultSet = list(result)
# print(resultSet)
# resultSet = dict(result)
# print(resultSet)