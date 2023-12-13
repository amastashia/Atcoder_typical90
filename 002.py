N = int(input())
if N%2==1:
    print()
else:
    result_list = []
    for i in range(2**N):
        bin_str = format(i, f'0{N}b')
        count_0 = 0
        count_1 = 0
        result = ''
        for bin in bin_str:
            if bin == '0':
                result += '('
                count_0 += 1
            else:
                result += ')'
                count_1 += 1
            if count_0 < count_1:
                break
        if count_0 == count_1:
            result_list.append(result)

    result_list.sort()
    for output in result_list:
        print(output)