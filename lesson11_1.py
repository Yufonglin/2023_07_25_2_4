{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m執行具有 'c:\\Users\\wnedy\\AppData\\Local\\Programs\\Python\\Python311\\python.exe' 的儲存格需要 ipykernel 套件。\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/wnedy/AppData/Local/Programs/Python/Python311/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "import random\n",
    "def get_score() -> list:\n",
    "    score = []\n",
    "    for i in range(5):\n",
    "        score.append(random.randint(50, 100))\n",
    "    return score\n",
    "\n",
    "nums = int(input(\"請輸入學生數:\"))\n",
    "with open(\"names.txt\",encoding=\"utf-8\") as file:\n",
    "    file.read()\n",
    "\n",
    "\n",
    "students = []\n",
    "for _ in range(nums):  #其中_是省略運算子，當下列城市不需要時，可以使用\n",
    "    scores = get_score()\n",
    "    students.append(scores)\n",
    "students"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.11.3"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
