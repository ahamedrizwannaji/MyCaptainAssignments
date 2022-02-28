{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "APP Task 2.py",
      "provenance": [],
      "authorship_tag": "ABX9TyMy6OP1AaXGObfB3vCjI0kU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ahamedrizwannaji/MyCaptainAssignments/blob/main/APP_Task_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5S6inzeZ8hjA"
      },
      "source": [
        "#Task 1\n",
        "\n",
        "#Write a python program for Fibonacci numbers\n",
        "\n",
        "#Input the number of the terms needed\n",
        "\n",
        "nterms = int(input(\"Enter the required no. of terms: \"))\n",
        "\n",
        "# first two terms\n",
        "n1, n2 = 0, 1\n",
        "count = 0\n",
        "\n",
        "# check if the number of terms is valid\n",
        "if nterms <= 0:\n",
        "   print(\"Please enter a positive integer\")\n",
        "\n",
        "# if there is only one term, return zero\n",
        "elif nterms == 1:\n",
        "   print(\"Fibonacci sequence: \", n1)\n",
        "\n",
        "# generate fibonacci sequence\n",
        "else:\n",
        "   print(\"Fibonacci sequence:\")\n",
        "   while count < nterms:\n",
        "       print(n1)\n",
        "       nth = n1 + n2\n",
        "       # update values\n",
        "       n1 = n2\n",
        "       n2 = nth\n",
        "       count += 1"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 2\n",
        "\n",
        "\"\"\"Write a python program to print all \n",
        "positive values in the list\"\"\"\n",
        "\n",
        "#Creating a list with the user input\n",
        "\n",
        "e = []\n",
        "num = int (input(\"Enter number of Elements in List = \"))\n",
        "for i in range(1,num+1):\n",
        "  ele = int (input(\"Enter elements:\"))\n",
        "  e.append(ele)\n",
        "print(\"List = \", e)\n",
        "\n",
        "#\n",
        "for a in e:\n",
        "\n",
        " if a >= 0:\n",
        "  print (a, end = \" \")"
      ],
      "metadata": {
        "id": "NWEWtKyRjqsx"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}