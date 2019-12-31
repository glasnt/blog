---
layout: post
title: On Language Oddities
subtitle: wat. 

redirect_from: /2016/05/28/on-language-oddities.html
---



_This post serves as an accompaniment to "JavaScript is Awe-ful" talk, and as a list of obscure language oddities_

## Let's talk about Ruby


### Bare words 

In Ruby, there is no such thing as 'bare words'. Some languages turn unknown objects into strings, but this does not exist in Ruby

```ruby
irb> ruby bare words
NameError: undefined local variable or method `words'
```

However, unknown methods in Ruby fall through to a method called `method_missing`, which can be overloaded in userspace in order to handle unknown methods

```ruby
irb> def method_missing(@args)
   >   args.join(" ")
   > end
irb> ruby bare words
"ruby bare words"
```

Although this is something that seems to be not a good way to handle code, it is how generic method functionality was used in [Ruby on Rails 2.0](http://apidock.com/rails/v2.0.0/ActiveRecord/Base/method_missing/class). Custom methods based on user tables would be parsed based on a tokenization of the method name. For example, `Customer.find_all_by_last_name(last_name)` would be split into "find all_by last_name", which would then search `Customer` based on the `last_name` field.

### Operator Precidence

In Ruby, the [order of operations](http://whatthefuckruby.tumblr.com/post/70164947137) places `not` in between the and/or symbols `&&` `||` and the and/or keywords `and` `or`. Because of this, when used in combination with not, `and` and `&&` are not interchangable. 

```ruby
irb> not true && false
false

irb> not true and false
true
```

Except for specific cases, stick to using `and` and `or` to avoid this issue, and to improve code readability (over `&&` and `||`)

## Let's talk about Haskell


### Logical Length
In Haskell, there is native functionality to calculate the length of a list

```haskell
λ> length [1,2]
2
```

However, the logic of this doesn't apply to tuples or other set lists. Due to how `fmap` and folding functionaly works, the length of a tuple isn't it's logical length.

```haskell
λ> length (1,2)
1
```


### Function overrides

The `let` operator in Haskell allows for variable assignment. However, `where` can be used to define values for specific variable values, including overloading of integers. 

```haskell
λ> let a = 2 + 2
λ> a
4

λ> let b = 2 + 2 where 2 + 2 = 5
λ> b
5
```


## Let's talk about Pascal

### Variable assignment

Pascal is one of only a few languages that uses `=` for equality and not assignment. In Pascal you use the operand `:=` for assignment. 

```pascal
Program boop(output);
VAR x: INTEGER;
begin
 x := 41;
 x += 1;
 writeln(x = 42);
end.
```
```pascal
TRUE
```


## Let's talk about Bash

### Numeric operations

Bash doesn't allow for native bare numeric operations. Unlike a *lot* of other languages, to be able to do mathematics in the command-line equations need to be evaluated and echoed out to terminal.

```bash
$ 4 + 2
bash: 4: command not found
$ $(( 4 + 2 ))
bash: 6: command not found
$ echo $(( 4 + 2 ))
6
```


## Let's talk about Elixir

### Type coersion

In elixir, type coersion occurs when types are not defined. However, there are some issues when integers are interpreted to be strings, such as [in this example](http://www.cursingthedarkness.com/2015/10/the-definitive-all-dancing-all-complete.html): 

```elixir
iex> Enum.map(1..5, fn(x) -> x*x end )
[1, 4, 9, 16, 25]

iex> Enum.map(6..10, fn(x) -> x*x end )
'$1@Qd'
```


## Let's talk about C

### Trigraphs

Although disabled by default in `gcc`, in some versions of `c++` trigraphs are enabled by default. [Trigraphs](ttp://stackoverflow.com/questions/1234582/purpose-of-trigraph-sequences-in-c") are combinations of punctuation that work around the limitations in ISO646 with regards to the available punctuation characters. 

```c
> printf("wat??!")
wat|
```


## Let's talk about Python

### Numeric comparison using `is`

One of the many [Python wats](www.youtube.com/watch?v=sH4XF6pKKmk) includes variation in the way integers can be compared, depending on their size. In this example, integers declared in separate statements that are larger than 256 are not the same object. However, defining them on the same line makes them reference the same underlying low level value, and are equal when compared using `is`

```python
>>> a = 256
>>> b = 256
>>> a is b 
True
>>> a = 257
>>> b = 257
>>> a is b
False
>>> a = 257; b = 257
>>> a is b
True
```

If you need to compare objects, be wary of using `is` as opposed to object-type specific introspection.

## Let's talk about Java

### Integer comparison

Simpler to the Python example, due to limitations in integer caching abilities in [Java](http://stackoverflow.com/a/2001861/124019), some integers may not always be equal

```java
java> Integer a = 1024;
java> Integer b = 1024;
java> a <= b
true
java> a >= b
true
java> a == b
false
```


## Let's talk about JavaScript

### Unlike object concatenation

In the canonical [JavaScript wat](https://www.destroyallsoftware.com/talks/wat), concatenation operations in JavaScript of empty object types produce interesting results

```javascript
> [] + []
""
> [] + {}
[object Object]
> {} + []
0
> {} + {}
NaN
```

## Let's talk about Scala

### Unlike object concatenation


Like the JavaScript example, the concatenation of an empty object and an empty string in Scala produces an unusual result. 

```scala
scala>  println({} + "")
()
```

## Let's talk about Swift

### Inefficient nested dictionary parsing

Although slated to be fixed in Swift 2.2.3, [complex static dictionaries](https://spin.atomicobject.com/2016/04/26/swift-long-compile-time/) are extremely inefficient in Swift, to the point where a 20-entry instance of the below example would take _hours_ to compile.

```swift
let cat_cafe = [
   "cats": [
      "01": ["nyan": "mew"],
      "02": ["nyan": "mew"],
      "03": ["nyan": "mew"],
      "04": ["nyan": "mew"],
      "05": ["nyan": "mew"],
      "06": ["nyan": "mew"],
      "07": ["nyan": "mew"],
      "08": ["nyan": "mew"],
      "09": ["nyan": "mew"],
      "10": ["nyan": "mew"],
      "11": ["nyan": "mew"],
      "12": ["nyan": "mew"],
      "13": ["nyan": "mew"],
      "14": ["nyan": "mew"],
      "15": ["nyan": "mew"]
   ]
]

print("Cat count: " + String(cat_cafe["cats"]!.count))
```

```shell
$ time -p xcrun swift cats.swift
Cat count: 15</code></pre>
real 828.78
```


## Let's talk about Perl

### Numeric equality

Numeric equality is achieved in Perl using `==`, which is normally used for equality across all object types. However, because of this limitation, and the way that string casting works in Perl, using `==` to check if two strings are the same [will always be true](http://stackoverflow.com/a/14046720/124019). 

```perl
DB<1> if ("foo" == "bar") { print "true" } else { print "false" }
true
```

Use the generic `eq` for equality across any object type.

## Let's talk about PHP

### Chained ternery operations

PHP has a ternery operand which allows for a short-hand way of doing an `if then else` statement. 

The left command will be executed if the condition is true, the right if it's false. 

```php
php> echo (TRUE ? "True" : "False");
True
```

However, unlike other languages with ternary operands, PHP's version isn't associative, so they [cannot be chained](http://phpsadness.com/sad/30) in a way that resembles an if-then-else tree. 

```php
echo (FALSE ? "one" : FALSE ? "two" : "three");
three
php> echo (FALSE ? "one" : TRUE ? "two" : "three");
two
php> echo (TRUE  ? "one" : TRUE  ? "two" : "three");
two
```

It is recommended that you avoid this ternery form for anything other than a single instance chain

## Let's talk about Powershell

### `>` and `<`

In PowerShell, you can use the operand `>` to achieve numeric comparison

```powershell
PS> if (2 > 1) { "true" } else { "false" }
true
```

However, the `<` operator has not been implemented. 

```powershell
PS> if (2 < 1) { "true" } else { "false" }
The '<' operator is reserved for future use.
```

The complete set of comparison operands in PowerShell is `-lt`, `-gt` and `-eq`.

