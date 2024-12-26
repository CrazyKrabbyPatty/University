def solution(line:str, markers:list):
    '''
    :param line: исходный текст
    :param markers: список, содержащий строки, после которых текст должен быть удалён
    :return: возвращает изменённую строку, где на каждой строчке текст после маркера удалён
    '''
    result_lines = []
    lines = line.splitlines()
    for l in lines:
        for marker in markers:
            if marker in l:
                l = l.split(marker)[0]
        result_lines.append(l.rstrip())

    return '\n'.join(result_lines)

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
print(result)