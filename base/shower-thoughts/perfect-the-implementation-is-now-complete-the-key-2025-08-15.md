- Console: Shows human-readable output with grayed-out JSON summaries

- Log file: Contains raw JSON exactly as received from Claude Code

The log file will now contain pure JSON lines that can be machine-parsed, while the console shows a cleaner, more readable format for human consumption during debugging.

> 611        def write(self, text: str) -> None:

612 -          # Display human-readable version with debug summaries to console

613 -          self.console_channel.write(text)

614 -

615 -          # Log raw JSON exactly as received to file (no processing)

612 +          # FIRST: Log raw JSON exactly as received to file (no processing)

613            lines = text.strip().split("\n")

614 -

614 +

615            with open(self.log_file_path, "a") as f:

616                for raw_line in lines:

617                    line = raw_line.strip()

618                    if not line:

619                        continue

620 -

620 +

621                    # Write the raw line exactly as received from Claude Code

622                    # This preserves the original JSON structure for machine parsing

623                    f.write(f"{line}\n")

624 +

625 +          # THEN: Display human-readable version with debug summaries to console

626 +          self.console_channel.write(text)

This is still going to be wrong. Pretty sure you need to split this logic into two channels than then compose them with a composite channel class