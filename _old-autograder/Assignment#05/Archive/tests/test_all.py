import os
import glob
import filecmp
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

    def run_tests(self, testfname, folder, id):
        progfname = './prog-{}'.format(id)
        solfname = './sol-{}'.format(id)
        errorfname = './error-{}.log'.format(id)
        # make sure program exists
        if not os.path.exists(progfname):
            if os.path.exists(errorfname):
                with open(errorfname, 'rt') as fid:
                    self.fail('Compiler/Linker Error\n\n'+fid.read().replace('/autograder/submission/', ''))
        # read the test data
        with open('{}/{}'.format(folder,testfname), 'rt') as fin:
            data = fin.readlines()
        # iterate over all test cases
        self.n_cases = len(data)
        for idx, tc in enumerate(data):
            tc = tc.strip()
            line = tc.split()
            # run student program
            arglist = [progfname] + [folder+line[0]] + line[1:]
            out, err = self.run_process(arglist, tc, 5, idx+1, self.n_cases)
            outlines = out.decode(errors='backslashreplace').rstrip('\r\n').splitlines()
            # run solution
            arglist = [solfname] + [folder+line[0]] + line[1:]
            tout, terr = self.run_process(arglist, '', 5, None, None)
            toutlines = tout.decode(errors='backslashreplace').rstrip('\r\n').splitlines()
            if len(outlines) != len(toutlines):
                self.my_fail('Output: {} line(s), Expected: {} line(s)'.format(len(outlines),len(toutlines)), idx+1, self.n_cases, myin=tc)
            for j in range(len(outlines)):
                o1 = outlines[j].rstrip('\r\n')
                o2 = toutlines[j].rstrip('\r\n')
                # if the output is different
                if o1 != o2:
                    self.my_fail('Invalid Output', idx+1, self.n_cases, myin=tc, myout=o1, l_nbr=j+1, n_lines=len(outlines), truth=o2)

    @weight(30)
    def test01(self):
        '''cells'''
        self.run_tests('cells.tests', './tests/data/board/', 1)

    @weight(30)
    def test02(self):
        '''blobs'''
        self.run_tests('blobs.tests', './tests/data/board/', 2)

    @weight(30)
    def test03(self):
        '''sudoku'''
        self.run_tests('sudoku.tests', './tests/data/sudoku/', 3)

    @weight(30)
    def test04(self):
        '''binarize'''
        self.run_tests('binarize.tests', './tests/data/binarize/', 4)
        files = glob.glob('*.bw')
        if len(files) != self.n_cases:
            self.fail('Solutions were not generated for all test cases', '')
        for i in range(self.n_cases):
            if not filecmp.cmp(files[i], files[i][:-3]):
                self.my_fail('BMP files differ', i+1, self.n_cases, myin=None, myout=None, l_nbr=None, n_lines=None, truth=None)