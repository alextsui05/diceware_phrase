# diceware_phrase

Generate a diceware passphrase.

# Usage

Generate a five-word passphrase by default.

```
diceware_phrase.py
```

```
luckily rundown muppet calamari sixties
```

You can specify the number of words in the passphrase

```
diceware_phrase.py 10
```

```
shorter scorecard babble bullwhip conch commence shorty runny lankiness garland
```

# Data

By default, uses the EFF large wordlist, fetched from here:

https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt

Diceware wordlist is also included in the repository and can be swapped in by
changing the filename in the script.

# References

https://www.rempe.us/diceware/#eff

# Changelog

## 0.1.0 - 2018/12/23

* Implement `diceware_phrase` script
  * Support optional number of words parameter
  * Include EFF and Diceware word lists
