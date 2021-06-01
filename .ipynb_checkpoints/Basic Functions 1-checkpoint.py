{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4defbf16-dae1-45f0-9a0e-030aa3f45c12",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "def a():\n",
    "    return 5\n",
    "print(a())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1d2a5143-ae1d-48dd-8f57-a1e97c095fd5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "#2\n",
    "def a():\n",
    "    return 5\n",
    "print(a()+a())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d2cec37d-e9e2-453d-82ef-30e19d16eebc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "def a():\n",
    "    return 5\n",
    "    return 10\n",
    "print(a())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6d1c8a0d-dbe9-42f8-bdb5-fafffc822161",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "#4\n",
    "def a():\n",
    "    return 5\n",
    "    print(10)\n",
    "print(a())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6e1efe6c-c3d7-4f1a-904f-b38445b9c1b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "5\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for +: 'NoneType' and 'NoneType'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-d576ca284938>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mc\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0mc\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: unsupported operand type(s) for +: 'NoneType' and 'NoneType'"
     ]
    }
   ],
   "source": [
    "#6copy\n",
    "def a(b,c):\n",
    "    print(b+c)\n",
    "print(a(1,2) + a(2,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2f3c29f8-3b89-4ea1-a660-8e33f8150a04",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25\n"
     ]
    }
   ],
   "source": [
    "#7\n",
    "def a(b,c):\n",
    "    return str(b)+str(c)\n",
    "print(a(2,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "53ae876d-070f-44a1-87aa-a84d0ce8fc13",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "#8\n",
    "def a():\n",
    "    b = 100\n",
    "    print(b)\n",
    "    if b < 10:\n",
    "        return 5\n",
    "    else:\n",
    "        return 10\n",
    "    return 7\n",
    "print(a())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "8f724b80-f5cc-45d8-a44e-c12f9ccd0d42",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "14\n",
      "21\n"
     ]
    }
   ],
   "source": [
    "#9\n",
    "def a(b,c):\n",
    "    if b<c:\n",
    "        return 7\n",
    "    else:\n",
    "        return 14\n",
    "    return 3\n",
    "print(a(2,3))\n",
    "print(a(5,3))\n",
    "print(a(2,3) + a(5,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bc183f33-feb3-4838-b0b6-4cdb2f21acdb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "#10\n",
    "def a(b,c):\n",
    "    return b+c\n",
    "    return 10\n",
    "print(a(3,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "15df4ec7-b837-4528-bcf0-841210cf4589",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "500\n",
      "500\n",
      "300\n",
      "500\n"
     ]
    }
   ],
   "source": [
    "#11\n",
    "b = 500\n",
    "print(b)\n",
    "def a():\n",
    "    b = 300\n",
    "    print(b)\n",
    "print(b)\n",
    "a()\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "121e4235-53b8-4c04-9042-e9c8eac16780",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "500\n",
      "500\n",
      "300\n",
      "500\n"
     ]
    }
   ],
   "source": [
    "#12\n",
    "b = 500\n",
    "print(b)\n",
    "def a():\n",
    "    b = 300\n",
    "    print(b)\n",
    "    return b\n",
    "print(b)\n",
    "a()\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "4ffce0c9-4eb2-4093-bc3f-532a765a1b49",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "500\n",
      "500\n",
      "300\n",
      "300\n"
     ]
    }
   ],
   "source": [
    "#13\n",
    "b = 500\n",
    "print(b)\n",
    "def a():\n",
    "    b = 300\n",
    "    print(b)\n",
    "    return b\n",
    "print(b)\n",
    "b=a()\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "450d8185-c2d5-4a64-909b-6b23a3d0fa26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "#14\n",
    "def a():\n",
    "    print(1)\n",
    "    b()\n",
    "    print(2)\n",
    "def b():\n",
    "    print(3)\n",
    "a()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ffce76d1-cd23-47ee-bd9b-fa1448816189",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n",
      "5\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "#15\n",
    "def a():\n",
    "    print(1)\n",
    "    x = b()\n",
    "    print(x)\n",
    "    return 10\n",
    "def b():\n",
    "    print(3)\n",
    "    return 5\n",
    "y = a()\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be094f46-dee1-45ef-bc93-1943b034c12d",
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
