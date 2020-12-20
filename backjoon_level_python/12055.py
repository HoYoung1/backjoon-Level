from typing import List
import sys
input = sys.stdin.readline

def solve(n: int, ips: List[str]) -> List[str]:
    first_ip = ips[0]
    last_ip = ips[-1]

    common_bit_count = get_common_bit_num(ip_to_32bit(first_ip), ip_to_32bit(last_ip))
    subnet_bit = get_subnet_bit(common_bit_count)
    subnetwork = bit_to_network(subnet_bit)

    network = get_network_address(first_ip, subnetwork)
    return [network, subnetwork]


def deciaml_to_bin(n) -> str:
    return format(n, 'b')


def bin_to_decimal(b: str):
    return int(b, 2)


def bit_to_network(subnetbit: str):
    return '{}.{}.{}.{}'.format(
        bin_to_decimal(subnetbit[:8]),
        bin_to_decimal(subnetbit[8:16]),
        bin_to_decimal(subnetbit[16:24]),
        bin_to_decimal(subnetbit[24:32])
    )


def get_subnet_bit(n: int) -> str:
    result = ''
    for i in range(1, 33):
        if i <= n:
            result += '1'
        else:
            result += '0'
    return result


def ip_to_32bit(ip: str) -> str:
    result = ''
    num_list = list(map(int, ip.split('.')))
    for num in num_list:
        bits = deciaml_to_bin(num)
        bits = '0'*(8-len(bits)) + bits
        result += bits
    return result


def get_common_bit_num(ip1_bits, ip2_bits) -> int:
    result = 0
    for bit1, bit2 in zip(ip1_bits, ip2_bits):
        if bit1 == bit2:
            result += 1
        else:
            break
    return result


def get_network_address(ip, cnt):
    # subnet_bit = ip_to_32bit(subnet)
    # cnt = subnet_bit.count('1')
    # return ip[:cnt] + '0' * 32-cnt
    return bit_to_network(ip_to_32bit(ip)[:cnt] + '0' * (32 - cnt))


if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(T):
        n = int(input().rstrip())
        # ips = [input() for _ in range(n)]
        answer = []
        for _ in range(n):
            ips = [input().rstrip()]
            ip, prefix = ips[0].split('/')
            net = get_network_address(ip, int(prefix))
            # print(net)
            # print(prefix)
            answer.append((net, prefix))
            answer.sort(key=lambda ip_prefix: (ip_to_32bit(ip_prefix[0]), int(ip_prefix[1])))
        print(f"Case #{i+1}:")
        for net, prefix in answer:
            print(f"{net}/{prefix}")

        # print(subnet)

    # assert get_subnet_bit(24) == '11111111111111111111111100000000'
    # assert bit_to_network('11111111111111111111111100000000') == '255.255.255.0'
    # assert ip_to_32bit('194.85.160.176') == '11000010010101011010000010110000'
    # assert get_common_bit_num(ip_to_32bit('194.85.160.177'), ip_to_32bit('194.85.160.183')) == 29
    # assert get_common_bit_num(ip_to_32bit('194.85.160.177'), ip_to_32bit('194.85.160.178')) == 30
    #
    # assert get_network_address('194.85.160.177', '255.255.255.248') == '194.85.160.176'
    # assert get_network_address('194.85.160.177', '255.255.255.0') == '194.85.160.0'
    # assert get_network_address('194.85.160.177', '255.255.0.0') == '194.85.0.0'
    #
    # assert solve(3, ['194.85.160.177', '194.85.160.183', '194.85.160.178']) == ['194.85.160.176', '255.255.255.248']