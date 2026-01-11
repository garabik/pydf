# Welcome to pydf!

**pydf** is all-singing, all-dancing, fully colourised `df(1)`-clone
written in Python.

It is written by [Radovan Garabík](https://github.com/garabik)
&lt;garabik @ kassiopeia.juls.savba.sk&gt;.

GitHub is the official new home to **pydf** after
[`kassiopeia.juls.savba.sk`](https://kassiopeia.juls.savba.sk/~garabik/software/pydf.html).


# Requirements

**pydf** was written for linux, using specific linux features.
The fact it runs on other systems is pure coincidence,
but neverthless it happens to work on wide range of modern
Unix systems.


# Configuration

System-wide configuration is in `/etc/pydfrc`, per-user
configuration in `~/.pydfrc` (format of these files is the same).

Colours are one of:

- `none`, `default`
- `bold`, `underline`, `blink`, `reverse`, `concealed`
- `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`
- `on_black`, `on_red`, `on_green`, `on_yellow`, `on_blue`, `on_magenta`, `on_cyan`, `on_white`
- `beep`

`on_red` means that the background (instead of foreground) is painted
with red etc...


# Command Line Usage

**pydf** recognizes following parameters:

```console
# pydf --help
Usage: pydf [options] arg

Options:
  --help                show this help message
  -v, --version         show version
  -a, --all             include filesystems having 0 blocks
  -h, --human-readable  print sizes in human readable format (e.g. 1K 234M 2G)
  -H, --si              likewise, but use powers of 1000 not 1024
  -b BLOCKSIZE, --block-size=BLOCKSIZE
                        use BLOCKSIZE-byte blocks
  -l, --local           limit listing to local filesystems
  -k, --kilobytes       like --block-size=1024
  -m, --megabytes       like --block-size=1048576
  -g, --gigabytes       like --block-size=1073741824
  --blocks              use filesystem native block size
  --bw                  do not use colours
  -S, --scale-bars      scale bars to largest disk size
  --mounts=MOUNTS_FILE  File to get mount information from. On normal Linux
                        systems only /etc/mtab or /proc/mounts make sense.
                        Some other Unices use /etc/mnttab. Use /proc/mounts
                        when /etc/mtab is corrupted or inaccessible (the
                        output looks a bit weird in this case).
  -B, --show-binds      show 'mount --bind' mounts
  -i, --inodes          show inode instead of block usage
```


# Similar Utilities (in alphabetical order)

- **dfc** — colorful df clone written in C: https://github.com/rolinh/dfc
- **di** — disk information utility: https://diskinfo-di.sourceforge.io/
- **dysk** — advanced utility to display disk space usage, written in Rust: https://dystroy.org/dysk/
