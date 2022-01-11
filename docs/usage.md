# Example Usage

Maybe not yet ... but if you insist:

## Call without arguments

```console
$ gengive
Usage: gengive [OPTIONS] COMMAND [ARGS]...

  Render text (Danish: gengive tekst).

Options:
  -V, --version  Display the gengive version and exit  [default: False]
  -h, --help     Show this message and exit.

Commands:
  verify   Answer the question if now is a working hour.
  version  Display the gengive version and exit
```

## Version command

```console
$ gengive version
Render text (Danish: gengive tekst). version 2022.1.11
```

## Verify command

Not yet for real - but a start:
```console
$ gengive verify requirements.txt
using configuration ({})
markdown may be OK
```
