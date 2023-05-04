# Max

## Learning Goals

* Pass an array into a function
* Create a helper function that finds a maximum value

## Background

There are many situations where you’ll find it helpful to have a function that finds the maximum (and minimum) value in an array. Since there is no built-in max function in C, you’ll create one in this practice problem. You can then use it in upcoming problem sets where it may be helpful!

<details>
<summary>Hints</summary>
    <ul>
        <li>Start out with a variable that keeps track of your max value. There are two ways to initialize this. You can start out using the lowest possible value (be careful you don’t start with zero, as the max value could be a negative number!) or you can start with the first element in the array.</li>
        <li>Loop through the array and reset this max value every time you find a value that’s larger.</li>
    </ul>
</details>

## Demo

## Getting Started

1. Log into [code.cs50.io](https://code.cs50.io/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/3/max.zip` followed by Enter in order to download a zip called `max.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip max.zip` to create a folder called `max`.
5. You no longer need the ZIP file, so you can execute `rm max.zip` and respond with “y” followed by Enter at the prompt.
6. Finally, right-click or control-click on the `max` folder and click “Open in CS50 Lab”. You should see the specification for this problem on the left-hand side and its distribution code on the right-hand side.

## Implementation Details

The `main` function initializes the array, asks the user to enter values, and then passes the array and the number of items to the `max` function. Complete the `max` function by iterating through even element in the array, and return the maximum value.

## Thought Question

* What types of programs can you think of that might benefit from a max helper function?

## How to Test Your Code

Your program should behave per the examples below.
```
max/ $ ./max
Number of elements: 3
Element 0: 2
Element 1: 10
Element 2: -1
The max value is 10.
```
```
max/ $ ./max
Number of elements: 4
Element 0: -100
Element 1: -200
Element 2: -3
Element 3: -5000
The max value is -3.
```

You can check your code using `check50`, a program that CS50 will use to test your code when you submit, by typing in the following at the `$` prompt. But be sure to test it yourself as well!
```
check50 cs50/labs/2022/fall/max
```
To evaluate that the style of your code, type in the following at the `$` prompt.
```
style50 max.c
```

## How to Submit

No need to submit! This is an optional practice problem.