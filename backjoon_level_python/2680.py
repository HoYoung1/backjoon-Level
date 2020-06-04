class QRdecoder:
    def __init__(self):
        pass

    def decode(self, encoded):
        result_decoded = ''
        result_num_character = 0

        binary = self._encoded_to_bin(encoded)

        # mode_bit = binary[:4]
        bit_pointer = 0
        while len(binary[bit_pointer:]) > 4:
            mode_bit = binary[bit_pointer:bit_pointer + 4]
            bit_pointer += 4
            if mode_bit == '0001':
                count_bits = 10
                data_bits = 10
                count_num = int(binary[bit_pointer:bit_pointer + count_bits], 2)

                bit_pointer += count_bits
                # 문자열이 2글자일 경우엔 7bit로, 1글자일 경우엔 4bit로 저장한다
                remainder = count_num % 3
                if remainder == 2:
                    temp = 7
                elif remainder == 1:
                    temp = 4
                else:
                    temp = 0
                increase_bit = (count_num // 3) * data_bits + temp

                decoded = self._numeric(binary[bit_pointer:bit_pointer + increase_bit])
                result_decoded += decoded
                result_num_character += count_num

                bit_pointer += increase_bit

            elif mode_bit == '0010':
                count_bits = 9
                data_bits = 11
                count_num = int(binary[bit_pointer:bit_pointer + count_bits], 2)

                bit_pointer += count_bits
                # 만일 한 개의 문자가 남는다면, 이것은 6 비트로 인코딩된다.
                remainder = count_num % 2
                if remainder == 1:
                    temp = 6
                else:
                    temp = 0
                increase_bit = (count_num // 2) * data_bits + temp

                decoded = self._alpha_numeric(binary[bit_pointer:bit_pointer + increase_bit])
                result_decoded += decoded
                result_num_character += count_num

                bit_pointer += increase_bit
            elif mode_bit == '0100':
                count_bits = 8
                data_bits = 8
                count_num = int(binary[bit_pointer:bit_pointer + count_bits], 2)

                bit_pointer += count_bits
                increase_bit = count_num * data_bits

                decoded = self._8bit_byte(binary[bit_pointer:bit_pointer + increase_bit])
                result_decoded += decoded
                result_num_character += count_num

                bit_pointer += increase_bit
            elif mode_bit == '1000':
                count_bits = 8
                data_bits = 13
                count_num = int(binary[bit_pointer:bit_pointer + count_bits], 2)

                bit_pointer += count_bits
                increase_bit = count_num * data_bits

                decoded = self._kanji(binary[bit_pointer:bit_pointer + increase_bit])
                result_decoded += decoded
                result_num_character += count_num

                bit_pointer += increase_bit
            elif mode_bit == '0000':
                break

        return result_num_character, result_decoded

    @staticmethod
    def _encoded_to_bin(encoded):
        result = ''
        for s in encoded:
            result += bin(int(s, 16))[2:].zfill(4)
        return result

    def _numeric(self, bits):
        result = ''
        pointer = 0
        while len(bits[pointer:]) >= 10:
            result += str(int(bits[pointer:pointer + 10], 2)).zfill(3)
            pointer += 10
        result += str(int(bits[pointer:], 2))
        return result

    def _alpha_numeric(self, bits):  # 스페이스바 확인
        alpha_numerics = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:'
        result = ''
        pointer = 0
        key = 45
        while len(bits[pointer:]) >= 11:
            temp = int(bits[pointer:pointer + 11], 2)
            result += alpha_numerics[temp // key]
            result += alpha_numerics[temp % key]
            pointer += 11
        if bits[pointer:]:
            result += alpha_numerics[int(bits[pointer:], 2)]
        return result

    def _8bit_byte(self, bits):
        result = ''
        pointer = 0
        while len(bits[pointer:]) >= 8:
            temp = hex(int(bits[pointer:pointer + 8], 2))[2:].zfill(2)
            if int(0x20) <= int(temp, 16) <= int(0x7e):
                temp_chr = chr(int(temp, 16))
                if temp_chr == '\\':
                    temp_chr = '\\\\'
                elif temp_chr == '#':
                    temp_chr = '\#'
                result += temp_chr
            else:
                result += '\\' + temp.upper()
            pointer += 8
        return result

    def _kanji(self, bits):
        result = ''
        pointer = 0
        while len(bits[pointer:]) >= 13:
            result += '#' + hex(int(bits[pointer:pointer + 13], 2))[2:].zfill(4)
            pointer += 13
        return result.upper()


if __name__ == '__main__':
    P = int(input())
    qr_decoder = QRdecoder()
    for _ in range(P):
        qr_contents = input()
        num_character, decoded = qr_decoder.decode(qr_contents)
        print('{} {}'.format(num_character, decoded))

    assert QRdecoder._encoded_to_bin(
        '10207B72271014E77390900D164A8C00EC11EC') == '00010000001000000111101101110010001001110001000000010100111001110111001110010000100100000000110100010110010010101000110000000000111011000001000111101100'

    assert qr_decoder._numeric('000111101101110010001001110') == '12345678'
    assert qr_decoder._alpha_numeric('0011100111011100111001000010') == 'AC-42'
    assert qr_decoder._8bit_byte('010001011001001010100011') == 'E\92\A3'
    assert qr_decoder._kanji('11010101111000001101000101') == '#1ABC#0345'

    assert qr_decoder.decode('10207B72271014E77390900D164A8C00EC11EC') == (16, '12345678AC-42E\92\A3')
    assert qr_decoder.decode('802D5E0D1400EC11EC11EC11EC11EC11EC11EC') == (2, '#1ABC#0345')
    assert qr_decoder.decode('20BB1AA65F9FD7DC0ED88C973E15EF533EB0EC') == (23, 'HTTP://WWW.ACMGNYR.ORG/')
    assert qr_decoder.decode('2010B110888D9428D937193B9CEA0D7F45DF68') == (36, '3.1415926535897932384626433832795028')

    assert qr_decoder.decode('10A40C566A6E14EA8DF7A1EDC8C540C566A6B4') == (41, '01234567890123456789012345678901234567890')
    assert qr_decoder.decode('20C9CD452A1570B3D732FD628CADA13596E0C4') == (25, 'ABCDEFGHIJKLMNOPQRSTUVWXY')
    assert qr_decoder.decode('4116162636465666768696A6B6C6D6E6F70710') == (17, 'abcdefghijklmnopq')
    assert qr_decoder.decode('80A111D59D135BCD77FC48C8AD78955E77BC00') == (10, '#0223#1567#089A#1BCD#0EFF#1123#0456#1789#0ABC#1DEF')
    assert qr_decoder.decode('102BDBA3941000EC11EC11EC11EC11EC11EC11') == (10, '9876543210')
    assert qr_decoder.decode('20A0010BA2E48A971C97A9F81F5FF760EC11EC') == (20, '0123456789Z $%*+-./:')


