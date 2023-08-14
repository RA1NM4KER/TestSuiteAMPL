import os
from re import U
import subprocess
import sys
from dataclasses import dataclass
import difflib as dl


class Util:

    @staticmethod
    def get_argument():
        return sys.argv

    @staticmethod
    def get_directory(folder, argument):
        return os.listdir("./" + "TestCases/" + folder + argument + "/")

    @staticmethod
    def make(test):
        os.chdir("../ampl/src")
        print("--- make " + test + " " + ("-" * 63))
        os.system("make " + test)
        print("-" * 80)
        os.chdir("../../TestSuiteAMPL")


class Difference:
    results_folder = ''

    def __init__(self, folder):
        self.results_folder = folder

    def display_differences(self, l):
        for file in l:
            s1 = file[1].splitlines()
            print("\033[1;30;41m%s%s\033[0m" % ("DIFFERENCES IN FILE: ", file[0]))
            with open('./Results/' + self.results_folder + '/' + file[0] + '.txt') as f:
                s2 = f.read().splitlines()
            for diff in dl.context_diff(s1, s2):
                print(diff)


class Test:
    fails = list()

    @dataclass
    class Stats:
        tests: int
        passes: int
        failures: int

    CurrentResult = Stats(0, 0, 0)

    def __init__(self, directory):
        self.list = directory

    def test(self, bin_file, type, arg):
        self.list.sort()
        for i in self.list:
            i = i.replace(".ampl", "")
            self.out = subprocess.run(
                ['../ampl/bin/' + bin_file, './TestCases/' + type + '/' + arg + '/' + i + '.ampl'],
                capture_output=True)
            with open('./Results/' + type + '/' + i + '.txt') as f:
                result = f.read()
            print(result)
            self.display_result(i + '.ampl', result == (self.out.stdout.decode() + self.out.stderr.decode()))

    def display_result(self, file, res):
        self.CurrentResult.tests += 1
        if res:
            print("\033[1;30;42m%-30s %9s\033[0m" % (file, "PASS"))
            self.CurrentResult.passes += 1
        else:
            print("\033[1;30;41m%-30s %9s\033[0m" % (file, "FAIL"))
            self.fails.insert(self.CurrentResult.failures - 1,
                              [file.replace(".ampl", ""), self.out.stdout.decode() + self.out.stderr.decode()])
            self.CurrentResult.failures += 1

    def display_stats(self):
        print("%i TESTS: %i PASSES and %i FAILS" % (
            self.CurrentResult.tests, self.CurrentResult.passes, self.CurrentResult.failures))
        print(str(round(self.CurrentResult.passes / self.CurrentResult.tests, 4) * 100) + '%')

    @staticmethod
    def hash(bin_file, file):
        with open(file) as f:
            country = f.readline()
            out = subprocess.run(['../ampl/bin/' + bin_file, 'co', 'to'])



if __name__ == '__main__':

    argument = Util.get_argument()
    # Get arguments
    if len(argument) == 3:
        arg = argument[1] + " " + argument[2]

    # Set directory and testxxx
    test = ''
    directory = list()
    loc = ''
    diff = ''
    bin_file = ''

    if argument[1] == 'scanner':
        directory = Util.get_directory('scanner/', argument[2])
        test = 'testscanner'
        diff = 'scanner'
        bin_file = 'testscanner'


    if argument[1] != 'hash':
        Util.make(test)
        test = Test(directory)
        print(bin_file)
        test.test(bin_file, argument[1], argument[2])
        test.display_stats()
        
        print("hoseeaaaaaeyy")
        print("-" * 80)
        print("Enter 0 to exit, or 1 to display differences in failed cases: ")

        for line in sys.stdin:
            if line.rstrip() == "1":
                diffy = Difference(diff)
                diffy.display_differences(test.fails)
                break
            if line.rstrip() == "0":
                break

