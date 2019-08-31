#tuple.py
#튜플은 값을 변경할 수 없습니다.
#리스트와 동일하지만 값을 변경할 수는 없습니다.
#값을 변경하는 함수를 제공하지 않습니다.
#* strOp.py 할 때부터 주피터 노트북 커널이 죽어서 런이 안됩니다 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ*
#*[W 11:52:58.533 NotebookApp] Kernel bbec3506-8adf-4174-82fa-ba3bc33af0f4 died, removing from map.*

my_tuple = ('x', 'y', 'z')
your_tuple = (3,4,5,6,7)
print(my_tuple)
print(your_tuple)
print(my_tuple[1])
our_tuple = my_tuple + your_tuple
print(our_tuple)