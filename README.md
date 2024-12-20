<!-- THIS FILE IS GENERATED AUTOMATICALLY. -->
<!-- DO NOT EDIT THIS FILE. -->
<!-- EDIT README_gen.md INSTEAD. -->
# berkeley-hardfloat patches (stable-v0.1.0)

This repository is a slightly modified version of UC Berkeley's [Hardfloat](https://github.com/ucb-bar/berkeley-hardfloat) library.
All modifications can be found in patches under [`patches/`](./patches/),
applied in lexicographical order.
It's the version that powers the [Spade hardfloat library](https://github.com/ethanuppal/hardfloat-spade).

## Usage

Head over to the [Releases](https://github.com/ethanuppal/berkeley-hardfloat/releases) page and download one of the `.zip` files.
For example, you can get `v0.1.0` by running

```shell
wget https://github.com/ethanuppal/berkeley-hardfloat/archive/refs/tags/v0.1.0.zip
```

## Local Development

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

_This changelog is automatically generated._

### 1. Icarus fix (see [changes](./patches/1-icarus-fix.patch))

This patch fixes an issue with Icarus Verilog:
```
error: 'sqrtOpOut' has already been declared in this scope.
It was declared here as a net.
```

