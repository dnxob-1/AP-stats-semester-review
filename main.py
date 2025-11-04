from selectFiles import selectSet
from mode import mode
from median import median
from range import range
from iqr import iqr
from calculate import calculate
from variance import variance
from createSet import makeSet
from mean import mean
from stdev import stdev
from fileRemover import removeFiles
from calculateZscore import zscore
from advanced import advancedSets
from displaySet import displayCurrentlySelectedSet
from plot import plotData
from normcdf import cumulativeDistFunc
from normpdf import probDensityFunc
from pe import peFunc
from moe import moeFunc
import platform
import os

try:
    if platform.system() == "Windows":
        import pyreadline as readline
    else:
        import readline
except ImportError:
    print("Error: Module not found")


HISTORY_FILE = ".shell_history"


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            for line in f:
                readline.add_history(line.strip())


def save_history():
    with open(HISTORY_FILE, "w") as f:
        for i in range(1, readline.get_current_history_length() + 1):
            f.write(readline.get_history_item(i) + "\n")


def mainTerms():
    print("hi. 'help' for help.")
    load_history()
    directory = "./"
    n = 0
    j = 0
    p = 0
    fileWorker = ""
    while True:
        command = input(">> ").strip()
        if command == "exit":
            print("nighty!")
            break
        elif command == "help":
            print(
                "Commands: help, clear, echo, ls, exit, select, set, mean, stdev, zscore, remove, set advanced, display, plot, normcdf, normpdf, median, mode, variance, iqr, range, calculate, pe, moe"
            )
        elif command == "clear":
            os.system("cls" if os.name == "nt" else "clear")
        elif command.startswith("echo "):
            print(command[5:])
        elif command.startswith("ls"):
            textFilesInDir = [f for f in os.listdir(directory) if f.endswith(".txt")]
            for file in textFilesInDir:
                print(file)
        elif command.startswith("select"):
            fileWorker = str(command.replace("select", "").strip())
            fileWorker = str(selectSet(fileWorker))
        elif command == "set":
            n += 1
            makeSet(n)
        elif command == "mean":
            mean(fileWorker)
        elif command == "stdev":
            stdev(fileWorker)
        elif command.startswith("remove"):
            wantGone = command.split()
            wantGone.remove("remove")
            removeFiles(wantGone)
        elif command == "zscore":
            zscore(fileWorker)
        elif command == "set advanced":
            j += 1
            p += 1
            advancedSets(j, p)
        elif command == "display":
            displayCurrentlySelectedSet(fileWorker)
        elif command == "plot":
            plotData(fileWorker)
        elif command == "normcdf":
            cumulativeDistFunc(fileWorker)
        elif command == "normpdf":
            probDensityFunc(fileWorker)
        elif command == "mode":
            mode(fileWorker)
        elif command == "range":
            range(fileWorker)
        elif command == "iqr":
            iqr(fileWorker)
        elif command == "median":
            median(fileWorker)
        elif command == "calculate":
            calculate()
        elif command == "variance":
            variance(fileWorker)
        elif command == "pe":
            peFunc()
        elif command == "moe":
            moeFunc()
        else:
            print("Unknown command.")


if __name__ == "__main__":
    mainTerms()
