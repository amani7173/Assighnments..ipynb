{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "feac8cf6-ff3c-4963-b0b6-b82d1fd29575",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 4, 3, 2, 1, 0]\n"
     ]
    }
   ],
   "source": [
    "#1\n",
    "\n",
    "def  countDown(num):\n",
    "    newList = []\n",
    "    for i in range(num, -1, -1):\n",
    "        newList.append(i)\n",
    "    return newList\n",
    "print(countDown(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cd50f2d3-b9cf-45a1-b02e-f2f9ade2158d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "#2\n",
    "\n",
    "def print_and_return(list):\n",
    "    print(list[0])\n",
    "    return list[1]\n",
    "print (print_and_return([1,2]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9b57fa5b-c144-4fe8-9c76-e4363eabaf32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "#3\n",
    "def first_plus_length(list):\n",
    "    print(list[0])\n",
    "    return len(list)\n",
    "print(first_plus_length([1,2,3,4,5]) + 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8aff4f3f-0fa8-473e-ba69-24eb836af899",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[7, 7, 7, 7]\n"
     ]
    }
   ],
   "source": [
    "#4\n",
    "def length_and_value(size,value):\n",
    "    newList = []\n",
    "    for i in range(size):\n",
    "        newList.append(value)\n",
    "    return newList\n",
    "print(length_and_value(4,7))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b89d02db-55b8-428d-834a-6d7c2289cf73",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
