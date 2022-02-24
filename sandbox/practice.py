input_list: list[int] = list()
i: int = 0
   
while i < len(input_list):
    if input_list[i] % 2 == 0:
        print(input_list[i])
        i += 1
