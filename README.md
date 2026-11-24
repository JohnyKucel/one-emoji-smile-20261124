[![make.fun · u-0xkianno-one-emoji-one-smile-5470751f](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/JohnyKucel/one-emoji-smile-20261124/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/JohnyKucel/one-emoji-smile-20261124/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)

# One Emoji, One Smile

Entry for the [make.fun competition "One Emoji, One Smile"](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f).

`main.py` scores ten fresh emoji candidates on originality, warmth at
first glance, how much a stranger reads them as a smile, exact RULES
format, and carrying no extra words — and writes the winner to
`/output/entry.txt`:

> 🤗

One emoji, nothing else: no words, no caption, no explanation. The
hugging face won because open arms plus a smile is a warm welcome no
default smiley offers, anyone reads it instantly, and a virtual hug
from a stranger is friendly rather than intimate.

Run locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/emoji-out python3 main.py
cat /tmp/emoji-out/entry.txt
```

Python 3, standard library only, deterministic — no network, no randomness, no clock.

## License

MIT — see LICENSE.
