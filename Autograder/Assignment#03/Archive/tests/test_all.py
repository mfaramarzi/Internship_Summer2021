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

    @weight(10)
    def test01(self):
        '''count_first'''
        self.run_tests('count_first', 1)

    @weight(10)
    def test02(self):
        '''palindrome'''
        self.run_tests('palindrome', 2)

    @weight(10)
    def test03(self):
        '''reverse'''
        self.run_tests('reverse', 3)

    @weight(10)
    def test04(self):
        '''sorted'''
        self.run_tests('sorted', 4)

    @weight(10)
    def test05(self):
        '''filter_dups'''
        self.run_tests('filter_dups', 5)

    @weight(10)
    def test06(self):
        '''str_hash'''
        self.run_tests('str_hash', 6)

    @weight(15)
    def test07(self):
        '''diameter'''
        self.run_tests('diameter', 7)

    @weight(10)
    def test08(self):
        '''unique'''
        self.run_tests('unique', 8)

    @weight(15)
    def test09(self):
        '''same_gmail'''
        self.run_tests('same_gmail', 9)

    @weight(15)
    def test10(self):
        '''hostname'''
        self.run_tests('hostname', 10)
