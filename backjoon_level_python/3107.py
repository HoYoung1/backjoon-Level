PART_COUNT = 8

if __name__ == '__main__':
    abbreviated_ipv6 = input()
    divided_ipv6 = abbreviated_ipv6.split(':')
    for idx, part in enumerate(divided_ipv6):
        if len(part) == 0:
            removed_idx = idx
        zero_count = 4 - len(part)
        part = '0' * zero_count + part
        divided_ipv6[idx] = part

    # print(divided_ipv6)

    for i in range(PART_COUNT - len(divided_ipv6)):
        divided_ipv6.insert(removed_idx, '0000')

    if len(divided_ipv6) > 8:
        del divided_ipv6[removed_idx]
    print(':'.join(divided_ipv6))


