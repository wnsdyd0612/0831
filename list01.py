#list01.py

#����Ʈ�� ����� ���ؼ��� ���ȣ([])�� ����Ѵ�
#��ȣ (()), �߰�ȣ ({}), ���ȣ ([])
#len() �Լ��� ���� ����Ʈ �� ������ ���� ����.
#max() �Լ��� min() �Լ��� �ִ�/�ּ� ���� ã�´�.
#count() �Լ��� ����Ʈ �� Ư�� ���� ������ Ƚ���� ����.

a_list = [1,2,3]
print(a_list)
print("a_list has {} elements.".format(len(a_list)))
print("the maximum value in a_list is {}.".format(max(a_list)))
print("the minimum value in a_list is {}.".format(min(a_list)))
another_list = ['printer', 5, ['star', 'circle', 9]]
print(another_list)
print("another_list also has {} elements.".format(len(another_list)))
print("5 is another_list {} time.".format(another_list.count(5)))
print(a_list[0])
print(a_list[1])
print(a_list[2])
print(a_list[-1])
print(a_list[-2])
print(a_list[0:2])