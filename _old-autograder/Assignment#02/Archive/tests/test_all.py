import os
import json
import unittest
import subprocess
from gradescope_utils.autograder_utils.decorators import weight

class TestQuestions(unittest.TestCase):

    def run_process(self, pargs, myin, tmt, case, tot):
        try:
            process = subprocess.run(pargs, stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=myin.encode(), shell=False, timeout=tmt, check=True)
        except subprocess.CalledProcessError as p:
            self.my_fail('Program Crashed with Exit Code {}'.format(-p.returncode), case, tot, myin)
        except subprocess.TimeoutExpired:
            self.my_fail('Timeout Ocurred (max {} secs)'.format(tmt), case, tot, myin)
        except Exception as e:
            self.my_fail('Program Crashed with Exception: {}'.format(str(e)), case, tot, myin)
        return process.stdout, process.stderr
    
    def my_fail(self, root, case, tot, myin=None, myout=None, l_nbr=None, n_lines=None, truth=None):
        thr1 = int(0.15 * tot) # show input + output + truth
        thr2 = int(0.75 * tot) # show input + output
        thr3 = int(0.9 * tot) # show output
        msg = '{}/{}\n{}\n\n'.format(case, tot, root)
        if case <= thr3 and myout != None:
            msg += ' + Your output (line {}/{}): "{}"\n'.format(l_nbr, n_lines, myout)
        if case <= thr2 and myin != None:
            msg += ' + Input: "{}"\n'.format(myin)
        if case <= thr1 and truth != None:
            msg += ' + Expected output (line {}/{}): "{}"\n'.format(l_nbr, n_lines, truth)
        self.fail(msg.rstrip())

    def run_tests(self, name, id):
        progfname = './prog-' + str(id)
        errorfname = './error-' + str(id) + '.log'
        # make sure program exists
        if not os.path.exists(progfname):
            if os.path.exists(errorfname):
                with open(errorfname, 'rt') as fid:
                    self.fail("Compiler/Linker Error\n\n"+fid.read().replace('/autograder/submission/', ''))
        # read the test data
        with open('./tests/json/{}.json'.format(name), 'rt') as fin:
            data = json.load(fin)
        # iterate over all test cases
        n_cases = len(data['tests'])
        for tc in data['tests']:
            out, err = self.run_process([progfname], tc['input'], 2, tc['case'], n_cases)
            outlines = out.decode(errors='backslashreplace').rstrip('\r\n').splitlines()
            truth = tc['output'].rstrip('\r\n').splitlines()
            if len(outlines) != len(truth):
                self.my_fail('Output: {} line(s), Expected Output: {} line(s)'.format(len(outlines),len(truth)), tc['case'], n_cases, myin=tc['input'])
            for j in range(len(outlines)):
                o1 = outlines[j].rstrip('\r\n')
                o2 = truth[j].rstrip('\r\n')
                # if the output is different
                if o1 != o2:
                    self.my_fail('Invalid Output', tc['case'], n_cases, myin=tc['input'], myout=o1, l_nbr=j+1, n_lines=len(outlines), truth=o2)

    @weight(5)
    def test01(self):
        '''draw_triangle_1'''
        self.run_tests('draw_triangle_1', 1)

    @weight(5)
    def test02(self):
        '''draw_triangle_2'''
        self.run_tests('draw_triangle_2', 2)

    @weight(5)
    def test03(self):
        '''factorial'''
        self.run_tests('factorial', 3)

    @weight(5)
    def test04(self):
        '''pow'''
        self.run_tests('pow', 4)

    @weight(5)
    def test05(self):
        '''prime'''
        self.run_tests('prime', 5)

    @weight(5)
    def test06(self):
        '''suffix_sum'''
        self.run_tests('suffix_sum', 6)

    @weight(5)
    def test07(self):
        '''sum_even'''
        self.run_tests('sum_even', 7)

    @weight(5)
    def test08(self):
        '''x_of_stars'''
        self.run_tests('x_of_stars', 8)

    @weight(5)
    def test09(self):
        '''draw_triangle_3'''
        self.run_tests('draw_triangle_3', 9)

    @weight(5)
    def test10(self):
        '''loan_payment'''
        self.run_tests('loan_payment', 10)

    @weight(5)
    def test11(self):
        '''char_pyramid'''
        self.run_tests('char_pyramid', 11)

    @weight(5)
    def test12(self):
        '''rgb_to_hex'''
        self.run_tests('rgb_to_hex', 12)

    @weight(5)
    def test13(self):
        '''armstrong'''
        self.run_tests('armstrong', 13)

    @weight(5)
    def test14(self):
        '''perfect'''
        self.run_tests('perfect', 14)

    @weight(10)
    def test15(self):
        '''a_lovely_rug'''
        self.run_tests('a_lovely_rug', 15)

    @weight(10)
    def test16(self):
        '''circular_prime'''
        self.run_tests('circular_prime', 16)

    @weight(10)
    def test17(self):
        '''knight_moves'''
        self.run_tests('knight_moves', 17)