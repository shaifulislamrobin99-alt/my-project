import sys
import time
from decimal import Decimal, getcontext

def simple_infinite_pi():                                   getcontext().prec = 50

    with open('pi.txt', 'w') as f:
        print('3.', end='', flush=True)
        f.write('3.')
        f.flush()

        digits_on_current_line = 0
        precision_digits = 0
                                                                try:
            while True:                                                 precision_digits += 1
                getcontext().prec = max(50, precision_digits + 50)

                pi_over_4 = Decimal(0)
                sign = 1
                denominator = 1

                iterations = max(1000, precision_digits * 100)

                for _ in range(iterations):
                    term = Decimal(sign) / Decimal(denominator)
                    pi_over_4 += term
                    sign *= -1
                    denominator += 2

                pi = pi_over_4 * 4
                pi_str = str(pi)

                decimal_index = pi_str.find('.')
                if decimal_index != -1 and len(pi_str) > decimal_index + precision_digits:
                    digit = pi_str[decimal_index + precision_digits]

                    sys.stdout.write(digit)                                 sys.stdout.flush()

                    f.write(digit)                                          f.flush()
                                                                            digits_on_current_line += 1         
                    if digits_on_current_line % 50 == 0:                        sys.stdout.write('\n')
                        sys.stdout.flush()                                      f.write('\n')
                        f.flush()                       
                    time.sleep(0.001)                                                                                   except KeyboardInterrupt:
            print('\n')                                             f.write('\n')                               
simple_infinite_pi()
