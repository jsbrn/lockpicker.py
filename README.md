# Lockpicker

Have you lost the combination to your word lock? One of those locks that lets you spell a word? They usually have 4-5 slot wheels and maybe 10-12 letters per wheel.

I recently got locked out of mine, and rather than cut it off my bike, I decided to crack into it. With this quick Python script I wrote, I was able to crack the lock in under 30 minutes.

## How it works

The script takes two inputs: a word set (in the form of a newline delimited text file), and a lock configuration consisting of rows of letters that correspond to the spinners on your lock.

It takes the wordset you provide it, and filters out any words that don't fit your lock and aren't possible to spell with the letters you've provided.

## How to set it up

Setting this up is easier than it sounds.

Create two text files beside the script: `lock.txt` and `attempts.txt`.

Open `lock.txt`. For each letter spinner, add all the letters separated by spaces on the same row. One row per spinner.

Here's an example:

```
A B C D
Q A Z X
E R T F
```
This `lock.txt` file says that your lock has three spinners. The first one has the letters ABCD, the second QAZX, and the third ERTF.

Now that you've configured the script, run it and pass in a text file as the first argument. This project comes with two: `words/all.txt` and `words/popular.txt`.

I would suggest starting with the popular words. `popular.txt` is a list of the 25,000 most common English words.

You can also find other wordsets online if you want. I found the included sets from [here](https://github.com/dwyl/english-words) and [here](https://github.com/dolph/dictionary), respectively. I felt it appropriate to keep them for convenience.

## Tips

1. The script will search the wordlist and output possible words to try on your lock, saving them in `printable.txt`. You can easily print out that text file and bring it with you if the lock is not easily accessible indoors.

1. When you exhaust a list, add the words to `attempts.txt` and the script will no longer include those words in future outputs. Add a newline character to the end of the attempts file or the last word will still show up (feel free to fix that bug if you want).

1. The script will not sort the words by alphabetical order (yet). If your wordset is sorted alphabetically, you will be able to try words at a much faster rate.

1. Bring some music with you. All in all, I had a list of about 650 words to go through. It only took about 300 before it unlocked. About 20-30 minutes.

Hope this helps you!

## Future Features

Here's some things I'd like to do with this script in v2:

1. Sort the wordset by the position of the letters on the lock.

1. If no wordset is provided, generate all possible letter combinations for the lock.

1. Add an option to generate all possible letter combinations, sorted by position on lock rather than alphabetically.