import os
import json
import unittest
import subprocess
from gradescope_utils.autograder_utils.decorators import weight

class TestQuestions(unittest.TestCase):

    def run_process(self, pargs, txt_in, tmt):
        try:
            process = subprocess.run(pargs, stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=txt_in, shell=False, timeout=tmt, check=True)
        except subprocess.CalledProcessError as p:
            self.fail("Program Crashed with exit code={}".format(-p.returncode))
        except subprocess.TimeoutExpired:
            self.fail("Timeout Ocurred (max {} secs)".format(tmt))
        except Exception as e:
            self.fail("Program Crashed with unknown exception: {}".format(str(e)))
        return process.stdout, process.stderr

    def fail_test_case(self, _out, _in, _num, _truth, _n):
        threshold1 = int(0.1 * _n) # show input + output + truth
        threshold2 = int(0.6 * _n) # show input + output
        threshold3 = int(0.85 * _n) # show output
        msg = 'invalid output for test case {}/{}\n'.format(_num,_n)
        if _num <= threshold3:
            msg += '+ Your output: "{}"'.format(_out)
        if _num <= threshold2:
            msg += '\n+ Input: "{}"'.format(_in)
        if _num <= threshold1:
            msg += '\n+ Expected output: "{}"'.format(_truth)
        return msg
    
    def fail_n_lines(self, _out, _truth, _num, _n):
        msg = 'number of lines differ for test case {}/{}'.format(_num, _n)
        msg += '\n+ Your output contains {} line(s)'.format(len(_out))
        msg += '\n+ The expected output contains {} line(s)'.format(len(_truth))
        return msg

    def run_tests(self, name, id):
        progfname = './prog-' + str(id)
        errorfname = './error-' + str(id) + '.log'
        # make sure program exists
        if not os.path.exists(progfname):
            if os.path.exists(errorfname):
                with open(errorfname, 'rt') as fid:
                    self.fail("Compiler/Linker error:\n\n"+fid.read().replace('/autograder/submission/', ''))
        # read the test data
        with open('./tests/json/{}.json'.format(name), 'rt') as fin:
            data = json.load(fin)
        # iterate over all test cases
        for tc in data['tests']:
            out, err = self.run_process([progfname], tc['input'].encode(), 2)
            outlines = out.decode(errors='backslashreplace').rstrip('\r\n').splitlines()
            truth = tc['output'].rstrip('\r\n').splitlines()
            if len(outlines) != len(truth):
                self.fail(self.fail_n_lines(outlines, truth, tc['case'], len(data['tests'])))
            for j in range(len(outlines)):
                o1 = outlines[j].rstrip('\r\n')
                o2 = truth[j].rstrip('\r\n')
                # if the output is different
                if o1 != o2:
                    self.fail(self.fail_test_case(o1, tc['input'], tc['case'], o2, len(data['tests'])))

    @weight(5)
    def test01(self):
        '''addition'''
        self.run_tests('addition', 1)

    @weight(5)
    def test02(self):
        '''subtraction'''
        self.run_tests('subtraction', 2)

    @weight(5)
    def test03(self):
        '''division'''
        self.run_tests('division', 3)

    @weight(5)
    def test04(self):
        '''all'''
        self.run_tests('all', 4)

    @weight(5)
    def test05(self):
        '''odd-or-even'''
        self.run_tests('odd-or-even', 5)

    @weight(5)
    def test06(self):
        '''pos-or-neg'''
        self.run_tests('pos-or-neg', 6)

    @weight(5)
    def test07(self):
        '''larger-than-100'''
        self.run_tests('larger-than-100', 7)

    @weight(5)
    def test08(self):
        '''last-digit-is-9'''
        self.run_tests('last-digit-is-9', 8)

    @weight(5)
    def test09(self):
        '''privileges'''
        self.run_tests('privileges', 9)

    @weight(5)
    def test10(self):
        '''word-for-number'''
        self.run_tests('word-for-number', 10)

    @weight(5)
    def test11(self):
        '''date-converter'''
        self.run_tests('date-converter', 11)

    @weight(5)
    def test12(self):
        '''average'''
        self.run_tests('average', 12)

    @weight(5)
    def test13(self):
        '''smallest-number'''
        self.run_tests('smallest-number', 13)

    @weight(5)
    def test14(self):
        '''which-quadrant'''
        self.run_tests('which-quadrant', 14)

    @weight(5)
    def test15(self):
        '''is-it-cold-out'''
        self.run_tests('is-it-cold-out', 15)

    @weight(5)
    def test16(self):
        '''temperature-converter'''
        self.run_tests('temperature-converter', 16)

    @weight(5)
    def test17(self):
        '''grades'''
        self.run_tests('grades', 17)

    @weight(7.5)
    def test18(self):
        '''day-of-the-week'''
        self.run_tests('day-of-the-week', 18)

    @weight(7.5)
    def test19(self):
        '''triangles'''
        self.run_tests('triangles', 19)

    @weight(10)
    def test20(self):
        '''HelloWorld'''
        self.run_tests('HelloWorld', 20)

    @weight(10)
    def test21(self):
        '''iostream'''
        self.run_tests('iostream', 21)