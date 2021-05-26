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
        thr1 = int(0.20 * tot) # show input + output + truth
        thr2 = int(0.80 * tot) # show input + output
        thr3 = int(0.95 * tot) # show output
        msg = '{}/{} {}\n\n'.format(case, tot, root)
        if case <= thr3 and myout != None:
            msg += '=> Your output (line {}/{}):\n\n{}\n\n'.format(l_nbr, n_lines, myout)
        if case <= thr2 and myin != None:
            msg += '=> Input:\n\n{}\n\n'.format(myin)
        if case <= thr1 and truth != None:
            msg += '=> Expected output (line {}/{}):\n\n{}\n\n'.format(l_nbr, n_lines, truth)
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
                self.my_fail('Output: {} line(s), Expected: {} line(s)'.format(len(outlines),len(truth)), tc['case'], n_cases, myin=tc['input'])
            for j in range(len(outlines)):
                o1 = outlines[j].rstrip('\r\n')
                o2 = truth[j].rstrip('\r\n')
                # if the output is different
                if o1 != o2:
                    self.my_fail('Invalid Output', tc['case'], n_cases, myin=tc['input'], myout=o1, l_nbr=j+1, n_lines=len(outlines), truth=o2)

    @weight(30)
    def test01(self):
        '''sudoku_checker'''
        self.run_tests('sudoku_checker', 1)

    @weight(30)
    def test02(self):
        '''game_of_life'''
        self.run_tests('game_of_life', 2)

    @weight(30)
    def test03(self):
        '''sliding_puzzle'''
        self.run_tests('sliding_puzzle', 3)

    @weight(30)
    def test04(self):
        '''k_nearest_neighbors'''
        self.run_tests('k_nearest_neighbors', 4)
