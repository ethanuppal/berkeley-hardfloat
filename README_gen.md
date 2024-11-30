# berkeley-hardfloat (stable-{{VERSION_TAG}})

This repository is a slightly modified version of UC Berkeley's [Hardfloat](https://github.com/ucb-bar/berkeley-hardfloat) library.
All modifications can be found in patches under [`patches/`](./patches/),
applied in lexicographical order.
It's the version that powers the [Spade hardfloat library](https://github.com/ethanuppal/hardfloat-spade).

## Usage

First, clone the repository:

```shell
git clone https://github.com/ethanuppal/berkeley-hardfloat.git
```

Everything should be ready to use.

You can repair locally by running the build script:

```shell
chmod u+x ./build.sh
./build.sh
```

The build script assumes you have a valid Python installation with the python
binary in your `PATH` and a working internet connection.

## Rationale

The Verilog downloaded by `build.sh` has certain compilation issues fixed by this repository.

## Changelog

{{CHANGELOG}}
