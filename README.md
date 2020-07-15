my **al**bert **ex**tensions

how do I get them?

```shell
# clone repo and switch to py dir
$ git clone https://github.com/dorind/alex && cd alex/py

# ensure modules dir
$ mkdir -p ~/.local/share/albert/org.albert.extension.python/modules

# copy all extensions
$ cp -rf . ~/.local/share/albert/org.albert.extension.python/modules/

# or a one long liner
$ git clone https://github.com/dorind/alex && cd alex/py && mkdir -p ~/.local/share/albert/org.albert.extension.python/modules && cp -rf . ~/.local/share/albert/org.albert.extension.python/modules/ && echo "remember to enable the extensionsin albert" || echo "ouch, something went wrong, good luck."
```

now invoke albert, click on settings, check `Python` and enable `Random`, `Text Case`, `Window Finder` and/or `Word Unscramble`

## random

enter words separated by space and see them being randomized before your very eyes!

```
rnd marry john mike

> mike
```

sorry Mike, looks like you're tipping today

## text case

ever needed to quickly change the case of a piece of text? me neither

```
tc abracadabra
> abracadabra
> ABRACADABRA
> AbRaCaDaBrA
> aBrAcAdAbRa
```

## window finder

this is inspired by `window_switcher.py` with Ed Perez and Manuel Schneider as original authors

I've added small changes so that you can quickly find and switch to windows based on title too.

```
x nix
> Thunar - Desktop 0
> Xfce4 terminal - Desktop 0
```

pretty cool, huh?

## word unscramble

with this extension you can destroy your mates in case you ever need to unscramble words

thanks to the guys at [https://dwyl.com](https://dwyl.com) you have a word list containing

```shell
$ wc -l words

> 370103 words
```

that's right! 370,103 words

```
wu tang
> gant
> gnat
> tang
```

wth is a `gnat`? great question, according to google:

- a small two-winged fly that resembles a mosquito. Gnats include both biting and non-biting forms, and they typically form large swarms
- a person regarded as tiny or insignificant


