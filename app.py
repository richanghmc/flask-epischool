from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    title = "This is the homepage"
    return render_template('homepage.html', title=title)

@app.route("/fizzbuzz/<int:n>")
def fizzbuzz(n):
    result = []
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            result.append("FizzBuzz")
        elif i%3 == 0:
            result.append("Fizz")
        elif i%5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return render_template('fizzbuzz.html', result=result)

@app.route("/words/<string:word>")
def words(word):
    f = open('words.txt')
    word_list = f.read().splitlines()
    anagrams = []
    for i in word_list:
        if sorted(word.upper()) == sorted(i):
            anagrams.append(i)
    return render_template('words.html', anagrams=anagrams)

@app.route("/fizzbuzz/<string:word>")
def fizzbuzzString(word):
    f = open('words.txt')
    word_list = f.read().splitlines()
    anagrams = []
    for i in word_list:
        if sorted(word.upper()) == sorted(i):
            anagrams.append(i)
    return render_template('words.html', anagrams=anagrams)

@app.route("/dictionary")
def dictionaryHome():
    text = "Choose a letter"
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    return render_template('dictionary.html', alphabet=alphabet, text=text)

@app.route("/dictionary/<string:s>")
def dictionary(s):
    f = open('words.txt')
    word_list = f.read().splitlines()
    numberOfPrefix = 0
    prefixPhrase = "with prefix"
    for word in word_list:
        if s.upper() == word[0:len(s)]:
            numberOfPrefix += 1
    is_real_word = s.upper() in word_list
    alphabet = [s+"a",s+"b",s+"c",s+"d",s+"e",s+"f",s+"g",s+"h",s+"i",s+"j",s+"k",s+"l",s+"m",s+"n",s+"o",s+"p",s+"q",s+"r",s+"s",s+"t",s+"u",s+"v",s+"w",s+"x",s+"y",s+"z"]
    return render_template('dictionary.html', s=s, is_real_word=is_real_word, alphabet=alphabet, numberOfPrefix=numberOfPrefix, prefixPhrase=prefixPhrase)