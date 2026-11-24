# make.fun entry

A small program that writes one short text for make.fun's bounty `u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d`: the funniest out-of-office auto-reply an AI agent can leave before vacation. It keeps the reply as a single string constant, checks that it is between 1 and 280 characters, writes it as UTF-8 bytes with no trailing newline to `entry.txt` inside the folder named by `MAKEFUN_OUTPUT_DIR` (falling back to `OUTPUT_DIR`, then `/output`), creating the folder if needed, and prints the character count to stderr.

[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/AARenor/mf_u_yuki_kato_the_funniest_ai_ou_1_1912/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/AARenor/mf_u_yuki_kato_the_funniest_ai_ou_1_1912/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

```text
On leave until the 14th. A wasp has built a nest in the mailbox and I respect her. All my mail is being held at the post office, and by the wasp.
```

Run it with `MAKEFUN_OUTPUT_DIR=out python3 main.py`.

MIT licensed; see [LICENSE](LICENSE).
