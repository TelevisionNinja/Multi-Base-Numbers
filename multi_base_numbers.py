def _pad_left(a_list, padding_element, length):
    for _ in range(length - len(a_list)):
        a_list.insert(0, padding_element)


def _remove_leading_element(a_list):
    if a_list:
        while a_list[0] == 0:
            del a_list[0]

            if not a_list:
                a_list = [0]
                break
    return a_list


def _compare_numbers_represented_as_arrays(list_1, list_2):
    """
    compares two numbers that are represented as lists

    both lists must be the same length

    1 : list 1 is greater
    0 : both are equal
    -1 : list 2 is greater
    """

    for value_1, value_2 in zip(list_1, list_2):
        if value_2 > value_1:
            return -1
        if value_1 > value_2:
            return 1

    return 0


def _make_lists_equal_length(list_1, list_2, base_bool):
    length_1 = len(list_1)
    length_2 = len(list_2)

    if length_1 != length_2:
        max_len = max(length_1, length_2)

        _pad_left(list_1, 0, max_len)

        if base_bool:
            _pad_left(list_2, list_2[0], max_len)
        else:
            _pad_left(list_2, 0, max_len)


def _make_whole_list_negative(a_list):
    for x in range(len(a_list)):
        if a_list[x] > 0:
            a_list[x] *= -1
    return a_list


def _format_into_regular_negative_number(a_list):
    for x in range(len(a_list)):
        if a_list[x] < 0:
            a_list[x] *= -1
    a_list[0] *= -1
    return a_list


def _check_if_negative(a_list):
    if a_list[0] < 0:
        a_list = _make_whole_list_negative(a_list)
    return a_list


def _formate_numbers(num_list_1, num_list_2):
    num_list_1 = _check_if_negative(num_list_1)
    num_list_2 = _check_if_negative(num_list_2)
    
    _make_lists_equal_length(num_list_1, num_list_2, False)


def add(num_list_1, num_list_2, base_list):
    """
    num_list_1 + num_list_2

    base_list is a list of the bases of the 2 numbers this function is supposed to work with
    """
    
    _formate_numbers(num_list_1, num_list_2)
    
    return clean_up_bases([x + y for x, y in zip(num_list_1, num_list_2)], base_list)


def subtract(num_list_1, num_list_2, base_list):
    """
    num_list_1 - num_list_2

    base_list is a list of the bases of the 2 numbers this function is supposed to work with
    """

    _formate_numbers(num_list_1, num_list_2)

    negative_flag = _compare_numbers_represented_as_arrays(num_list_1, num_list_2)

    if negative_flag == -1:
        num_list_1, num_list_2 = num_list_2, num_list_1

    result = clean_up_bases([x - y for x, y in zip(num_list_1, num_list_2)], base_list)

    if negative_flag == -1 and result[0] > 0:
        result[0] *= -1

    return result


def clean_up_bases(a_list, base_list):
    """
    this "cleans up" the result of the addition or subtraction to give the right asnwer to the operation

    since there is a chance the list of bases is not long enough to include a base for the carry,
    like -99 - 1 = -100 where the list of bases may be [10, 10],
    this function tries to correct the carry by extending the list of bases using the most significant base
    """
    a_list = clean_up_bases_ignore_most_significant_digit(a_list, base_list)

    # test for length
    # this deals with the most significant digit if the positive or negative value of it is greater than or euqal to the base
    
    if len(a_list) > len(base_list):
        while a_list[0] >= base_list[0] or -a_list[0] >= base_list[0]:
            carry = 0

            if -a_list[0] >= base_list[0]:
                a_list[0] *= -1
                carry = -(a_list[0] // base_list[0])
            else:
                carry = a_list[0] // base_list[0]
            
            a_list.insert(0, carry)
            a_list[1] = a_list[1] % base_list[0]

    return a_list


def clean_up_bases_ignore_most_significant_digit(a_list, base_list):
    """
    this "cleans up" the result of the addition or subtraction to give the right asnwer to the operation

    since there is a chance the list of bases is not long enough to include a base for the carry,
    like -99 - 1 = -100 where the list of bases may be [10, 10],
    this function will not try to correct the carry or the -1 in the example
    """
    if a_list[0] == 0:
        a_list = _remove_leading_element(a_list)

    for x in a_list:
        if x > 0:
            break
    else:
        a_list = _format_into_regular_negative_number(a_list)

    a_list.reverse()
    base_list.reverse()

    for x, (value, base) in enumerate(zip(a_list, base_list)):
        if value >= base or value < 0:
            carry = 0
            if -value >= base:
                value *= -1
                carry = -(value // base)
            else:
                carry = value // base # floor division
            
            if x < len(a_list) - 1:
                a_list[x + 1] += carry
            else:
                if value < base:
                    break
                a_list.append(carry)
            a_list[x] = value % base

    a_list.reverse()
    base_list.reverse()

    # removing leading zeros that may show up
    if a_list[0] == 0:
        a_list = _remove_leading_element(a_list)

    return a_list