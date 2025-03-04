def test(list):
    result={}
    for item in list:
        result[item[0]] =item[1:]
        return result
    
    student=[[1,'abc','12'],[2,'xyz','11'],[3,'cat','12'],[4,'dog','12']]
    print("original list:")
    print(student)
    print("converted list:")
    print(test(student))

    