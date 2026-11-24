# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/amjoice/say-what-broke-20261124/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/amjoice/say-what-broke-20261124/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

One line of software error copy for the [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) bounty on make.fun.

## The line

> Disk full. Your file is safe in memory, but memory forgets. Free 100 MB or this work dies with the tab.

103 characters. It names the real failure (the disk is full), tells the user
exactly what to do next (free 100 MB), and says the quiet part out loud:
unsaved work only lives in memory, and memory forgets.

## How it works

`main.py` (Python standard library only, no third-party imports) writes the
line to `/output/entry.txt`. The output is deterministic — byte-identical on
every run.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
