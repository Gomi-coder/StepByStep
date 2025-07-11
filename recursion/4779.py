# 백준 4779 칸토어 집합 (https://www.acmicpc.net/problem/4779)

def cantor_set(target_str):
    total_len = len(target_str)

    if total_len < 3: return target_str

    num_of_sections = total_len//3

    first_section_str = target_str[:num_of_sections]
    third_section_str = target_str[-num_of_sections:]
    second_section_str = " " * num_of_sections

    return cantor_set(first_section_str) + second_section_str + cantor_set(third_section_str)